TOKEN_URL = 'https://developers.onemap.sg/publicapi/publicsessionid'

DISTRICT_URL = 'https://developers.onemap.sg/publicapi/propsvc/retrieve_prop' \
    'erty_locations_within_district'

PRIVATEPROPERTY_URL = 'https://developers.onemap.sg/publicapi/propsvc/getPPT' \
    'ransactionRecordsByLatLon'
PRIVATERENT_URL = 'https://developers.onemap.sg/publicapi/propsvc/getPPRenta' \
    'lRecordsByLatLon'
PUBLICPROPERTY_URL = 'https://developers.onemap.sg/publicapi/propsvc/getHDBR' \
    'esaleByBuildingBlock'
PUBLICRENT_URL = 'https://developers.onemap.sg/publicapi/propsvc/getHDBRenta' \
    'lByBuildingBlock'

POSTAL_DISTRICTS = range(1, 28)

SEARCH_CONFIG = {
    'apartment': 'true',
    'condo': 'true',
    'executive_condo': 'true',
    'executive_hdb': 'true',
    'five_room_hdb': 'true',
    'four_room_hdb': 'true',
    'landed': 'true',
    'multi_gen_hdb': 'true',
    'one_room_hdb': 'true',
    'three_room_hdb': 'true',
    'two_room_hdb': 'true'
}
