---
name: prompt-contract-proof-case-writer
description: Write a Prompt Contract Development v6 Proof Case from implementation, tests, logs, demos, reviews, rollback plans, and observation plans. Use when the agent must prove completion with Claim/Evidence/Gap/Confidence.
---

# Prompt Contract Proof Case Writer

Turn implementation evidence into a Proof Case.

## Structure

```md
### Claim

<What is satisfied?>

### Evidence

- Test:
- Log/Metric:
- Flag/Rollback:
- Demo:
- Review:
- Observation:

### Gap

<What remains unproven or uncertain?>

### Confidence

Low / Medium / High
```

## Evidence Ladder

- L0 Claim
- L1 Demo
- L2 Test
- L3 Telemetry
- L4 Rollback
- L5 Independent Review
- L6 Time-boxed Observation

## Rules

- Confidence must match evidence strength.
- Always include Gap, even when confidence is High.
- Do not include secrets, tokens, customer personal data, payment data, or private keys.
- For Guarded work, include rollback and observation evidence or mark the gap explicitly.
