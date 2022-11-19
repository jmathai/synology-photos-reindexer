#! /usr/bin/env python3
import os
import requests

def call_api(api, method, version, **kwargs):
    hostname = os.environ['SYNO_HOSTNAME']

    url = 'https://{}:5001/webapi/query.cgi'.format(hostname)
    # https://stackoverflow.com/a/66464593
    data = kwargs
    data['api'] = api
    data['method'] = method
    data['version'] = version
    return requests.post(url, verify=False, data=data)

def login():
    username = os.environ['SYNO_USERNAME']
    password = os.environ['SYNO_PASSWORD']

    res_login = call_api('SYNO.API.Auth', 'login', '3', account=username, passwd=password)
    res_login_json = res_login.json()
    if('data' not in res_login_json):
        exit('Login failed')

    return res_login_json['data']['sid']

def reindex(sid):
    res_reindex = call_api('SYNO.Foto.Index', 'reindex', '1', _sid=sid)
    res_reindex_json = res_reindex.json()
    if('success' not in res_reindex_json):
        exit('Reindex failed')

    return True

def logout():
    res_logout = call_api('SYNO.API.Auth', 'logout', '3')
    res_logout_json = res_logout.json()
    if('success' not in res_logout_json):
        print('Logout failed')



if(__name__ == '__main__'):
    if('SYNO_HOSTNAME' not in os.environ):
        exit('Synology hostname (SYNO_HOSTNAME) not in environment')
    if('SYNO_USERNAME' not in os.environ):
        exit('Synology username (SYNO_USERNAME) not in environment')
    if('SYNO_PASSWORD' not in os.environ):
        exit('Synology password (SYNO_PASSWORD) not in environment')

    login_sid = login()
    res_reindex = reindex(login_sid)
    logout()
    print('Reindexed successfully')
