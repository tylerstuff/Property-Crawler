import json
from typing import Optional
from urllib.parse import urlencode
import requests
from propertycrawler.config import (
    TOKEN_URL, SEARCH_CONFIG,
    DISTRICT_URL, PUBLICPROPERTY_URL, PRIVATEPROPERTY_URL,
    PUBLICRENT_URL, PRIVATERENT_URL
)


def get_token(proxy: Optional[dict] = None) -> str:
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
    district_num: int,
    lower_bound_date: str,
    upper_bound_date: str,
    lower_bound_price: int = 0,
    upper_bound_price: int = 20000000,
    proxy: Optional[str] = None
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
    if proxy:
        proxies = {
            "HTTP": proxy,
            "HTTPS": proxy
        }
    else:
        proxies = None
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


def get_property_transaction(
    HDB_flag: bool,
    latitude: str,
    longitude: str,
    block: str = None,
    proxy: Optional[str] = None
) -> dict:
    """
    Gets property transaction contract information
    Args:
        proxy: proxy ip and port (e.g. 0.0.0.0:80)
        HDB_flag: True if HDB False if else
        latitude: Latitude value
        longitude: Longitude value
        block: Block value if it exists
    """
    if proxy:
        proxies = {
            "HTTP": proxy,
            "HTTPS": proxy
        }
    else:
        proxies = None
    token = get_token(proxy=proxies)
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'token': token
    }
    if HDB_flag:
        base_url = PUBLICPROPERTY_URL
        params = {
            **params,
            'block': block
        }
    else:
        base_url = PRIVATEPROPERTY_URL
    url = "{}?{}".format(base_url, urlencode(params))
    response = requests.get(url, proxies=proxies)
    data = json.loads(response.text)
    return data


def get_property_rent(
    HDB_flag: bool,
    latitude: str,
    longitude: str,
    block: str = None,
    proxy: Optional[str] = None
) -> dict:
    """
    Gets property rent contract information
    Args:
        proxy: proxy ip and port (e.g. 0.0.0.0:80)
        HDB_flag: True if HDB False if else
        latitude: Latitude value
        longitude: Longitude value
        block: Block value if it exists
    """
    if proxy:
        proxies = {
            "HTTP": proxy,
            "HTTPS": proxy
        }
    else:
        proxies = None
    token = get_token(proxy=proxies)
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'token': token
    }
    if HDB_flag:
        base_url = PUBLICRENT_URL
        params = {
            **params,
            'block': block
        }
    else:
        base_url = PRIVATERENT_URL
    url = "{}?{}".format(base_url, urlencode(params))
    response = requests.get(url, proxies=proxies)
    data = json.loads(response.text)
    return data
