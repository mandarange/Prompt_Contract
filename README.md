<div align="center">

# 🚀 Prompt Contract
### *PM reviews prompts. AI reviews code.*

[![Stars](https://img.shields.io/github/stars/Prompt-Contract/Prompt_Contract?style=for-the-badge)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](./LICENSE)
[![English](https://img.shields.io/badge/README-English-111827?style=for-the-badge)](./README.md)
[![한국어](https://img.shields.io/badge/README-한국어-0EA5E9?style=for-the-badge)](./README.ko.md)

**Build prompt-first product workflows with clear contracts between PM intent and AI execution.**

</div>

---

## Why this exists

Most teams still treat prompting like ad-hoc chat.
That doesn’t scale.

**Prompt Contract** turns prompts into a product artifact:
- versioned
- reviewable
- testable
- reusable

If your team can review PRs, it can review prompts.

---

## ✨ Core idea

A **Prompt Contract** is a structured spec that defines:
1. **Business intent** (what outcome PM wants)
2. **Execution constraints** (what AI must and must not do)
3. **Acceptance criteria** (how we verify quality)
4. **Failure behavior** (what to do when uncertain)

This lets PM, AI engineer, and reviewer align before shipping.

---

## 🧱 Recommended repo structure

```text
.
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
│  └─ playbooks/
├─ README.md
└─ README.ko.md
```

> Start small: one contract + one rubric + one regression set.

---

## ⚡ Quick start

1. Create your first contract from a template.
2. Define 5–10 acceptance cases.
3. Add a PR checklist for prompt changes.
4. Run evaluation before merge.
5. Keep improving with postmortem feedback.

---

## ✅ Contract checklist (for PR review)

- [ ] Objective is measurable
- [ ] Inputs/outputs are explicitly defined
- [ ] Tool limits and safety constraints are present
- [ ] Edge/failure cases are documented
- [ ] Evaluation rubric is attached
- [ ] Regression examples are linked

---

## 🌟 What makes this “star-worthy”

- **Simple enough for day-1 use**
- **Strict enough for production reliability**
- **Clear PM ↔ AI handoff language**
- **Portable across coding assistants and agents**

Think of this as the missing layer between product requirement docs and AI runtime behavior.

---

## 🛣️ Roadmap

- [ ] v0.1 Contract template pack
- [ ] v0.2 Evaluation harness examples
- [ ] v0.3 CI automation guide
- [ ] v1.0 Real-world case studies

---

## 🤝 Contributing

PRs are welcome for:
- contract templates
- evaluation rubrics
- practical case studies
- CI workflows for prompt quality gates

---

## License

MIT. See [LICENSE](./LICENSE).
