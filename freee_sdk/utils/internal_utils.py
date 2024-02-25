from json import dumps, loads
from urllib.parse import urljoin, urlencode
from urllib.request import HTTPError, Request, urlopen

def _remove_none_values(d: dict) -> dict:
    if d is dict:
        return {k: v for k, v in d.items() if v is not  None}
    else:
        return dict()

def _get_url(base_url: str, endpoint_url: str) -> str:
    return urljoin(base_url, endpoint_url)

def _add_query(
        base_url: str,
        query_param: dict
    ) -> str:
        return "{}?{}".format(base_url, urlencode(query_param))

def create_headers(access_token: dict) -> dict:
    return {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
        "FREEE-VERSION": "2022-02-01"
        }

def request_urllib(body: dict=None, query: dict=None, *, headers: dict, url: str):
    url = _add_query(base_url=url, query_param=query) if query is not None else url
    body = dumps(body).encode() if body is not None else body
    request = Request(headers=headers, url=url, data=body)
    
    try:
        with urlopen(request) as response:
            return dict(
                status_code=response.getcode(),
                http_verb=vars(response)["_method"],
                url=vars(response)["url"],
                data=loads(response.read().decode("utf-8"))
            )
    except HTTPError as e:
        return dict(
            status_code=e.code,
            http_verb=None,
            url=vars(e)["url"],
            data=None
        )

if __name__ == "__main__":
    from configparser import ConfigParser

    config = ConfigParser()
    config.read("./doc/.ini")

    me = request_urllib(header=create_headers(config["freee"]["ACCESS_TOKEN"]), url="https://api.freee.co.jp/hr/api/v1/users/me")
    print(me)