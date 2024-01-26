from json import dumps
import requests
from urllib.request import Request, urlopen
from webbrowser import open as web_open
from .freee_response import FreeeResponse
from freee_sdk.oauth import OAuth
from freee_sdk.utils import _add_query, create_headers, _get_url, _remove_none_values


class BaseClient:
    BASE_URL = "https://api.freee.co.jp"
    API_URL = ""
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        token: str=None,
        headers: dict=None,
        company_id: int=None,
    ):
        self.request_url = _get_url(base_url=self.BASE_URL, endpoint_url=self.API_URL)
        self.default_params = dict()
        
        self.company_id = company_id
        self.headers = headers or dict()
        
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        
        if token is None:
          self.token = self.get_access_token()
        else:
          self.token = token
        
        if company_id is not None:
          self.default_params["company_id"] = company_id
        
    def api_call(
        self,
        headers: dict=None,
        body: dict=None,
        query: dict=None,
        *,
        method: str,
        endpoint_url: str
        ) -> FreeeResponse:
        api_url = _get_url(base_url=self.request_url, endpoint_url=endpoint_url)
        
        if query is not None:
          query = _remove_none_values(query)
          
        if body is not None:
          body = dumps(_remove_none_values(body), ensure_ascii=False).encode('utf-8')
          
        if headers is None:
          headers = create_headers(self.token)
          
        return self._urllib_api_send(
            method=method,
            headers=headers,
            body=body,
            endpoint_url=api_url
          )

    def _urllib_api_send(
        self,
        headers: dict=None,
        body: dict=None,
        query: dict=None,
        *,
        method: str,
        endpoint_url: str
      ) -> FreeeResponse:
      print(f"url: {endpoint_url}\nbody: {body}\nquery: {query}")
      
      req = requests.request(method=method, url=endpoint_url, headers=headers, data=body, params=query)
      req.raise_for_status()
      return FreeeResponse(
        client=endpoint_url,
        http_verb=method,
        data=req
      ).varidate()

    def get_access_token(self):
        oauth2_session = OAuth(
          client_id=self.client_id,
          client_secret=self.client_secret,
          redirect_uri=self.redirect_uri
        )
        session = oauth2_session.generate_auth_token_url()
        
        web_open(session["authorization_url"], new=0, autoraise=True)
        
        code = input('認可コードを入力: ')
        
        token = oauth2_session.generate_access_token(
        oauth_session=session["session"],
        authorize_code=code
        )
        print(token)
        return token


if __name__ == "__main__":
    base_client = BaseClient()
    print(base_client.request_url)
