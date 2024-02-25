from json import dumps
import requests
from .freee_response import FreeeResponse
from freee_sdk.errors import UnAuthorizedError
from freee_sdk.utils import _add_query, create_headers, _get_url, _remove_none_values
from freee_sdk.oauth import OAuth

class BaseClient:
    BASE_URL = "https://api.freee.co.jp"
    API_URL = ""
    def __init__(
        self,
        access_token: str=None,
        refresh_token: str=None,
        token_create_at: int=None,
        headers: dict=None,
        company_id: int=None,
        *,
        client_id: str=None,
        client_secret: str=None,
        redirect_uri: str=None
    ):
        self.request_url = _get_url(base_url=self.BASE_URL, endpoint_url=self.API_URL)
        self.default_params = dict()
        
        self.headers = headers or dict()
        
        self.__access_token = access_token
        self.__refresh_token = refresh_token
        self.__token_create_at = token_create_at
        self.__company_id = company_id

        
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        
        self.oauth = OAuth
        
        if company_id is not None:
            self.default_params["company_id"] = company_id
    
    @property
    def access_token(self):
        return self.__access_token

    @access_token.setter
    def access_token(self, access_token):
        self.__access_token = access_token

    @property
    def refresh_token(self):
        return self.__refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        self.__refresh_token = refresh_token

    @property
    def token_create_at(self):
        return self.__token_create_at

    @token_create_at.setter
    def token_create_at(self, token_create_at):
        self.__token_create_at = token_create_at

    @property
    def company_id(self):
        return self.__company_id

    @company_id.setter
    def company_id(self, company_id):
        self.__company_id = company_id
        self.default_params["company_id"] = company_id

    # Oauth関係
    def get_auth_url(self) -> str|None:
        """認可コードの取得
        
        APIの認可用URLを取得します。

        Returns:
            str|None: 認可用URLを返却する。
        """
        authorization_url = self.oauth.get_auth_url(
            client_id=self.client_id,
            redirect_uri=self.redirect_uri
            )
        return authorization_url

    def get_access_token(
        self,
        state: str
        ) -> dict|None:
        """アクセストークンの取得
        
        APIのアクセストークンを取得します。

        Args:
            state (str): 認可後に返却される一意のcode。

        Returns:
            dict|None: アクセストークン、リフレッシュトークンなどを含む辞書を返却。
        """
        token_response = self.oauth.get_access_token(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
            state=state
        )
        match token_response.status_code:
            case 200:
                response = token_response.json()
                #TODO アクセストークンとリフレッシュトークンのテーブルを分けてトークンローテに対応させる
                
                #TODO 再考の余地おおあり(クラス化)2024/02/08
                self.access_token = response["access_token"]
                self.refresh_token = response["refresh_token"]
                self.token_create_at = response["created_at"]
                
                return token_response
            
            case _:
                raise UnAuthorizedError

    
    # APIコール関係
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
        
        match method:
            case "GET":
                query = self.default_params|_remove_none_values(query)
        
        """if query is not None:
        query = dumps(_remove_none_values(query), ensure_ascii=False)"""

        if body is not None:
            body = dumps(_remove_none_values(body), ensure_ascii=False).encode('utf-8')

        if headers is None:
            headers = create_headers(self.access_token)
        
        print(headers)
        
        return self._urllib_api_send(
            method=method,
            headers=headers,
            body=body,
            query=query,
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
        print(f"url: {endpoint_url}\nheader: {headers}\nbody: {body}\nquery: {query}[{type(query)}]")
        print()
        
        req = requests.request(
        method=method,
        url=endpoint_url,
        headers=headers,
        data=body,
        params=query  # 修正点: dictをparamsに渡す
        )
        
        req.raise_for_status()
        
        return FreeeResponse(
        client=endpoint_url,
        http_verb=method,
        data=req
        ).varidate()


if __name__ == "__main__":
    base_client = BaseClient()
    print(base_client.request_url)
