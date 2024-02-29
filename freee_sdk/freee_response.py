import freee_sdk.errors as err
from requests import request, Response

class FreeeResponse:
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
    
    def __getitem__(self, item):
        return self.data[item]
    
    def __str__(self) -> str:
        return f"{self.data}"
    
    def items(self):
        return self.data.items()
    
    @staticmethod
    def __error_content(error_body: dict) -> str:
        e = error_body["errors"][0]
        return f"{e["messages"][0]}({e["type"]}[{error_body["status_code"]}])"
    
    def validate(self):
        if self.status == 200:
            return self
        
        elif self.status == 400:
            raise err.UnAuthorizedError(self.__error_content(self.data))

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
