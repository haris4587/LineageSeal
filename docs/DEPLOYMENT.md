# Deployment and confirmed live test

Verified on 2026-10-12 using the built-in Studio account. Network: Studionet (chain 61999). Execution mode: Normal (Full Consensus), with Simulation Mode off. No external wallet.

| Item | Verified value |
|---|---|
| Contract | [0x4cE703B965B121e243cE517e62Eff58d5c9E50E7](https://explorer-studio.genlayer.com/address/0x4cE703B965B121e243cE517e62Eff58d5c9E50E7) |
| Final source commit | [dfb05b2bb4046bbc9b1116c97fde44bca19a0cdf](https://github.com/haris4587/LineageSeal/commit/dfb05b2bb4046bbc9b1116c97fde44bca19a0cdf) |
| Source SHA-256 | `023b57fec17ade002f25a4010d579add2df2c879403571045b55d93970be8364` |
| Fixture commit | `43cde57c0a171ffaa8d37eca075550cd7131f116` |
| Request ID | `67b3c6f49645119f14b9983a6621461ad0f5f358acc24aabd54c1e4e2b21d04a` |
| Final verdict | **CONFLICTING_LINEAGE** |
| Decision hash | `45b1a7b4d84c0a6017e0b2c4e408ed6ee71ea35ee800ddde1d9ad96b8bda2fbe` |
| Package hash | `5e497d6e48075a21f7c3758bb58c0d7f9192b5fcc935d3498d0caf8053eaf27d` |
| Baseline hash | `118c158e1e0d7908248b4f3f4cb94d17d5183b38ab9496dc649b95282e20fea1` |

| Transaction | Hash and explorer |
|---|---|
| deployment | [0xd6823975b6e1e9084f1e263483ccce10124628d1dbac9a3093aae3fb626e1345](https://explorer-studio.genlayer.com/tx/0xd6823975b6e1e9084f1e263483ccce10124628d1dbac9a3093aae3fb626e1345) |
| submit | [0x5c24655135c9df259dba544ab9ec28136fcf1c206becea1dcaaff138a57a2c33](https://explorer-studio.genlayer.com/tx/0x5c24655135c9df259dba544ab9ec28136fcf1c206becea1dcaaff138a57a2c33) |
| evaluate | [0x6f2ac8c3b0a102603b20e01d9d3efc8072031ae50bd2bf4fbb2371427d78e975](https://explorer-studio.genlayer.com/tx/0x6f2ac8c3b0a102603b20e01d9d3efc8072031ae50bd2bf4fbb2371427d78e975) |

All three transactions are FINALIZED with MAJORITY_AGREE and `leader_only=false`. The assessment required one leader rotation; the final vote map has three agree votes and two idle executions cancelled after quorum. This is a quorum result, not a claim of unanimous validation. Earlier development runs failed safely and were superseded by this exact source.

## What the test establishes

The claimant says StationObservations version 2.0 feeds DailyTemperature 2026.1. The commit-pinned records instead attest version 1.0 and explicitly exclude version 2.0. Validators independently fetched and authenticated all four documents, assessed the checklist and validated exact source-grounded citations.

| Check | Final status |
|---|---|
| release | SUPPORTED |
| source:StationObservations | CONFLICT |
| lineage:StationObservations | CONFLICT |
| transformation | SUPPORTED |
| policy | CONFLICT |

The finalized state contains one immutable attempt and the verified decision hash. Source bytes fetched through `gen_getContractCode` exactly equal the repository contract. Documentation-only commits after the source commit do not change those bytes.

## Reproduce the evidence without spending consensus quota

```sh
python -m pip install -r requirements-dev.txt
python scripts/verify_live.py
```

This read-only script checks source equality, finalized receipts and Full Consensus mode, request/package binding, final verdict, decision hash and public evidence bytes. It uses no key, wallet, signing or write transaction. Studio data can be reset; committed snapshots preserve what was observed, while RPC re-verification depends on availability of the deployment.

## Deploy a new instance

1. Open GenLayer Studio, load `contracts/lineage_seal.py` and choose Normal (Full Consensus).
2. Deploy with `publishers_json` set to the string `["haris4587/LineageSeal"]` (or your independently trusted publisher repositories).
3. Run `python scripts/build_demo.py 43cde57c0a171ffaa8d37eca075550cd7131f116`.
4. Submit the contents of `evidence/demo_conflicting.json`; read the actual request ID from the finalized submit receipt.
5. Evaluate that request ID, wait for successful consensus and FINALIZED, and read `get_request` with State set to Finalized.

The supplied fixtures are synthetic demonstrations. Metadata integrity and documentary lineage are evaluated; CSV execution, truthful collection and legal ownership are outside scope.
