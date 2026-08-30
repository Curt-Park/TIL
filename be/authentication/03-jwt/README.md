# JWT

아무것도 기억하지 않는 서버다.
저장된 상태를 가리키는 ID 대신, 사용자 이름을 담고 서명한 토큰을 클라이언트가 직접 들고 다닌다.

## 실행

```bash
go run .
```

## 확인할 것

```bash
# RFC 7515는 base64url로 인코딩하되 뒤의 '=' 패딩을 모두 제거하도록 규정한다.
# base64 명령은 입력 길이가 4의 배수가 아니면 나머지 글자를 오류 없이 버리므로, 패딩을 도로 채워 넣어야 한다.
b64() { printf '%s' "$1" | base64 | tr '+/' '-_' | tr -d '='; }
d64() { printf '%s========' "$1" | cut -c1-$(( (${#1}+3)/4*4 )) | base64 -d; }

TOKEN=$(curl -s -X POST -u alice:wonderland localhost:18080/login) && echo $TOKEN
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbGljZSIsImV4cCI6MTc4ODA4ODEwN30.aLz2ndF6TXcDxOkOP9dRomvjWuqE1o1wkeb_PEWQZ-c

curl -H "Authorization: Bearer $TOKEN" localhost:18080/whoami   # alice: 1
curl -H "Authorization: Bearer $TOKEN" localhost:18080/whoami   # alice: 2
```

점으로 나뉜 세 부분은 각각 header, payload, 그리고 앞의 두 부분에 대한 서명이다.

```bash
d64 $(echo $TOKEN | cut -d. -f1)   # {"alg":"HS256","typ":"JWT"}
d64 $(echo $TOKEN | cut -d. -f2)   # {"sub":"alice","exp":1788088107}
```

앞의 두 부분은 JSON이지만, 세 번째는 HMAC-SHA256의 원시 32바이트라서 디코딩해도 읽을 수 있는 글자가 나오지 않는다.
읽는 대신 같은 값을 직접 계산해 보면 서명이 무엇인지 드러난다.

```bash
echo $TOKEN | cut -d. -f3
# xRWCHQLM1_UID2jxZApxDv14YwQyv3Fof43TByJIVHQ

# 앞의 두 부분을 점으로 이은 문자열에 secret으로 HMAC-SHA256을 건다
printf '%s' "$(echo $TOKEN | cut -d. -f1,2)" \
  | openssl dgst -sha256 -hmac 'tutorial-secret-not-for-real-use' -binary \
  | base64 | tr '+/' '-_' | tr -d '='
# xRWCHQLM1_UID2jxZApxDv14YwQyv3Fof43TByJIVHQ
```

secret을 아는 쪽은 누구나 같은 값을 만들 수 있고, 모르는 쪽은 만들 수 없다.

세션 방식은 서버가 저장해 둔 값을 조회하여 대조하는 것으로 유효성을 판단했지만, 여기에는 대조할 저장소가 없다.
토큰이 스스로 자신의 주인을 밝히고 서버는 그 내용이 위조되지 않았는지만 확인하므로,
사칭을 막는 일이 전부 서명 검증에 달려 있다.

```bash
# payload만 admin으로 바꿔치기한다
TAMPERED="$(echo $TOKEN | cut -d. -f1).$(b64 '{"sub":"admin","exp":9999999999}').$(echo $TOKEN | cut -d. -f3)"
curl -H "Authorization: Bearer $TAMPERED" localhost:18080/whoami   # invalid token

# 서명이 필요 없다고 선언하는 토큰을 만든다
FORGED="$(b64 '{"alg":"none"}').$(b64 '{"sub":"admin","exp":9999999999}')."
curl -H "Authorization: Bearer $FORGED" localhost:18080/whoami     # invalid token
```

그리고 서버를 재시작해도 토큰은 그대로 통한다. 기억해 둔 것이 없으니 잃어버릴 것도 없다.

```bash
curl -H "Authorization: Bearer $TOKEN" localhost:18080/whoami   # alice: 1
```

세션 방식에서 외부 저장소로 옮겨야 풀리던 재시작과 인스턴스 공유 문제가, 인증을 저장소에 의존하지 않고
서명 검증만으로 처리함으로써 해소되었다.

## 문제상황

발급한 토큰을 도로 거둘 수 없다.

```bash
curl -X POST -H "Authorization: Bearer $TOKEN" localhost:18080/logout   # 404
```

02의 `/logout`에 해당하는 것이 이 서버에는 없다. 버릴 대상을 서버가 가지고 있지 않기 때문이다.
재시작조차 소용이 없다는 사실은 앞에서 이미 확인했다. 유출된 토큰은 `exp`가 지날 때까지 그대로 유효하다.

무효화하려면 `secret`을 바꾸는 수밖에 없는데, 그러면 그 순간 발급되어 있던 모든 사용자의 토큰이 한꺼번에 죽는다.
버릴 수 있는 단위가 02에서는 세션 하나였는데 여기서는 서비스 전체로 되돌아간 셈이다.

그래서 실무에서는 토큰의 수명을 짧게 잡고, 만료되면 다시 로그인하는 대신 refresh token으로 새 토큰을 받아 간다.
refresh token은 거둬들일 수 있어야 하므로 서버가 다시 기억해야 하지만, 요청마다가 아니라 갱신할 때만 조회하면 된다.
상태를 없앤 것이 아니라 조회 빈도를 낮춘 것이다.

## 짚어둘 것

- **payload는 서명될 뿐 암호화되지 않는다.** 위에서 `d64`로 그대로 읽어 낸 것처럼, 토큰을 가진 쪽은 누구나 내용을 본다.
  서명이 막는 것은 열람이 아니라 변조이므로, 남이 보면 안 되는 값을 담아서는 안 된다.
- **알고리즘을 토큰에서 읽지 않는다.** header의 `alg`를 그대로 믿고 검증 방식을 고르면, 공격자가 `none`이라고 적어
  서명 검사를 통째로 건너뛰게 만들 수 있다. 이 서버는 검증 방식을 HMAC-SHA256으로 고정해 두었으므로 `alg`에 무엇이
  적혀 있든 결과가 달라지지 않는다.
- **서명 비교에는 `hmac.Equal`을 쓴다.** 바이트 단위로 비교하다가 어긋나는 지점에서 멈추면, 응답 시간의 차이로부터
  올바른 서명을 한 바이트씩 맞춰 나갈 수 있다.
- **직접 구현한 것은 구조를 드러내기 위해서다.** 실무에서는 검증된 라이브러리를 쓴다. `alg` 처리, 키 회전, 만료 시각의
  허용 오차처럼 틀리기 쉬운 부분이 많고, 이 서버는 그중 최소한만 다룬다.
