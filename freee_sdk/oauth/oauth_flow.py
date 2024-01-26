import requests
from requests_oauthlib import OAuth2Session
from json import dumps
from urllib.parse import urljoin

class OAuth:
    AUTH_URL_BASE = "https://accounts.secure.freee.co.jp/"
    AUTH_TOKEN = "/public_api/authorize"
    ACCESS_TOKEN = "/public_api/token"
    AUTH_TOKEN_URL = urljoin(AUTH_URL_BASE, AUTH_TOKEN)
    ACCESS_TOKEN_URL = urljoin(AUTH_URL_BASE, ACCESS_TOKEN)

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        ) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def generate_auth_token_url(self) -> dict:
        oauth_session = OAuth2Session(
            client_id=self.client_id,
            redirect_uri=self.redirect_uri
        )
        authorization_url, state = oauth_session.authorization_url(self.AUTH_TOKEN_URL)
        return {
            "session": oauth_session,
            "authorization_url": authorization_url,
            "code": state
                }

    def generate_access_token(
        self,
        oauth_session: OAuth2Session.authorization_url,
        authorize_code: str,
    ) -> dict:
        return oauth_session.fetch_token(
            self.ACCESS_TOKEN_URL,
            client_secret=self.client_secret,
            code=authorize_code
        )

if __name__ == "__main__":
    from webbrowser import open as web_open
    import configparser
    config = configparser.ConfigParser()

    #設定ファイル読み込み
    config.read("./doc/.ini")
    CLIENT_ID = config["freee"]["CLIENT_ID"]
    CLIENT_SECRET = config["freee"]["CLIENT_SECRET"]
    REDIRECT_URI = config["freee"]["REDIRECT_URI"]

    oauth2_session = OAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI
    )
    
    session = oauth2_session.generate_auth_token_url()
    
    web_open(session["authorization_url"], new=0, autoraise=True)
    code = input('認可コードを入力: ')
    
    token = oauth2_session.generate_access_token(
        oauth_sesion=session["session"],
        authorize_code=code
    )

    url = "https://api.freee.co.jp/hr/api/v1/users/me"
    token = token["access_token"]
    
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}",
        "FREEE-VERSION": "2022-02-01"
    }

    req = requests.get(url=url, headers=headers)
    print(req.status_code)
    print(req.json())
