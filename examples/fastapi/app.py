from urllib.parse import parse_qs
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from Freee import HumanResourse
from Freee.freee_sdk.errors import UnAuthorizedError

HOST = "127.0.0.1"
PORT = 8000

api = FastAPI()
hr = HumanResourse(
    client_id="client_id",
    client_secret="client_secret",
    redirect_uri="redirect_uri"
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
