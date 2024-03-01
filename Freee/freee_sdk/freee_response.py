import Freee.freee_sdk.errors as err
from requests import Response

class FreeeResponse:
    """Freeeレスポンス定義クラス
    APIのレスポンスを受け取り、必要に応じてエラーを発生させる。
    """
    def __init__(
            self,
            *,
            client,
            http_verb: str,
            data: Response
        ) -> None:
            self._client = client
            self.http_verb = http_verb
            self.api_url = data.url
            self.data = data.json()
            self.status = data.status_code
    
    def __getitem__(self, item: str) -> any:
        return self.data[item]
    
    def __str__(self) -> str:
        return f"{self.data}"
    
    def items(self):
        return self.data.items()
    
    def __error_content(self, error_body: dict) -> str:
        """エラーレスポンスの整形
        エラーレスポンスをフォーマットに整形して返却する

        Args:
            error_body (dict): エラーレスポンス

        Returns:
            str: フォーマットに沿った文字列
        """
        print(self.data)
        print(error_body)
        message = error_body["errors"][0]["messages"][0] if error_body.get("errors") is not None else error_body["message"]
        code = error_body["errors"][0]["code"][0] if error_body.get("errors") is not None else error_body["code"]
        return f"{message}({code}[{self.status}])"
        
    
    def validate(self):
        """_summary_

        Raises:
            err.UnAuthorizedError: _description_
            err.AccessDeniedError: _description_
            err.ForbiddenError: _description_
            err.NotFoundError: _description_
            err.TooManyRequestsError: _description_
            err.InternalServerError: _description_

        Returns:
            objrct: Freeeレスポンス
        """
        if self.status == 200:
            return self
        
        elif self.status == 400:
            raise err.BadRequestError(self.__error_content(self.data))

        elif self.status == 401:
            raise err.AccessDeniedError(self.__error_content(self.data))

        elif self.status == 403:
            raise err.ForbiddenError(self.__error_content(self.data))
        
        elif self.status == 404:
            raise err.NotFoundError(self.__error_content(self.data))

        elif self.status == 429:
            raise err.TooManyRequestsError(self.__error_content(self.data))

        elif self.status == 503:
            raise err.InternalServerError(self.__error_content(self.data))
