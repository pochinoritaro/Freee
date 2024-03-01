# Freee
FreeeのAPIをPythonから扱えるようにするライブラリ
<br>Vertion: Python 3.12.1

<br>外部ライブラリ
| ライブラリ名       | バージョン | 依存先            | ライセンス | 
| ------------------ | ---------- | ----------------- | ---------- | 
| requests-oauthlib  | 1.3.1      |                   | ISC        | 
| oauthlib           | 3.2.2      | requests-oauthlib | BSD        | 
| requests           | 2.31.0     | requests-oauthlib | Apache 2.0 | 
| certifi            | 2023.11.17 | requests          | MPL-2.0    | 
| charset-normalizer | 3.3.2      | requests          | MIT        | 
| idna               | 3.6        | requests          |            | 
| urllib3            | 2.1.0      | requests          |            | 
<br>

## 人事労務(HumanResource)
[人事労務リファレンス](https://developer.freee.co.jp/reference/hr/reference)
<br>本ライブラリで提供されている各種メソッドについては上記リファレンスを参照してください。
<br>
### サンプル
【使用例】
```
from human_resource import HumanResourse

hr = HumanResourse(
    client_id=クライアントID,
    client_secret=シークレットID,
    redirect_uri=リダイレクト先
    )

# アクセストークンを登録
hr.access_token = アクセストークン

# ログイン中のユーザが所属している事業所情報を取得
me = hr.get_users_me()
print(me)

# 事業所IDを登録
human_resourse.company_id = me["companies"][0]["id"]
```
---
【使用例(FastAPI連携)】
```
from urllib.parse import parse_qs
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from Freee import HumanResourse
from Freee.freee_sdk.errors import UnAuthorizedError

HOST = "127.0.0.1"
PORT = 8000

api = FastAPI()
hr = HumanResourse(
    client_id=クライアントID,
    client_secret=シークレットID,
    redirect_uri=リダイレクト先
    )


# 認証URLにコールバック
@api.get("/")
def freee_redirect():
    url = hr.oauth.get_auth_url()
    return RedirectResponse(url=url)


# コールバック
@api.get("/freee/callback")
def freee_callback(request: Request):
    # stateを取得
    state = parse_qs(str(request.query_params))["code"][0]
    
    # アクセストークンを取得
    try:
        response = hr.oauth.get_access_token(state=state)
        hr.access_token, hr.refresh_token, hr.token_create_at = response["access_token"], response["refresh_token"], response["expires_in"]
        return "アクセストークンを生成しました。"
    
    except UnAuthorizedError as e:
        return "アクセストークンの生成に失敗しました。"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="app:api", host=HOST, port=PORT, reload=True)
```
