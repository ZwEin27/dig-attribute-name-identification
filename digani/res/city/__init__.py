# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-08 13:40:38
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-09 11:49:09

import os
import json
import codecs
from digani.common import trie_helper

RES_CITY_NAMES_PATH = os.path.join(os.path.dirname(__file__), 'names.json')

city_names_trie_obj = None

def load(names_path=RES_CITY_NAMES_PATH):
    global city_names_trie_obj

    if not city_names_trie_obj or names_path:
        names = json.load(codecs.open(names_path, 'r', 'utf-8'))
        trie_obj = trie_helper.load_trie_obj(names)
        city_names_trie_obj = trie_obj

    return city_names_trie_obj

city_names_trie_obj = load()

def match(token):
    return trie_helper.match_names(token, city_names_trie_obj)
    
if __name__ == '__main__':
    pass