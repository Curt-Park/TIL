# Authentication

## 인증이란

암호학 표준 참고서인 *Handbook of Applied Cryptography*의 공저자 van Oorschot은, 웹 보안까지 범위를 넓혀 다시 쓴 교재에서 인증을 이렇게 정의한다. [1]

> Authentication is the process of using supporting evidence to corroborate an asserted identity.

**인증이란 주장된 신원을 뒷받침하는 증거로 확증하는 과정**이다.

**신원**은 시스템이 다른 대상과 구별하여 다루는 단위이며, 이 문서에서는 사용자에 대한 식별자다.
**증거**는 그 주장이 참임을 뒷받침하는 것이다.

클라이언트가 자신의 신원을 주장하고, 서버는 어떤 과정을 거쳐 그것이 참인지에 대한 여부를 판단한다.
이 튜토리얼은 **어떤 증거로 어떻게 신원을 확증하는지**에 대한 다양한 방법과 각 방법의 장단점을 다룬다.

## 목차

| # | 챕터 | 문제 | 해결 | 다루는 내용 |
|---|---|---|---|---|
| [00](00-whoami/) | Whoami | HTTP 요청은 그 자체로는 그것이 누구의 요청인지 알 수 없다 | 클라이언트가 요청 헤더에 식별자를 실어 보낸다 | `X-User` 헤더로 받는 사용자별 카운터 |
| [01](01-password/) | Password | 헤더에 아무 이름이나 적으면 그만이라 제시된 신원이 정당한지 확인할 수 없다 | 요청마다 비밀번호를 함께 받아 저장된 해시와 대조한다 | `Authorization: Basic`, 비밀번호 해시 저장, 상수 시간 비교와 응답 시간 노출, 401의 `WWW-Authenticate` |
| [02](02-session/) | Session | 비밀번호가 요청마다 오간다. 거쳐 가는 지점마다 노출되는데, 한 번 노출되면 계정 또한 노출된다 | 서버가 생성한 무작위 ID로 비밀번호를 대신하고, 필요시 드랍한다 | `Authorization: Bearer`로의 전환, 로그아웃과 만료, in-memory 저장소의 한계 및 external 저장소 부담 |
| 03 | JWT | 서버가 모든 세션을 기억해야 한다. 조회 비용, 재시작 시 소실, 확장 시 공유 | 서명으로 위조를 막아 서버가 아무것도 기억하지 않게 한다 | JWS 구조, 알고리즘 선택, `alg: none`과 검증 누락, 취소가 불가능하다는 한계와 access / refresh token 분리 |
| 04 | Cookie | JavaScript가 읽을 수 있는 곳에 증거를 두면 XSS 한 번에 통째로 털린다 | `HttpOnly` cookie로 옮겨 스크립트로부터 격리한다. 브라우저가 자동으로 붙여 주는 것은 덤이다 | `Set-Cookie` 구조, `Domain` / `Path` / `Expires` / `Max-Age`, `Secure`, localStorage와의 비교 |
| 05 | CSRF | cookie가 자동으로 붙는 탓에 다른 사이트가 사용자 몰래 요청을 보낼 수 있다 | 요청의 출처를 확인한다 | `SameSite`, CSRF token 대조, XSS와의 위협 모델 비교 |
| 06 | OAuth 2.0 / OIDC | 사용자의 비밀번호를 우리가 보관하고 직접 검증해야만 한다 | 검증을 외부 제공자에게 위임한다 | 인가와 인증의 구분, Authorization Code 흐름과 PKCE |

## 참고 자료

1. P. C. van Oorschot, *Computer Security and the Internet: Tools and Jewels from Malware to Bitcoin*, 2nd ed., Springer, 2021 — 3장 도입부. [저자 공개본](https://people.scs.carleton.ca/~paulv/toolsjewels.html)
