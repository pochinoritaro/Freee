from urllib.parse import urljoin

class BaseClient:
    BASE_URL = "https://api.freee.co.jp"
    API_URL = ""
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        redirect_uri: str
    ):
        self.access_token = ""
        self.request_url = urljoin(base=self.BASE_URL, url=self.API_URL)

    def api_call(self):
        pass

    def generate_access_token(self):
        pass

if __name__ == "__main__":
    base_client = BaseClient()
    print(base_client.request_url)
