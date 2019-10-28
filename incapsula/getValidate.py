#!/usr/bin/env python3

"""Validates if a site is fully-configured

 site_id -- numerical site id to retrive
 api_id -- API ID to use (Default: enviroment variable)
 api_key -- API KEY to use (Default: enviroment variable)
 """
 
from .com_error import errorProcess
from .sendRequest import ApiCredentials, ApiUrl, makeRequest

api_creds = ApiCredentials()
api_endpoint = ApiUrl.api_endpoint

def getValidation(site_id, verify_ssl=True):
    url = api_endpoint + 'prov/v1/sites/status'
    try:
        payload = {
            'api_id': api_creds.api_id,
            'api_key': api_creds.api_key,
            'site_id':site_id,
            'tests':'domain_validation'
        }
        r = makeRequest(url, payload, verify_ssl)
        return r.text
    except Exception as error:
        return errorProcess(error)