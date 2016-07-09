# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-08 13:40:38
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-08 14:05:00

import os
import json

RES_CITY_NAMES_PATH = os.path.join(os.path.dirname(__file__), 'names.json')

def load_city_names():
    with open(RES_CITY_NAMES_PATH, 'rb') as file_handler:
        city_names = json.load(file_handler)
        return city_names

res_city_names = None
if not res_city_names:
    res_city_names = load_city_names()

if __name__ == '__main__':
    print res_city_names[:4]