"""Read-only reproduction of the committed Studionet evidence; no wallet/signing."""
import base64
import hashlib
import json
from pathlib import Path
import requests
from genlayer_py.abi import calldata

ROOT = Path(__file__).resolve().parents[1]


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def rpc(method, params):
    response = requests.post('https://studio.genlayer.com/api', json={
        'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': params}, timeout=40)
    response.raise_for_status()
    result = response.json()
    assert 'error' not in result, result.get('error')
    return result['result']


def read_request(address, sender, request_id):
    result = rpc('gen_call', [{'from': sender, 'to': address, 'type': 'read',
        'status': 'finalized', 'data': '0x' + calldata.encode(
            {'method': 'get_request', 'args': [request_id]}).hex()}])
    # Studio returns raw encoded calldata; newer Node API returns a result envelope.
    if isinstance(result, dict):
        assert result['status']['code'] == 0, result['status']
        result = result['data']
    raw = bytes.fromhex(result.removeprefix('0x'))
    return json.loads(calldata.decode(raw))


def verify():
    summary = json.loads((ROOT / 'evidence/live-summary.json').read_text())
    source = base64.b64decode(rpc('gen_getContractCode', [summary['address']]))
    assert source == (ROOT / 'contracts/lineage_seal.py').read_bytes(), 'source mismatch'
    assert hashlib.sha256(source).hexdigest() == summary['source_sha256']
    for tx_hash in summary['transactions'].values():
        tx = rpc('eth_getTransactionByHash', [tx_hash])
        assert tx['status'] == 'FINALIZED', tx['status']
        assert tx['leader_only'] is False, 'not Full Consensus'
        assert tx['result_name'] == 'MAJORITY_AGREE', tx['result_name']
    record = read_request(summary['address'], summary['sender'], summary['request_id'])
    assert record['status'] == summary['outcome']
    assert record['package_hash'] == digest(record['package'])
    expected_id = digest({'domain': 'LineageSeal/v1', 'chain_id': 61999,
        'contract': summary['address'], 'sender': record['submitter'], 'package': record['package']})
    assert record['id'] == expected_id
    assert record['package'] == json.loads((ROOT / 'evidence/demo_conflicting.json').read_text())
    decision = record['attempts'][-1].copy()
    decision_hash = decision.pop('decision_hash')
    assert digest(decision) == decision_hash == summary['decision_hash']
    assert decision['request_id'] == record['id'] == summary['request_id']
    assert decision['package_hash'] == record['package_hash']
    assert decision['baseline_hash'] == record['baseline_hash']
    assert len(decision['result']['fingerprints']) == len(record['package']['evidence'])
    for item, fingerprint in zip(record['package']['evidence'], decision['result']['fingerprints']):
        response = requests.get(item['url'], timeout=30)
        response.raise_for_status()
        body = response.content
        assert len(body) == item['bytes'] == fingerprint['bytes']
        assert hashlib.sha256(body).hexdigest() == item['sha256'] == fingerprint['sha256']
        assert fingerprint['status'] == 'AUTHENTICATED'
    print('Verified: final source, Full Consensus receipts, finalized verdict, decision hash and evidence bytes.')
    return record


if __name__ == '__main__':
    verify()
