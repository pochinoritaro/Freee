import freee_sdk.errors as err
from requests import request

class FreeeResponse:
	def __init__(
			self,
			*,
			client,
			http_verb: str,
			data: request
		) -> None:
			self._client = client
			self.http_verb = http_verb
			self.api_url = data.url
			self.data = data.json()
			self.status = data.status_code
			self.error_format = f"url: {self.api_url}\nstatus: {self.status}\ndata: {self.data}"
	
	def __getitem__(self, item):
		return self.data[item]
	
	def __str__(self) -> str:
		return f"{self.data}"
	
	def items(self):
		return self.data.items()
	
	def varidate(self):
		if self.status == 200:
			return self
		
		elif self.status == 400:
			raise err.UnAuthorizedError(self.error_format)

		elif self.status == 401:
			raise err.AccessDeniedError(self.error_format)

		elif self.status == 403:
			raise err.ForbiddenError(self.error_format)
		
		elif self.status == 404:
			raise err.NotFoundError(self.error_format)

		elif self.status == 503:
			raise err.InternalServerError(self.error_format)
