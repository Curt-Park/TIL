# Cookie

증거를 페이지가 아니라 브라우저에 저장시키는 서버다.
로그인을 이 브라우저에 묶는 `state`와 그 뒤를 잇는 세션을 모두 cookie로 주고받으므로,
페이지의 JavaScript는 어느 쪽도 읽지 못한다.

앞 챕터와 마찬가지로 `:18080`이 우리 앱이고 `:19090`이 인증 제공자다.

## 실행

```bash
go run .
```

## 확인할 것

`state`가 URL과 cookie 두 경로로 함께 나간다.

```bash
JAR=$(mktemp)
curl -s -i -c $JAR localhost:18080/login | grep -iE '^set-cookie|^location'
# Set-Cookie: oauth_state=FXYTUX6DL66EEDNHC2OQD7276M; Path=/; Max-Age=300; HttpOnly; SameSite=Lax
# Location: http://localhost:19090/authorize?...&state=FXYTUX6DL66EEDNHC2OQD7276M
```

로그인을 마치면 앱은 `state` cookie를 버리고 세션 cookie를 내준다.

```bash
AUTH=$(curl -s -i -c $JAR -b $JAR localhost:18080/login | awk '/^[Ll]ocation:/{print $2}' | tr -d '\r')
CB=$(curl -s -i -u alice:wonderland "$AUTH" | awk '/^[Ll]ocation:/{print $2}' | tr -d '\r')
curl -s -i -c $JAR -b $JAR "$CB" | grep -iE '^set-cookie'
# Set-Cookie: oauth_state=; Path=/; Max-Age=0; HttpOnly; SameSite=Lax
# Set-Cookie: session=eyJhbGciOi...; Path=/; Max-Age=900; HttpOnly; SameSite=Lax
```

이후 요청에는 `Authorization` 헤더를 붙이지 않는다. 브라우저가 알아서 실어 보낸다.

```bash
curl -s -b $JAR localhost:18080/whoami   # alice: 1
curl -s -b $JAR localhost:18080/whoami   # alice: 2
curl -s        localhost:18080/whoami    # no session
```

### 앞 챕터의 주입이 막힌다

공격자가 자기 계정으로 `code`와 `state`를 얻어 그 주소를 피해자에게 열게 하는 공격이다.

```bash
JAR2=$(mktemp)
AUTH_B=$(curl -s -i -c $JAR2 -b $JAR2 localhost:18080/login | awk '/^[Ll]ocation:/{print $2}' | tr -d '\r')
ATT=$(curl -s -i -u bob:builder "$AUTH_B" | awk '/^[Ll]ocation:/{print $2}' | tr -d '\r')

curl -s -b $JAR  "$ATT"   # state does not belong to this browser
curl -s -b $JAR2 "$ATT"   # 302 (공격자 자신의 브라우저에서는 정상 로그인)
```

공격자가 만든 주소에는 공격자의 `state`가 실려 있는데, 피해자의 브라우저에는 그 값이 없다.
공격자는 남의 브라우저에 값을 맡길 수 없으므로 이 대조를 통과할 방법이 없다.

### JavaScript는 세션을 보지 못한다

브라우저로 `http://localhost:18080/`을 열고 로그인하면 페이지가 두 값을 보여 준다.

```
document.cookie: (비어 있음)
fetch('/whoami'): alice: 1
```

페이지의 스크립트는 세션을 읽지 못하는데 요청은 성공한다.
`HttpOnly`가 `document.cookie`에서 가리고, 첨부는 브라우저가 대신 하기 때문이다.
페이지가 증거를 직접 다루지 않고도 쓸 수 있게 된 것이 앞 챕터들과 달라진 점이다.

## 문제상황

브라우저는 **요청이 어디로 가는지**만 보고 cookie를 붙인다. 누가 그 요청을 시키는지는 보지 않는다.

```bash
# 다른 사이트가 시킨 요청인 것처럼 보내도 서버는 구별하지 못한다
curl -s -b $JAR -H 'Origin: http://evil.example' -X POST localhost:18080/reset
# alice: reset
```

그래서 공격자의 페이지에 이런 폼을 넣어 두고 피해자가 열게 하면, 피해자의 세션 cookie가 실린 채로 요청이 나간다.

```html
<form action="http://localhost:18080/reset" method="POST">
  <input type="submit" value="당첨을 확인하세요">
</form>
<script>document.forms[0].submit()</script>
```

이것이 CSRF다. 증거를 훔칠 필요가 없고, 브라우저가 알아서 붙여 준다는 성질을 그대로 이용한다.
자동 첨부는 앞에서 문제를 푼 바로 그 성질이므로, 해결책과 대가가 같은 뿌리에서 나온다.

막는 방법은 이 cookie가 이미 달고 있다.

```
Set-Cookie: session=...; HttpOnly; SameSite=Lax
```

`SameSite=Lax`는 다른 사이트가 시작한 요청에 cookie를 붙이지 말라고 브라우저에 이르는 지시다.
위의 폼 전송은 이 지시에 따라 cookie 없이 나가고, 서버는 세션이 없는 요청으로 보아 거절한다.
사용자가 링크를 눌러 직접 이동하는 것은 `Lax`가 허용하므로, 다른 사이트에서 우리 서비스로 들어오는 평범한 이동은 그대로 동작한다.

## 짚어둘 것

- **`SameSite`는 브라우저가 지키는 약속이다.** 서버는 요청을 누가 시켰는지 알 수 없고, 위의 `curl` 실행이
  그것을 보여 준다. 값을 붙일지 말지 판단하는 쪽이 브라우저이므로, 브라우저를 쓰지 않는 클라이언트에는
  이 방어가 존재하지 않는다.
- **`Lax`가 모든 것을 덮지는 않는다.** 같은 사이트로 취급되는 하위 도메인에서 오는 요청은 막지 않고,
  상태를 바꾸는 일을 `GET`으로 처리하면 그것도 막지 않는다. 남는 자리는 요청마다 예측 불가능한 값을 하나 더
  요구하는 CSRF token으로 메운다. cookie와 달리 이 값은 브라우저가 자동으로 붙여 주지 않으므로,
  다른 사이트는 만들어 낼 수 없다.
- **`HttpOnly`와 `SameSite`는 서로 다른 위협을 막는다.** 앞은 페이지에 끼어든 스크립트가 값을 읽는 것을,
  뒤는 다른 사이트가 값을 쓰게 만드는 것을 막는다. 한쪽만으로는 다른 쪽이 열린다.
- **`Secure`는 실제 배포에서 반드시 켠다.** 이 코드는 `http://localhost`로 시연하느라 꺼 두었다.
  켜면 브라우저가 평문 HTTP 요청에는 cookie를 붙이지 않는다.
- **cookie는 HTTP 인증 스킴이 아니다.** 그래서 401에 실어 보낼 `WWW-Authenticate` challenge가 없다.
  페이지를 다루는 앱이라면 보통 로그인 화면으로 보내며, 이 서버는 `curl`로 읽기 쉽도록 401에 짧은 문구만 담는다.
- **`localStorage`와의 차이는 자동 첨부와 격리다.** `localStorage`에 둔 값은 스크립트가 읽어서 헤더에
  직접 실어야 하고, 같은 곳을 페이지에 끼어든 스크립트도 읽을 수 있다.
  대신 자동으로 붙지 않으므로 CSRF는 겪지 않는다.
