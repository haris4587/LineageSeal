# LineageSeal

A reusable GenLayer Intelligent Contract that seals documentary dataset provenance from authenticated, commit-pinned public evidence. AI interprets provenance; deterministic code controls evidence integrity, identity commitments, decision derivation and immutable history.

## What it does

A deployment fixes a publication-repository trust allowlist. A caller submits an immutable package identifying a dataset release, 1–4 claimed upstream releases, their artifact SHA-256 digests, transformation claim, and exactly one release, one document per source, one transformation and one policy document. Evidence must use full 40-hex GitHub commit pins, expected SHA-256 and byte length. No branches, tags, credentials, arbitrary hosts, query strings or path traversal.

Leader and validators independently GET every file and verify status, raw bytes, digest and UTF-8 decoding. Each independently interprets release identity, source identity, every lineage edge, transformation completeness and policy compliance. Verdicts are derived from per-check statuses:

| Result | Meaning |
|---|---|
| VERIFIED | Every check has affirmative documentary support |
| PROVENANCE_GAPS | Readable documents omit required provenance facts |
| CONFLICTING_LINEAGE | Documents explicitly contradict a claimed version, digest, source or transformation |
| INCONCLUSIVE | Failed integrity/retrieval/model checks or ambiguous assessment; never positive certification |

UNKNOWN dominates conflict/gap. Validators compare exact objective fingerprints and check statuses; differing quotations are allowed only after literal grounding checks and a second source-grounded semantic citation judgment. A well-shaped answer alone never passes validation.

## Interface

- Constructor `publishers_json`: JSON array of trusted `owner/repository` publication locations, fixed forever (1–8).
- `submit(package_json) -> request_id`: validates and commits the complete evidence package; request ID binds chain, contract, caller and canonical package. Exact duplicate submissions by the same caller are rejected.
- `evaluate(request_id)`: submitter-only assessment. Up to three immutable attempts while pending/inconclusive. Conclusive decisions cannot be overwritten. Consensus failure reverts and does not spend an attempt.
- `get_request(request_id) -> JSON`: full committed package, baseline hash and decision history.
- `get_config() -> JSON`: immutable publishers and resource limits.

Each decision hash is SHA-256 of canonical UTF-8 JSON of the complete decision envelope **before** adding `decision_hash`. Canonicalization: sorted keys, separators `,` and `:`, `ensure_ascii=False`. Decision binds domain, request ID, package hash, baseline hash, attempt number and the full accepted result.

## Use and verification

```sh
python -m pip install -r requirements-dev.txt
python -m pytest -q tests
# executable may be in ~/.local/bin
 genvm-lint check contracts/lineage_seal.py
 genvm-lint schema contracts/lineage_seal.py
```

Direct tests use the official runner SDK and mocked I/O; they exercise captured validator functions explicitly. They are not a substitute for real Full Consensus. See [deployment](docs/DEPLOYMENT.md), [security](docs/SECURITY.md), [evidence](docs/EVIDENCE.md) and [submission](docs/SUBMISSION.md) for confirmed live results.

## Demonstration scope

Fixtures are explicitly synthetic station readings and a daily mean: (28 + 30)/2 = 29. The release attests StationObservations **1.0**; a claim using **2.0** should return conflicting lineage. CSV artifacts and metadata are public, reproducible and commit-pinned. This is a real consensus execution over synthetic evidence, not a claim about a production dataset.

## Limits

Authentication means bytes match a commitment at an allowed publication location. It does **not** prove a repository owner's legal identity, honest collection, complete disclosures, legal rights, artifact execution, or recursive provenance. A dishonest trusted publisher can publish consistent false records. Artifact digests are compared against metadata; the contract does not download large CSV datasets or execute transformations. Consumers must configure trusted publisher repositories carefully and independently authenticate the returned submitter/policy/package. LLM consensus mitigates individual errors, not correlated errors or guaranteed prompt-injection immunity. There are no payments, escrow, upgrades, owner overrides or external wallet requirements.

## Official references

Checked on 2026-10-12:
- [Equivalence Principle](https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle)
- [Non-determinism](https://docs.genlayer.com/developers/intelligent-contracts/features/non-determinism)
- [Web access](https://docs.genlayer.com/developers/intelligent-contracts/features/web-access)
- [Prompt injection](https://docs.genlayer.com/developers/intelligent-contracts/security-and-best-practices/prompt-injection)
- [GenVM lint and validation](https://docs.genlayer.com/api-references/genlayer-linter)

The exact pinned SDK exposes `Response.status` (not `status_code`) and JSON-format `exec_prompt` returns a dictionary. Both are tested against the actual SDK rather than copied from an inconsistent documentation example.
