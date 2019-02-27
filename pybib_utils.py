# Modified from https://github.com/jgilchrist/pybib/blob/master/pybib/utils.py
# commit: da2130d281bb02e930728ed7c1d0c1dffa747ee0

import requests

GET_URL = "http://dx.doi.org/{}"


def get_bibtex(doi):
    url = GET_URL.format(doi)
    headers = {'Accept': 'application/x-bibtex; charset=utf-8'}

    r = requests.get(url, headers=headers)
    r.encoding = "utf-8"

    if r.status_code == 200:
        entry = r.text.strip()
        return entry
    elif r.status_code == 404:
        print("DOI {} not found".format(doi))
    else:
        print("Unhandled http response code: {}".format(r.status_code))

