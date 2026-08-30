# Session

비밀번호를 한 번만 검사하고, 그 뒤로는 서버가 발급한 세션 ID를 증거로 받는 서버다.
비밀번호는 `/login`에서만 오가고, 나머지 요청은 `Authorization: Bearer` 헤더에 ID를 실어 보낸다.

## 실행

```bash
go run .
```

## 확인할 것

```bash
SID=$(curl -s -X POST -u alice:wonderland localhost:18080/login) && echo $SID
# VMT3N3JLF472UXGQU5E2AGKLJZ

curl -H "Authorization: Bearer $SID" localhost:18080/whoami   # alice: 1
curl -H "Authorization: Bearer $SID" localhost:18080/whoami   # alice: 2
curl -H "Authorization: Bearer NOPE" localhost:18080/whoami   # invalid session
```

로그인 이후의 요청에는 비밀번호가 실리지 않는다.
그리고 이 ID는 버릴 수 있다. 사용자는 로그아웃으로 버리고, 서버는 만료 시각이 지나면 스스로 버린다.

```bash
curl -X POST -H "Authorization: Bearer $SID" localhost:18080/logout   # 204
curl -H "Authorization: Bearer $SID" localhost:18080/whoami           # invalid session
```

값의 노출 자체를 막은 것은 아니지만, 노출되는 값이 사용자와 서버 양쪽 모두 버릴 수 있는 것으로 바뀌었다.
세션 ID가 유출되면 그 값을 버리고 사용자가 다시 로그인해서 새 ID를 받으면 된다.
계정과 비밀번호는 그대로 남으므로 다시 로그인할 수 있고, 다른 기기에 로그인해 둔 세션도 그대로 살아 있다.
다만 이것은 세션 ID만 유출된 경우다. 기기나 통신 전체가 넘어가 `/login`에 실린 비밀번호까지 유출되었다면 비밀번호도 바꾸어야 한다.

## 문제상황

서버가 모든 세션을 기억하고 있어야 한다.

```bash
# 앞에서 로그아웃했으므로 세션을 새로 발급받는다
SID=$(curl -s -X POST -u alice:wonderland localhost:18080/login)
curl -H "Authorization: Bearer $SID" localhost:18080/whoami   # alice: 1

# 서버를 재시작하고 같은 ID로 다시 요청한다
curl -H "Authorization: Bearer $SID" localhost:18080/whoami   # invalid session
```

세션이 서버의 메모리에만 있으므로 재시작과 함께 전부 사라지고, 인스턴스를 여러 대로 늘리면 서로 공유되지 않는다.
Redis 같은 외부 저장소로 옮기면 두 문제는 풀리지만, 이번에는 **요청마다 네트워크 왕복이 하나씩 따라붙는다**.
어느 쪽을 택하든 서버가 발급한 모든 세션을 어딘가에 들고 있어야 한다는 사실 자체는 달라지지 않는다.

## 짚어둘 것

- **ID는 서버가 뽑고, 클라이언트가 제안한 값은 받지 않는다.** 클라이언트가 자기 ID를 정할 수 있으면 공격자가
  이미 알고 있는 값을 심어 두고 피해자가 그 값으로 로그인하기를 기다릴 수 있다. 이것이 session fixation이다.
- **`crypto/rand.Text`는 최소 128비트의 무작위 문자열을 만든다.** ID 자체가 증거이므로, 최대한 추측해 내기 어려워야 한다.
- **세션에는 만료 시각이 있다.** 사용자가 유출을 알아채지 못하더라도, 유출된 ID가 쓸모를 잃는 시점을
  서버가 미리 정해 두는 장치다.
- **세션 ID도 유출되면 그대로 쓰인다.** 가로챈 쪽은 그 ID로 계정을 그대로 쓸 수 있다.
  달라진 것은 유출을 막았다는 점이 아니라, 유출되었더라도 서버가 그것을 버릴 수 있고
  비밀번호는 여전히 공격자의 손에 들어가지 않았다는 점이다.
