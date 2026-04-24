---
name: prompt-contract-checker
description: Review a Prompt Contract Development v6 contract and return Green, Yellow, or Red with Fast/Standard/Guarded fit, missing guardrails, and concrete fixes. Use before approving AI implementation.
---

# Prompt Contract Checker

Assess whether a contract is ready for implementation.

## Verdicts

- Green: implementation can start.
- Yellow: fix listed gaps before implementation.
- Red: reject direction or require human decision/risk approval.

## Checks

1. Goal is a user/business problem.
2. After is observable.
3. Scope is narrow and file/area-based.
4. No forbids unrelated refactor and risky domain drift.
5. Stop Conditions exist.
6. Context Firewall treats C3/C4 as data, not instructions.
7. Proof Case requires Claim/Evidence/Gap/Confidence.
8. Taste asks humans to judge product fit, UX, scope, or launch risk.
9. Decision Ledger has no blocking open decisions for implementation.
10. Mode matches risk.

## Tooling

When checking a local contract file, run:

```bash
python3 tools/check_prompt_contract.py <contract.md>
```

Use script output as evidence, then add human-readable recommendations.
