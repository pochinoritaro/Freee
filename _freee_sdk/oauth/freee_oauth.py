import requests
from requests_oauthlib import OAuth2Session
from json import dumps
from urllib.parse import urljoin
from webbrowser import open as web_open

CLIENT_ID = "2612398b54dd2a73d45b51c2fdf3b12360fcbb40d346d2f0bb04c34e7bb383ef"
CLIENT_SECRET = "f2b4272865b6fa0685f8ed0331bc9d2bd7e06a4c85eeb8a4d685bc4ab8bbd07b"
REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"

AUTH_URL_BASE = "https://accounts.secure.freee.co.jp/"
AUTH_TOKEN = "/public_api/authorize"
ACCESS_TOKEN = "/public_api/token"

AUTH_TOKEN_URL = urljoin(AUTH_URL_BASE, AUTH_TOKEN)
ACCESS_TOKEN_URL = urljoin(AUTH_URL_BASE, ACCESS_TOKEN)

oauth_session = OAuth2Session(
	client_id=CLIENT_ID,
	redirect_uri=REDIRECT_URI
)

authorization_url, state = oauth_session.authorization_url(AUTH_TOKEN_URL)
web_open(authorization_url, new=0, autoraise=True)
code = input('認可コードを入力: ')

access_token = oauth_session.fetch_token(
	ACCESS_TOKEN_URL,
	client_secret=CLIENT_SECRET,
	code=code,
)

url = "https://api.freee.co.jp/hr/api/v1/users/me"
token = access_token["access_token"]
print(f"Bearer {token}")
headers = {
	"accept": "application/json",
	"Authorization": f"Bearer {token}",
	"FREEE-VERSION": "2022-02-01"
}

req = requests.get(url=url, headers=headers)
print(req.status_code)
print(req.json())
