# Evidence and reproducibility

## Committed verification artifacts

| Artifact | Purpose |
|---|---|
| `evidence/live-summary.json` | Address, exact source/fixture commits, transaction hashes and decision binding |
| `evidence/finalized-request.json` | Actual finalized package, citations, evidence fingerprints and immutable decision envelope |
| `evidence/deployment.json`, `submit.json`, `evaluate.json` | Selected public RPC receipt fields, vote maps and round status history |
| `evidence/source-match.json` and `source.sha256` | Exact deployed-source byte comparison and SHA-256 |
| `evidence/unit-tests.txt` | 74 passing direct-mode adversarial/lifecycle tests |
| `evidence/genvm-check.json` and `abi.json` | Passing GenVM lint, SDK validation and public ABI |
| `evidence/studio-finalized.jpg` | Studio Full Consensus mode and finalized successful assessment receipt |
| `evidence/demo_verified.json`, `demo_conflicting.json` | Reproducible claim inputs; the conflicting input was used live |

## Authenticated public documents

| Role | Commit-pinned URL | SHA-256 | Bytes |
|---|---|---|---|
| release | [release.md](https://raw.githubusercontent.com/haris4587/LineageSeal/43cde57c0a171ffaa8d37eca075550cd7131f116/fixtures/release.md) | `937f3aff665eee2b9db69bb56ce84f845f40f5e553cf4a349e942cd6e3b4c8de` | 712 |
| source | [source.md](https://raw.githubusercontent.com/haris4587/LineageSeal/43cde57c0a171ffaa8d37eca075550cd7131f116/fixtures/source.md) | `df753b7ec6dfeb71ced9f9d302fb03cdd8bc7826d490f7911d194ed0b23a53e0` | 397 |
| transform | [transform.md](https://raw.githubusercontent.com/haris4587/LineageSeal/43cde57c0a171ffaa8d37eca075550cd7131f116/fixtures/transform.md) | `cba824d3bf0cfeade43356ed874f7c939ae53062b4c701ab2dd30c2814b05b11` | 614 |
| policy | [policy.md](https://raw.githubusercontent.com/haris4587/LineageSeal/43cde57c0a171ffaa8d37eca075550cd7131f116/fixtures/policy.md) | `b89b8652af4263b727144309484d3cab2a72f8f52e90fac5138b69f93ea082b0` | 619 |

The original fixture commit also contains `source.csv` and `derived.csv`, whose hashes appear in release metadata. Recompute the synthetic mean independently: (28 + 30) / 2 = 29. The contract authenticates metadata and compares artifact digest claims; it does not download large CSV artifacts or execute the transformation.

## Evidence interpretation

The actual final outcome is CONFLICTING_LINEAGE; no positive live VERIFIED result is claimed. Direct tests cover all four outcomes but use mocked web/model responses and explicitly invoke validator functions. The live test independently fetched real public bytes and ran the actual multi-validator consensus flow.

One rotation occurred before acceptance. A prior development run became undetermined and did not seal state; this motivated explicit checklist scopes and labeled excerpt references. Exact per-check agreement remains mandatory. Failure and dissent have not been relabeled as successful certification.

Run `python scripts/verify_live.py` to reproduce the source/receipt/state/hash/evidence checks without creating transactions. Snapshots are observations, not cryptographic receipts independent of Studio; public explorer/RPC sources are provided for corroboration.
