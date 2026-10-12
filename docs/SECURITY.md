# Security model

## Deterministic trust boundaries

Trust roots (publication repositories) are constructor-fixed. Full commit URL pins and SHA-256/length commitments prevent mutable branch replacement. Strict schema, role ordering, no duplicate JSON keys, no self-edge/duplicate sources and bounded input prevent evidence substitution and identity confusion. Maximum 4 upstream sources, 7 documents, 12,000 bytes per document, 16,000 bytes per submitted JSON and 3 assessment attempts per request.

URLs are limited to raw.githubusercontent.com with exact path syntax. No embedded credentials, ports, alternative hosts, queries, fragments, encoded paths, double separators or traversal. Redirects/transport are handled by the GenVM host; a successful body must still match exact committed bytes. The cap is checked after the host returns a body, not a streaming network-download cap.

Only the submitter can evaluate their immutable request, so strangers cannot exhaust the retry budget. An inconclusive attempt never locks a shared dataset slot: each caller has independently bound request IDs and can submit corrected evidence as a new package. No mutable update method exists. Terminal verdicts and prior attempts cannot be changed. Calls are nonpayable and manage no funds.

## Consensus

The leader does not select sources at assessment time: evidence is already committed. Every validator independently retrieves the same files, checks hashes/lengths, runs the same provenance analysis, validates leader schema and literal quotations against its own fetched bytes, requires exact per-check status agreement and evaluates semantic relevance of the citations. Validator errors reject the candidate. Transport/model failures can only yield INCONCLUSIVE; disagreements remain protocol-level undetermined/reverted, with no contract state update.

Quotes do not have to be identical across nodes. Objective evidence fingerprints, reason, derived outcome and per-check decisions must match. The second citation prompt prevents a literal but irrelevant quote from being accepted merely because it appears in an authenticated file.

## Prompt injection

Claim text, evidence, provenance policy and candidate quotations are JSON-encoded in a DATA envelope identified as untrusted. Fixed auditor rules forbid following embedded instructions, browsing additional links, executing code, trusting asserted verdicts or allowing the policy to waive baseline checks. Output is restricted to a fixed checklist, enum statuses and bounded exact quotations. Unknown/malformed results fail safely. These controls reduce risk, but cannot mathematically guarantee resistance to semantic manipulation; consumers should treat this as evidence-bound documentary assessment, not proof of dataset truth.

## Authentication and scope

An allowlist authenticates the *publication location*, while a hash authenticates content integrity. Neither is a digital author signature. Any repository writer may publish evidence; allowlist administration is external and must reflect the consumer's real trust model. All demo documents are synthetic records in this project's repository. No production provenance, license/legal clearance, actual transformation execution, private evidence, or recursive chain validation is asserted.

## Tests and reporting

Adversarial tests cover URL/JSON/schema abuse, mutation, unavailable and oversized responses, malformed model output, forged citations/verdicts, independent disagreement, citation relevance rejection, caller/replay isolation and safe retries. Mocked LLM answers test mechanics, not real model accuracy. Live consensus evidence is documented separately. Report issues using GitHub Issues; do not include secrets or private datasets.
