# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-08 13:40:38
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-09 10:36:09

import os
import json
import pygtrie

RES_CITY_NAMES_PATH = os.path.join(os.path.dirname(__file__), 'names.json')

def load_city_names(city_names_path=RES_CITY_NAMES_PATH):
    names = json.load(codecs.open(self.city_names_path, 'r', 'utf-8'))
    names_trie_obj = pygtrie.CharTrie()
    for name in names:
        names_trie_obj[name] = name
    return names_trie_obj

    # with open(city_names_path, 'rb') as file_handler:
    #     city_names = json.load(file_handler)
    #     return city_names

city_names_trie_obj = None
if not city_names_trie_obj:
    city_names_trie_obj = load_city_names()

if __name__ == '__main__':
    # print res_city_names[:4]
    pass