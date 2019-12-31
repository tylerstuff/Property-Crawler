import json
import mock
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


def mock_property_transaction_payload_public(*args, **kwargs):
    with open(
        "tests/docs/mock_public_property_transaction_response.json", "r"
    ) as fp:
        json_content = fp.read()
    return mock_district_request(json_content)


def mock_property_transaction_payload_private(*args, **kwargs):
    with open(
        "tests/docs/mock_private_property_transaction_response.json", "r"
    ) as fp:
        json_content = fp.read()
    return mock_district_request(json_content)


def mock_property_rent_payload_public(*args, **kwargs):
    with open(
        "tests/docs/mock_public_property_rent_response.json", "r"
    ) as fp:
        json_content = fp.read()
    return mock_district_request(json_content)


def mock_property_rent_payload_private(*args, **kwargs):
    with open(
        "tests/docs/mock_private_property_rent_response.json", "r"
    ) as fp:
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


@mock.patch("propertycrawler.prop_crawl.get_token", mock_token_payload)
@mock.patch(
    "propertycrawler.prop_crawl.requests.get",
    mock_property_transaction_payload_public
)
def test_get_property_transaction_public():
    response = prop_crawl.get_property_transaction(
        HDB_flag=True,
        latitude='1.28485860857395',
        longitude='103.842578771054',
        block='32'
    )
    with open(
        'tests/docs/mock_public_property_transaction_response.json', 'r'
    ) as fp:
        expected = json.load(fp)
    assert response == expected


@mock.patch("propertycrawler.prop_crawl.get_token", mock_token_payload)
@mock.patch(
    "propertycrawler.prop_crawl.requests.get",
    mock_property_transaction_payload_private
)
def test_get_property_transaction_private():
    response = prop_crawl.get_property_transaction(
        HDB_flag=False,
        latitude='1.2803150833928285',
        longitude='103.85218440030791'
    )
    with open(
        'tests/docs/mock_private_property_transaction_response.json', 'r'
    ) as fp:
        expected = json.load(fp)
    assert response == expected


@mock.patch("propertycrawler.prop_crawl.get_token", mock_token_payload)
@mock.patch(
    "propertycrawler.prop_crawl.requests.get",
    mock_property_rent_payload_public
)
def test_get_property_rent_public():
    response = prop_crawl.get_property_rent(
        HDB_flag=True,
        latitude='1.28180062242259',
        longitude='103.842908159495',
        block='4'
    )
    with open(
        'tests/docs/mock_public_property_rent_response.json', 'r'
    ) as fp:
        expected = json.load(fp)
    assert response == expected


@mock.patch("propertycrawler.prop_crawl.get_token", mock_token_payload)
@mock.patch(
    "propertycrawler.prop_crawl.requests.get",
    mock_property_rent_payload_private
)
def test_get_property_rent_private():
    response = prop_crawl.get_property_rent(
        HDB_flag=False,
        latitude='1.2794616640723235',
        longitude='103.8472833296039'
    )
    with open(
        'tests/docs/mock_private_property_rent_response.json', 'r'
    ) as fp:
        expected = json.load(fp)
    assert response == expected
