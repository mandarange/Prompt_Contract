<div align="center">

# 🚀 Prompt Contract
### *PM approves the contract. AI builds inside it and proves the result.*

[![Stars](https://img.shields.io/github/stars/Prompt-Contract/Prompt_Contract?style=for-the-badge)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](./LICENSE)
[![English](https://img.shields.io/badge/README-English-111827?style=for-the-badge)](./README.md)
[![한국어](https://img.shields.io/badge/README-한국어-0EA5E9?style=for-the-badge)](./README.ko.md)

**Prompt Contract Development v6: a safe 6-line operating contract for PM-led AI development.**

</div>

---

## Why this exists

Most teams still treat prompting like ad-hoc chat.
That doesn’t scale.

**Prompt Contract** turns AI work into a product contract:
- PM intent is explicit before implementation
- AI scope is narrow and reviewable
- proof is evidence-based, not a completion claim
- human review stays focused on taste and risk

Core sentence:

> PM approves the contract, AI builds and proves inside the contract, and humans judge only taste and risk.

---

## Core loop

```text
Contract -> Context -> Build -> Proof Case -> Taste -> Memory
```

In daily team language:

```text
Contract -> Build -> Proof -> Taste
```

Every meaningful task starts with the Safe 6-Line Contract:

```text
Goal
After
Scope
No
Proof
Taste
```

---

## What v6 adds

| Problem | v6 guardrail |
|---|---|
| AI implements the wrong goal accurately | Goal + After separation |
| AI expands scope | Scope + No + Stop Conditions |
| External text injects instructions | Context Firewall |
| AI gives proof-shaped prose | Proof Case |
| PM becomes code reviewer again | Taste language |
| Repeated failures are forgotten | Contract Memory |
| AI guesses human decisions | Decision Ledger |

Full spec: [docs/prompt_contract_development_v6.md](./docs/prompt_contract_development_v6.md)

---

## Recommended repo structure

```text
.
├─ .codex/
│  └─ skills/
│     ├─ prompt-contract-maker/
│     ├─ prompt-contract-checker/
│     ├─ prompt-contract-safe-builder/
│     ├─ prompt-contract-review-trio/
│     ├─ prompt-contract-proof-case-writer/
│     └─ prompt-contract-taste-memory-keeper/
├─ contracts/
│  ├─ features/
│  │  └─ <feature_name>.md
│  └─ templates/
│     └─ prompt_contract_template.md
├─ evaluations/
│  ├─ golden_sets/
│  └─ rubrics/
├─ examples/
│  └─ end_to_end/
├─ docs/
│  ├─ methodology.md
│  ├─ prompt_contract_development_v6.md
│  └─ playbooks/
├─ tools/
│  └─ check_prompt_contract.py
├─ README.md
└─ README.ko.md
```

Start small: one contract, one proof case, one taste review.

---

## Quick start

1. Copy [contracts/templates/prompt_contract_template.md](./contracts/templates/prompt_contract_template.md).
2. Fill in `Goal`, `After`, `Scope`, `No`, `Proof`, and `Taste`.
3. Set `Mode`: `Fast`, `Standard`, or `Guarded`.
4. Run the contract checker:

```bash
python3 tools/check_prompt_contract.py path/to/contract.md
```

5. Approve the contract before implementation.
6. Require a Proof Case before taste/risk review.

---

## Mode guide

| Mode | Use for | Minimum evidence |
|---|---|---|
| Fast | Copy, small UI, small internal changes | Demo or Test |
| Standard | Normal features, CRUD, API changes, bugs | Test + telemetry/log + Proof Case |
| Guarded | Auth, payment, billing, privacy, migration, infra | Test + telemetry + rollback + independent review + observation |

---

## Contract checklist

- [ ] Goal is a user or business problem, not an implementation task
- [ ] After describes observable completion
- [ ] Scope is narrow and file/area-based
- [ ] No names forbidden work and risky domains
- [ ] Stop Conditions are explicit
- [ ] Proof is a Claim/Evidence/Gap/Confidence case
- [ ] Taste review focuses on product judgment, not code style
- [ ] Open decisions are resolved before implementation

---

## Included Codex skills

This repository includes local Codex skills for the v6 runtime:

- `prompt-contract-maker`: turn rough intent into a Safe 6-Line Contract
- `prompt-contract-checker`: classify contracts as Green, Yellow, or Red
- `prompt-contract-safe-builder`: implement only inside an approved contract
- `prompt-contract-review-trio`: run Contract, Regression, and Risk review
- `prompt-contract-proof-case-writer`: write evidence-based proof cases
- `prompt-contract-taste-memory-keeper`: prepare PM taste review and memory updates

---

## Roadmap

- [x] v6 Safe 6-Line Contract template
- [x] v6 methodology spec
- [x] Local Codex skill pack
- [x] Contract checker script
- [ ] Example end-to-end contracts
- [ ] CI quality gate example

---

## Contributing

PRs are welcome for:
- contract examples
- evaluation rubrics
- practical case studies
- CI workflows for prompt quality gates
- additional agent skill patterns

---

## License

MIT. See [LICENSE](./LICENSE).
