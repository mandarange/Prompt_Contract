<div align="center">

# 🚀 Prompt Contract (한국어)
### *PM이 프롬프트를 리뷰하고, AI가 코드를 리뷰한다.*

[![English](https://img.shields.io/badge/README-English-111827?style=for-the-badge)](./README.md)
[![한국어](https://img.shields.io/badge/README-한국어-0EA5E9?style=for-the-badge)](./README.ko.md)

</div>

---

## 이 프로젝트가 필요한 이유

대부분 팀은 아직도 프롬프트를 일회성 대화처럼 다룹니다.
하지만 그 방식은 확장되지 않습니다.

**Prompt Contract**는 프롬프트를 다음과 같은 "제품 산출물"로 만듭니다.
- 버전 관리 가능
- 리뷰 가능
- 테스트 가능
- 재사용 가능

코드 PR 리뷰를 할 수 있는 팀이라면, 프롬프트 리뷰도 할 수 있습니다.

---

## 핵심 개념

**Prompt Contract**는 아래를 명확히 정의하는 구조화된 명세입니다.
1. **비즈니스 의도** (PM이 원하는 결과)
2. **실행 제약** (AI가 해야 할 것 / 하면 안 될 것)
3. **수용 기준** (품질을 검증하는 방법)
4. **실패 대응** (불확실할 때의 동작)

즉, PM/AI 엔지니어/리뷰어가 배포 전 같은 그림을 보게 합니다.

---

## 권장 저장소 구조

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

> 처음에는 "계약 1개 + 루브릭 1개 + 회귀 세트 1개"로 시작하세요.

---

## 빠른 시작

1. 템플릿으로 첫 계약서 작성
2. 수용 테스트 케이스 5~10개 정의
3. 프롬프트 변경용 PR 체크리스트 추가
4. 머지 전에 평가 실행
5. 포스트모템 피드백으로 지속 개선

---

## PR 리뷰 체크리스트

- [ ] 목표가 측정 가능하다
- [ ] 입력/출력이 명시되어 있다
- [ ] 도구 제한/안전 제약이 있다
- [ ] 엣지/실패 케이스가 문서화되어 있다
- [ ] 평가 루브릭이 연결되어 있다
- [ ] 회귀 예제가 연결되어 있다

---

## 라이선스

MIT. [LICENSE](./LICENSE) 참고.
