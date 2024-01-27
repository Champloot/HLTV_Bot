import json
auxiliary_data = open('../auxiliary_data.json', 'rw')
info_from_mainPage = auxiliary_dat
import datetime

import requests
from bs4 import BeautifulSoup
import re

hltv_url = "https://www.hltv.org/"
headers = {"Accept": "*/*",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

main_req = requests.get(url=hltv_url, headers=headers)
soup = BeautifulSoup(main_req.text, 'lxml')


def update_info():
    last_data_update = \
        re.search(r"\d\d?th of \w*", f"{soup.find(class_='leftCol').find_all(class_='normal-weight')[-1]}")[0] \
            .split()
    month = auxiliary_data.months[last_data_update[2]]
    day = last_data_update[0][:last_data_update[0].find('th')]
    info_from_mainPage["last_update_ranking"] = f"{datetime.date.today().isoformat()[:4]}/{month}/{day}"
    return 'updated'


def rating_parse() -> str:
    url = hltv_url + info_from_mainPage["last_update_ranking"]
    req = requests.get(url=url, headers=headers)
    return 'ok'

