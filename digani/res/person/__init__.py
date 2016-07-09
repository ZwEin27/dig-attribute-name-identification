# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-08 13:40:38
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-09 14:56:24

import os
import json
import codecs
import pygtrie
from digani.common import trie_helper

RES_PERSON_NAMES_PATH = os.path.join(os.path.dirname(__file__), 'names.json')

person_names_trie_obj = pygtrie.CharTrie()

def load(names_path=RES_PERSON_NAMES_PATH):
    global person_names_trie_obj

    if not person_names_trie_obj or names_path:
        names = json.load(codecs.open(names_path, 'r', 'utf-8'))
        trie_obj = trie_helper.load_trie_obj(person_names_trie_obj, names)
        person_names_trie_obj = trie_obj

    return person_names_trie_obj

person_names_trie_obj = load()

def match(token):
    return trie_helper.match_names(token, person_names_trie_obj)
    
if __name__ == '__main__':
    pass