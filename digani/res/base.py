# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-11 11:28:57
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-11 15:00:30

import os
import json
import codecs
import pygtrie
from digani.common import trie_helper

class ResourceBase(object):

    def __init__(self):
        self.path = os.path.dirname(__file__)

    def load(self, trie_obj, names_path=None):
        if not trie_obj or names_path:
            names = json.load(codecs.open(names_path, 'r', 'utf-8'))
            trie_obj = trie_helper.load_trie_obj(trie_obj, names)
        return trie_obj

    def match(self, token, trie_obj):
        return trie_helper.match_names(token, trie_obj)





    