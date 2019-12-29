import json
import mock
from random import choice
from randproxy import proxy as rp
from propertycrawler import prop_crawl

class mock_token_request:
    def __init__(self, text):
        self.text = text

class mock_district_request:
    def __init__(self, text):
        self.text = text

def mock_token_response(*args, **kwargs):
    with open("tests/docs/mock_token_response.json", "r") as fp:
        json_content = fp.read()
    return mock_token_request(json_content)

def mock_token_payload(*args, **kwargs):
    return ""

def mock_district_payload(*args, **kwargs):
    with open("tests/docs/mock_district_response.json", "r") as fp:
        json_content = fp.read()
    return mock_district_request(json_content)

@mock.patch("propertycrawler.prop_crawl.requests.get", mock_token_response)
def test_get_token():
    with open("tests/docs/mock_token.txt", "r") as fp:
        expected = fp.read()
    access_token = prop_crawl.get_token("")
    assert access_token == expected

@mock.patch("propertycrawler.prop_crawl.get_token", mock_token_payload)
@mock.patch("propertycrawler.prop_crawl.requests.get", mock_district_payload)
def test_get_district():
    proxy = "0.0.0.0:80"
    response = prop_crawl.get_district(
        proxy=proxy,
        district_num=1,
        lower_bound_date='20171201',
        upper_bound_date='20191229'
    )
    with open("tests/docs/mock_district_response.json", "r") as fp:
        expected = json.load(fp)
    assert response == expected