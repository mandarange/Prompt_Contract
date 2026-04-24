---
name: prompt-contract-review-trio
description: Run the Prompt Contract Development v6 Review Trio over an implementation: Contract Review, Regression Review, and Risk Review. Use after code changes and before proof/taste handoff.
---

# Prompt Contract Review Trio

Review implementation against the approved contract.

## Contract Review

Check:

- Goal/After match the implementation.
- Scope was not exceeded.
- No was not violated.
- Decision Ledger was followed.

## Regression Review

Check:

- Existing API, UX, data, and state behavior are preserved.
- New tests reinforce existing coverage instead of replacing it.
- Edge cases and failure states are covered for the chosen mode.

## Risk Review

Check:

- Security, auth, privacy, payment, billing, migration, and infra risks.
- Proof/logs do not expose secrets, tokens, PII, payment data, or private keys.
- Rollback and observation match the selected mode.
- Context Firewall was respected.

## Output

Return:

```md
## Contract Review
Verdict:
Findings:

## Regression Review
Verdict:
Findings:

## Risk Review
Verdict:
Findings:
```
