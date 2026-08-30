# Password

요청마다 자격 증명을 검사하는 서버다.
`Authorization: Basic` 헤더로 받은 비밀번호를 서버가 보관한 해시와 대조하고, 일치할 때만 카운터를 돌려준다.

## 실행

```bash
go run .
```

## 확인할 것

```bash
curl -u alice:wonderland localhost:18080/whoami   # alice: 1
curl -u alice:wonderland localhost:18080/whoami   # alice: 2
curl -u bob:builder      localhost:18080/whoami   # bob: 1
curl -u alice:nope       localhost:18080/whoami   # invalid credentials
curl -u admin:nope       localhost:18080/whoami   # invalid credentials
```

이제 이름만 적어 보냈던 이전 방식과 달리 요청에 이름과 함께 비밀번호가 실린다.
서버는 `alice`라는 신원에 대한 주장을 뒷받침하는 증거를 요구하고, 그 증거를 검사한 뒤에서야 비로소 사용자의 요청을 받아들인다.

## 문제상황

비밀번호가 모든 요청에 실린다.

```bash
curl -u alice:wonderland -v localhost:18080/whoami 2>&1 | grep Authorization
# > Authorization: Basic YWxpY2U6d29uZGVybGFuZA==
```

Basic 인증은 `사용자이름:비밀번호`를 base64로 부호화할 뿐이므로 누구나 원래 문자열로 되돌릴 수 있다.
회선은 TLS로 가릴 수 있지만 TLS가 지켜 주는 것은 전송 구간뿐이고, 앞단의 프록시나 서버의 접근 로그에는
복호화된 값이 그대로 닿는다. 비밀번호라는 증거가 요청 횟수만큼 그 지점들을 통과하는 셈이다.

## 짚어둘 것

- **401 응답에는 반드시 `WWW-Authenticate`를 붙인다.** RFC 9110은 401을 만드는 서버가 클라이언트에게
  어떻게 인증하면 되는지 알리는 이 헤더를 보내도록 요구한다. 자격 증명이 없을 때뿐 아니라 비밀번호가 틀렸을 때도
  마찬가지다.
- **비밀번호는 해시로만 보관한다.** 저장소가 통째로 유출되더라도 공격자가 비밀번호 자체를 곧바로 얻지는 못한다.
- **`CompareHashAndPassword`는 두 해시를 상수 시간으로 비교한다.** 앞에서부터 한 바이트씩 비교하다가 처음 어긋나는
  지점에서 멈추면, 공격자가 응답 시간의 차이로부터 자신이 정답에 얼마나 근접했는지 가늠할 수 있다.
- **존재하지 않는 사용자에게도 해시 검사를 수행한다.** 이름을 찾지 못했을 때 곧바로 거절해 버리면 그 응답만
  눈에 띄게 빨라지므로, 공격자가 응답 시간만으로 어떤 이름이 실재하는지 가려낼 수 있다.
