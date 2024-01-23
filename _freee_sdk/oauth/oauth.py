import requests
from requests_oauthlib import OAuth2Session
from json import dumps
from urllib.parse import urljoin

AUTH_URL_BASE = "https://accounts.secure.freee.co.jp/"
AUTH_TOKEN = "/public_api/authorize"
ACCESS_TOKEN = "/public_api/token"

AUTH_TOKEN_URL = urljoin(AUTH_URL_BASE, AUTH_TOKEN)
ACCESS_TOKEN_URL = urljoin(AUTH_URL_BASE, ACCESS_TOKEN)


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

    def generate_auth_token_url(self) -> OAuth2Session:
        oauth_session = OAuth2Session(
            client_id=self.client_id, 
            redirect_uri=self.redirect_uri
        )
        authorization_url, state = oauth_session.authorization_url(AUTH_TOKEN_URL)
        return {
            "session": oauth_session,
            "authorization_url": authorization_url,
            "code": state
                }

    def generate_access_token(
        self,
        oauth_sesion: OAuth2Session.authorization_url,
        authorize_code: str,
    ):
        return oauth_sesion.fetch_token(
            self.ACCESS_TOKEN_URL,
            client_secret=self.client_secret,
            code=authorize_code
        )

if __name__ == "__main__":
    from webbrowser import open as web_open
    
    CLIENT_ID = "2612398b54dd2a73d45b51c2fdf3b12360fcbb40d346d2f0bb04c34e7bb383ef"
    CLIENT_SECRET = "f2b4272865b6fa0685f8ed0331bc9d2bd7e06a4c85eeb8a4d685bc4ab8bbd07b"
    REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"

    oauth2_session = OAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI
    )
    
    session = oauth2_session.generate_auth_token_url()
    
    web_open(session["authorization_url"], new=0, autoraise=True)
    code = input('認可コードを入力: ')
    
    token = oauth2_session.generate_access_token(
        oauth_sesion=session["session"],
        authorize_code=code
    )

    print(token)
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