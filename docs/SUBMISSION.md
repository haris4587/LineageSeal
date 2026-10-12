# Intelligent Contracts submission

Contribution date: 2026-10-12

Title: LineageSeal — Evidence-bound dataset provenance consensus

Notes / Description (998 characters):

LineageSeal is a reusable GenLayer Intelligent Contract for dataset provenance. Callers lock a release, 1–4 upstream datasets, transformation and policy with commit-pinned public evidence, SHA-256 and byte lengths. Validators independently retrieve and authenticate every file, assess lineage and validate source-grounded citations. Deterministic rules derive VERIFIED, PROVENANCE_GAPS, CONFLICTING_LINEAGE or INCONCLUSIVE. Numbered excerpts become exact quotes in code; objective fingerprints and per-check statuses require agreement. Immutable caller-bound requests, decision hashes, replay protection, bounded retries and prompt-injection defenses prevent silent evidence substitution or unsafe positive verdicts. 74 adversarial/lifecycle tests, GenVM lint and SDK validation pass. The exact GitHub source is deployed on Studionet. A finalized Full Consensus demo detects a false upstream version as CONFLICTING_LINEAGE. Synthetic fixtures; documentary assessment, not proof of collection truth.

## Evidence links

- Repository: https://github.com/haris4587/LineageSeal
- Exact deployed source: https://github.com/haris4587/LineageSeal/blob/dfb05b2bb4046bbc9b1116c97fde44bca19a0cdf/contracts/lineage_seal.py
- Tests: https://github.com/haris4587/LineageSeal/blob/main/tests/test_lineage_seal.py
- Deployment and live evidence: https://github.com/haris4587/LineageSeal/blob/main/docs/DEPLOYMENT.md
- Contract explorer: https://explorer-studio.genlayer.com/address/0x4cE703B965B121e243cE517e62Eff58d5c9E50E7
- Full Consensus assessment: https://explorer-studio.genlayer.com/tx/0x6f2ac8c3b0a102603b20e01d9d3efc8072031ae50bd2bf4fbb2371427d78e975
- Finalized decision state: https://github.com/haris4587/LineageSeal/blob/main/evidence/finalized-request.json
- Security model: https://github.com/haris4587/LineageSeal/blob/main/docs/SECURITY.md
- Reproduction script: https://github.com/haris4587/LineageSeal/blob/main/scripts/verify_live.py

The submission package is prepared for the standalone Intelligent Contracts category. No portal contribution has been submitted by this workflow.
