import json
from urllib.parse import urlencode
import requests
from propertycrawler.config import (
    TOKEN_URL, POSTAL_DISTRICTS, SEARCH_CONFIG,
    DISTRICT_URL
)

def get_token(proxy: dict) -> str:
    """
    Gets public API Token
    Args:
        proxy: proxy ip and port (e.g. 0.0.0.0:80)
    Returns:
        str: Token JSON
    """
    response = requests.get(TOKEN_URL, proxies=proxy)
    return json.loads(response.text)["access_token"]


def get_district(
    proxy: str,
    district_num: int,
    lower_bound_date: str,
    upper_bound_date: str,
    lower_bound_price: int = 0,
    upper_bound_price: int = 20000000
) -> dict:
    """
    Gets properties available in a given district
    Args:
        proxy: proxy ip and port (e.g. 0.0.0.0:80)
        district_num: number between 1 and 28
        lower_bound_date: YYYYMMDD format
        upper_bound_date: YYYYMMDD format
        lower_bound_price: lower bound search limit
        upper_bound_price: upper bound search limit
    Returns:
        dict: Payload response (with all the data)
    """
    proxies = {
        "HTTP": proxy,
        "HTTPS": proxy
    }
    token = get_token(proxy=proxies)
    params = {
        **SEARCH_CONFIG,
        'district': district_num,
        'lower_bound_date': lower_bound_date,
        'upper_bound_date': upper_bound_date,
        'lower_bound_price': lower_bound_price,
        'upper_bound_price': upper_bound_price,
        'token': token
    }
    url = "{}?{}".format(DISTRICT_URL, urlencode(params))
    response = requests.get(url, proxies=proxies)
    data = json.loads(response.text)
    return data