from json import dumps
import requests
from .freee_response import FreeeResponse
from Freee.freee_sdk.errors import UnAuthorizedError
from Freee.freee_sdk.utils import create_headers, _get_url, _remove_none_values
from Freee.freee_sdk.oauth import OAuth

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
        
        self.oauth = OAuth(
            client_id = client_id,
            client_secret = client_secret,
            redirect_uri = redirect_uri
        )
        
        if company_id is not None:
            self.default_params["company_id"] = company_id


    @property
    def access_token(self) -> str:
        return self.__access_token


    @access_token.setter
    def access_token(self, access_token: str):
        self.__access_token = access_token


    @property
    def refresh_token(self) -> str:
        return self.__refresh_token


    @refresh_token.setter
    def refresh_token(self, refresh_token: str):
        self.__refresh_token = refresh_token


    @property
    def token_create_at(self) -> str:
        return self.__token_create_at


    @token_create_at.setter
    def token_create_at(self, token_create_at: str):
        self.__token_create_at = token_create_at


    @property
    def company_id(self) -> str:
        return self.__company_id


    @company_id.setter
    def company_id(self, company_id: int):
        self.__company_id = company_id
        self.default_params["company_id"] = company_id


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
            case "GET"|"DELETE":
                query = self.default_params|_remove_none_values(query) if query is not None else self.default_params
        
            case "POST"|"PUT":
                body = self.default_params|_remove_none_values(body) if body is not None else dict()
                body = dumps(_remove_none_values(body), ensure_ascii=False).encode('utf-8')
        
            case _:
                raise TypeError

        if body is not None:
            body = dumps(_remove_none_values(body), ensure_ascii=False).encode('utf-8')

        if headers is None:
            headers = create_headers(self.access_token)

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
        print(f"url: {endpoint_url}")
        
        req = requests.request(
            method=method,
            url=endpoint_url,
            headers=headers,
            data=body,
            params=query
        )
        return FreeeResponse(
            client=endpoint_url,
            http_verb=method,
            data=req
        ).validate()


if __name__ == "__main__":
    base_client = BaseClient()
    print(base_client.request_url)
