from http_client import *
from constants import *

def get_cards_url():
    resp = post_request(url=get_cards_url(), data=standard_body(), headers=get_headers())
    return resp
    assert resp.status_code == 200

def get_categories_url():
    resp = post_request(url=get_categories_url(), data=standard_body(), headers=get_headers())
    return resp

def get_getblacklist_url():
    resp = post_request(url=get_getblacklist_url(), data=standard_body(), headers=get_headers())
    print(resp.text)
    text_data = default_json_to_dict(resp.text)
    print(text_data)
    print(resp.status_code)
    t = text_data['GetBlackListResult']
    print(t)
    t2 = t['Data']
    print(t2)
    return resp

def get_appversions_url():
    resp = post_request(url=get_appversions_url(), data=standard_body(), headers=get_headers())
    return resp

def get_foxtrotcard_url():
    resp = post_request(url=get_foxtrotcard_url(), data=standard_body(), headers=get_headers())
    return resp

def get_offers_url():
    resp = post_request(url=get_offers_url(), data=standard_body(), headers=get_headers())
    return resp

def get_getretailers():
    resp = post_request(url=get_getretailers(), data=standard_body(), headers=get_headers())
    return resp