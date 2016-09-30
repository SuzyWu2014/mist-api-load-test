from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

import json
import re
import requests
import urllib

def getLocationIds(json_data):
    items = json_data["data"]
    return [item["id"] for item in items]


def _getAccessToken(client_id, client_secret, token_url):
    client    = BackendApplicationClient(client_id=client_id)
    oauth     = OAuth2Session(client=client)
    token_res = oauth.fetch_token(token_url=token_url, client_id=client_id, client_secret=client_secret)
    return token_res

def getResponse(token, params, api_url):
    query_params = urllib.urlencode(params)
    api_call_url = api_url + "?" + query_params
    return requests.get(api_call_url, headers={'Authorization': token})


def generate_config():
    config_file = open("configuration.json")
    config_data = json.load(config_file)

    base_url  = config_data["hostname"] + config_data["version"] + config_data["api"]
    token_url = base_url + config_data["token_endpoint"]
    token_res = _getAccessToken(config_data["client_id"], config_data["client_secret"], token_url)
    token     = re.sub("Token", "", token_res["token_type"]) + " " + token_res["access_token"]
    params   = {"page[size]": "280"}
    response = getResponse(token, params, base_url)
    locations_ids = getLocationIds(response.json())
    with open('config.py', 'w') as f:
        f.write('TOKEN = "%s"\n' % token)
        f.write('LOCATION_IDS = set(%r)' % locations_ids)


generate_config()
