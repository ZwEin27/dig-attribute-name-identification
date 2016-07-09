# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-08 13:40:38
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-09 10:58:30

import os
import json
import pygtrie
import codecs

RES_CITY_NAMES_PATH = os.path.join(os.path.dirname(__file__), 'names.json')

def load_city_names(city_names_path=RES_CITY_NAMES_PATH):
    names = json.load(codecs.open(self.city_names_path, 'r', 'utf-8'))
    names_trie_obj = pygtrie.CharTrie()
    for name in names:
        names_trie_obj[name] = name
    return names_trie_obj 

city_names_trie_obj = None
if not city_names_trie_obj:
    city_names_trie_obj = load_city_names()

def match_names(token, trie_obj=city_names_trie_obj):
    token = re.search('[a-zA-Z].*[a-zA-Z]', token)
    if token:
        value = t.value.get(token.group(0))
        if isinstance(value, basestring):
            return True
    return False

if __name__ == '__main__':
    # print res_city_names[:4]
    pass