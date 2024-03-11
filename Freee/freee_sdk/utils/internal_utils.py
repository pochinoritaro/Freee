from json import dumps
from urllib.parse import urljoin, urlencode

def _remove_none_values(d: dict) -> dict:
    if isinstance(d, dict):
        return {k: dumps(v) for k, v in d.items() if v is not None}
    else:
        return {}


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
