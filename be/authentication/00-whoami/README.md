# Whoami

튜토리얼의 출발점이 되는 서버다.
사용자 이름을 `X-User` 헤더로 받아서, 그 사용자가 몇 번째로 요청했는지에 대한 정보를 되돌려준다.

## 실행

```bash
go run .
```

## 확인할 것

```bash
curl -H 'X-User: alice' localhost:18080/whoami   # alice: 1
curl -H 'X-User: alice' localhost:18080/whoami   # alice: 2
curl -H 'X-User: bob'   localhost:18080/whoami   # bob: 1
curl -H 'X-User: alice' localhost:18080/whoami   # alice: 3
```

헤더에 기입한 사용자 이름을 식별자로 카운터가 누적된다. 마치 서버가 사람을 구분하고 있는 것처럼 보인다.

## 문제상황

이 서버는 헤더의 사용자 정보에 대한 검증을 전혀 하지 않는다.

```bash
curl -H 'X-User: admin' localhost:18080/whoami   # admin: 1
```

헤더에 적힌 이름은 주장일 뿐이고, 그 주장을 뒷받침하는 증거가 부재하다.
서버는 요청을 보낸 쪽이 정말 admin인지 확인할 방법 없이 그 주장을 그대로 믿는다.

## 짚어둘 것

- **카운터를 담은 map은 mutex로 보호한다.** Go의 map은 동시 접근에 안전하지 않고,
  각 요청은 별도의 goroutine에서 실행되므로 동시성에 대한 보호가 필요하다.
- **카운터는 메모리에만 있다.** 서버를 재시작하면 사라지고, 인스턴스를 여러 대로 늘리면 서로 공유되지 않는다.
  이 한계는 이후 챕터에서 다루도록 한다.
