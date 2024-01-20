from urllib.parse import urljoin

class BaseClient:
    BASE_URL = "https://api.freee.co.jp"
    API_URL = ""
    def __init__(
        self
    ):
        self.access_token= ""
        self.request_url = urljoin(base=self.BASE_URL, url=self.API_URL)


if __name__ == "__main__":
    base_client = BaseClient()
    print(base_client.request_url)
