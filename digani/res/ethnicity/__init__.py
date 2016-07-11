# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-08 13:40:38
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-11 18:00:40

import os
import pygtrie
from digani.res.base import ResourceBase

class ResourceEthnicity(ResourceBase):

    res_names_path = os.path.join(os.path.dirname(__file__), 'names.json')
    res_trie_obj = pygtrie.CharTrie()
    ethnicity_color = [
        'White',
        'Black',
        'Yellow'
    ]

    def __init__(self):
        ResourceBase.__init__(self)
        self.load()

    def load(self, trie_obj=res_trie_obj, names_path=res_names_path):
        super(ResourceEthnicity, self).load(trie_obj, names_path=names_path)

    def match(self, token):
        return super(ResourceEthnicity, self).match(token, ResourceEthnicity.res_trie_obj)

res_ethnicity_obj = ResourceEthnicity()