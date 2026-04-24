<div align="center">

# 🚀 Prompt Contract (한국어)
### *PM은 계약을 승인하고, AI는 계약 안에서 만들고 증명한다.*

[![English](https://img.shields.io/badge/README-English-111827?style=for-the-badge)](./README.md)
[![한국어](https://img.shields.io/badge/README-한국어-0EA5E9?style=for-the-badge)](./README.ko.md)

</div>

---

## 이 프로젝트가 필요한 이유

대부분 팀은 아직도 프롬프트를 일회성 대화처럼 다룹니다.
하지만 그 방식은 확장되지 않습니다.

**Prompt Contract**는 AI 작업을 제품 계약으로 만듭니다.
- PM 의도를 구현 전에 명확히 한다
- AI 작업 범위를 좁고 검토 가능하게 만든다
- 완료 주장이 아니라 증거 기반 Proof를 요구한다
- 사람 리뷰를 코드가 아니라 Taste와 Risk에 집중시킨다

핵심 문장:

> PM은 계약을 승인하고, AI는 계약 안에서 만들고 증명하며, 사람은 감각과 위험만 판단한다.

---

## 핵심 루프

```text
Contract → Context → Build → Proof Case → Taste → Memory
```

팀에서는 짧게 이렇게 말하면 됩니다.

```text
Contract → Build → Proof → Taste
```

모든 의미 있는 작업은 Safe 6-Line Contract로 시작합니다.

```text
Goal
After
Scope
No
Proof
Taste
```

---

## v6가 추가하는 보호 장치

| 문제 | v6 보호 장치 |
|---|---|
| AI가 틀린 목표를 정확하게 구현 | Goal + After 분리 |
| AI가 Scope를 넓힘 | Scope + No + Stop Conditions |
| 외부 문서/로그/이슈의 지시 오염 | Context Firewall |
| Proof처럼 보이는 완료 주장 | Proof Case |
| PM이 코드 리뷰어가 됨 | Taste Language |
| 반복 실패가 조직 지식으로 남지 않음 | Contract Memory |
| 사람이 결정할 일을 AI가 추론 | Decision Ledger |

전체 명세: [docs/prompt_contract_development_v6.md](./docs/prompt_contract_development_v6.md)

---

## 권장 저장소 구조

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

처음에는 "계약 1개 + Proof Case 1개 + Taste Review 1개"로 시작하세요.

---

## 빠른 시작

1. [contracts/templates/prompt_contract_template.md](./contracts/templates/prompt_contract_template.md)를 복사합니다.
2. `Goal`, `After`, `Scope`, `No`, `Proof`, `Taste`를 채웁니다.
3. `Mode`를 `Fast`, `Standard`, `Guarded` 중 하나로 정합니다.
4. 계약 체크를 실행합니다.

```bash
python3 tools/check_prompt_contract.py path/to/contract.md
```

5. 구현 전에 계약을 승인합니다.
6. Taste/Risk 리뷰 전에 Proof Case를 요구합니다.

---

## Mode 가이드

| Mode | 대상 | 최소 Evidence |
|---|---|---|
| Fast | 문구, 작은 UI, 작은 내부 수정 | Demo 또는 Test |
| Standard | 일반 기능, CRUD, API 변경, 버그 | Test + Telemetry/Log + Proof Case |
| Guarded | auth, payment, billing, privacy, migration, infra | Test + Telemetry + Rollback + Independent Review + Observation |

---

## PR 리뷰 체크리스트

- [ ] Goal이 구현명이 아니라 사용자/비즈니스 문제다
- [ ] After가 관찰 가능한 완료 상태다
- [ ] Scope가 좁고 파일/영역 기준이다
- [ ] No가 금지 작업과 위험 영역을 명확히 한다
- [ ] Stop Conditions가 명시되어 있다
- [ ] Proof가 Claim/Evidence/Gap/Confidence 구조다
- [ ] Taste가 코드 스타일이 아니라 제품 판단이다
- [ ] Open decisions가 구현 전에 해소되어 있다

---

## 포함된 Codex 스킬

이 저장소는 v6 런타임용 로컬 Codex 스킬을 포함합니다.

- `prompt-contract-maker`: 러프한 의도를 Safe 6-Line Contract로 변환
- `prompt-contract-checker`: 계약을 Green, Yellow, Red로 판정
- `prompt-contract-safe-builder`: 승인된 계약 범위 안에서만 구현
- `prompt-contract-review-trio`: Contract, Regression, Risk 리뷰 수행
- `prompt-contract-proof-case-writer`: 증거 기반 Proof Case 작성
- `prompt-contract-taste-memory-keeper`: PM Taste 리뷰와 Memory 업데이트 준비

---

## 라이선스

MIT. [LICENSE](./LICENSE) 참고.
