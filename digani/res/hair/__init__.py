# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-11 17:57:13
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-11 18:01:23


import os
import pygtrie
from digani.res.base import ResourceBase

class ResourceHair(ResourceBase):

    res_names_path = os.path.join(os.path.dirname(__file__), 'names.json')
    res_trie_obj = pygtrie.CharTrie()

    def __init__(self):
        ResourceBase.__init__(self)
        self.load()

    def load(self, trie_obj=res_trie_obj, names_path=res_names_path):
        super(ResourceHair, self).load(trie_obj, names_path=names_path)

    def match(self, token):
        return super(ResourceHair, self).match(token, ResourceHair.res_trie_obj)

res_hair_obj = ResourceHair()