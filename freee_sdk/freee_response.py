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
			print(self.status)
			print(self.data)
	
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
			raise err.UnAuthorizedError

		elif self.status == 401:
			raise err.AccessDeniedError

		elif self.status == 403:
			raise err.ForbiddenError
		
		elif self.status == 404:
			raise err.NotFoundError

		elif self.status == 503:
			raise err.InternalServerError
