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

이것이 CSRF(Cross-Site Request Forgery)다. 증거를 훔칠 필요가 없고, 브라우저가 알아서 붙여 준다는 성질을 그대로 이용한다.
앞에서 `state` 대조와 세션 보관을 해결한 것도 브라우저가 cookie를 알아서 붙인다는 바로 이 성질이었다.
하나의 성질이 해결책과 대가를 함께 가져오는 셈이다.

막는 방법은 이 cookie에 이미 적용되어 있다.

```
Set-Cookie: session=...; HttpOnly; SameSite=Lax
```

`SameSite=Lax`는 다른 사이트가 시작한 요청에 cookie를 붙이지 말라고 브라우저에 이르는 지시다.
위의 폼 전송은 이 지시에 따라 cookie 없이 나가고, 서버는 세션이 없는 요청으로 보아 거절한다.
사용자가 링크를 눌러 직접 이동하는 것은 `Lax`가 허용하므로, 다른 사이트에서 우리 서비스로 들어오는 평범한 이동은 그대로 동작한다.

## 짚어둘 것

- **`SameSite`는 브라우저가 지키는 규칙이다.** 서버는 그 요청을 어느 페이지가 시작했는지 알아낼 수 없고,
  앞의 `curl` 실행이 이 사실을 드러낸다. cookie를 붙일지 말지 판단하는 주체가 브라우저이므로,
  브라우저를 거치지 않는 클라이언트에는 이 방어가 적용되지 않는다.
- **`SameSite`만으로 CSRF가 끝나지는 않는다.** `Lax`가 비교하는 단위는 origin이 아니라 사이트이므로
  하위 도메인에서 오는 요청에는 cookie가 그대로 붙고, 최상위 화면 전환의 `GET`에도 붙는다.
  그래서 상태를 바꾸는 처리는 `/reset`처럼 `POST`로 두고, `/callback`처럼 `GET`일 수밖에 없다면
  그 요청의 `state` 대조처럼 다른 사이트가 만들어 낼 수 없는 값을 함께 요구해야 한다.
  이 값을 일반화한 것이 CSRF token이다.
- **`HttpOnly`와 `SameSite`는 서로 다른 위협을 막는다.** `HttpOnly`는 페이지에 끼어든 스크립트가
  cookie를 읽는 것을 막고, `SameSite`는 다른 사이트가 cookie를 실은 요청을 보내게 만드는 것을 막는다.
  둘 중 하나만 지정하면 나머지 위협은 그대로 남는다.
- **`Secure`는 실제 배포에서 반드시 켠다.** 이 코드는 `http://localhost`에서 시연하기 위해 꺼 두었다.
  켜 두면 브라우저가 평문 HTTP 요청에는 cookie를 붙이지 않는다.
- **cookie는 HTTP 인증 스킴이 아니다.** 그래서 401 응답에 실어 보낼 `WWW-Authenticate` challenge가
  정의되어 있지 않다. 페이지를 제공하는 앱이라면 보통 로그인 화면으로 이동시키고,
  이 서버는 `curl`로 확인하기 쉽도록 401 응답에 짧은 문구만 담는다.
- **`localStorage`와의 차이는 자동 첨부 여부와 격리 여부다.** `localStorage`에 저장한 값은 페이지의
  스크립트가 직접 읽어서 헤더에 실어야 하고, 페이지에 끼어든 스크립트도 같은 값을 읽을 수 있다.
  대신 브라우저가 자동으로 붙이지 않으므로 CSRF는 발생하지 않는다.
