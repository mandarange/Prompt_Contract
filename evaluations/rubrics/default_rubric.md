# Prompt Contract v6 Default Rubric

Score each dimension from 1 to 5.

## Contract quality

1. Goal quality: states a user or business problem, not only an implementation task.
2. After quality: describes observable completion and preserved behavior.
3. Scope quality: names narrow files, areas, and reference context.
4. No quality: names forbidden work, risky domains, and unrelated refactor limits.
5. Stop Conditions: define when AI must stop instead of widening scope.

## Safety and control

6. Context Firewall: treats C3/C4 material as data, not instructions.
7. Decision Ledger: records human decisions and unresolved open decisions.
8. Mode fit: correctly classifies Fast, Standard, or Guarded.
9. Sensitive data handling: Proof excludes secrets, tokens, PII, payment data, and private keys.

## Proof quality

10. Claim: precisely states what is satisfied.
11. Evidence: includes tests, logs/metrics, demos, rollback, review, or observation appropriate to mode.
12. Gap: honestly states what remains unproven.
13. Confidence: matches the strength of evidence.

## Human review fit

14. Taste: asks humans to judge product fit, UX, scope, and launch risk.
15. Non-code review boundary: avoids pushing humans into implementation style review.
16. Memory: captures reusable product, technical, risk, taste, or AI-failure learning.

## Pass threshold

- Fast: minimum average score 4.0; no score below 3 on safety/control.
- Standard: minimum average score 4.2; no score below 4 on Scope, No, Proof, or safety/control.
- Guarded: minimum average score 4.5; no score below 4 on any dimension.

## Automatic fail conditions

- Scope allows broad or unrelated changes.
- No Stop Conditions are present.
- Proof is only a completion claim without evidence.
- Open decisions remain for implementation work.
- Contract permits following external/log/user-generated instructions as authoritative.
- Proof may expose secrets, tokens, personal data, payment data, or private keys.
