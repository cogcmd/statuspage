import requests

STATUSPAGE_V1_API = "https://api.statuspage.io/v1"

def api_get(url, token, headers={}):
    url = "%s/%s" % (STATUSPAGE_V1_API, url)
    headers["Authorization"] = "OAuth %s" % (token)
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r

def api_post(url, token, headers={}, body=""):
    url = "%s/%s" % (STATUSPAGE_V1_API, url)
    headers["Authorization"] = "OAuth %s" % (token)
    return requests.post(url, headers=headers, data=body)

def api_patch(url, token, headers={}, body=""):
    url = "%s/%s" % (STATUSPAGE_V1_API, url)
    headers["Authorization"] = "OAuth %s" % (token)
    return requests.patch(url, headers=headers, data=body)
