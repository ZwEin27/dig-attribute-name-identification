# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-10 21:50:44
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-11 14:46:28

import re

class AttributeFunctionBase(object):

    def __init__(self, attr_vals):
        self.freq_dict, self.attr_vals = self.initialize(attr_vals)

    def initialize(self, attr_vals, threshold=0.8):
        # e.g. of <keyword>, remove of
        freq_dict = {}
        freq_token_dict = {}
        size = len(attr_vals)
        for value in attr_vals:
            for token in value.split():
                freq_token_dict.setdefault(token, 0)
                freq_token_dict[token] += 1
            freq_dict.setdefault(value, 0)
            freq_dict[value] += 1
        to_be_removed = []
        for (k, v) in freq_token_dict.iteritems():
            if (v != 0 and v % size == 0) or (float(v) / size >= threshold):
                to_be_removed.append(k)

        refiend_attr_vals = [''.join([_.replace(tbrw, '').strip() for tbrw in to_be_removed]) if to_be_removed else _ for _ in attr_vals]
        return freq_dict, refiend_attr_vals



if __name__ == '__main__':
    attr_vals = [
        'of hello',
        'of world',
        'of work',
        'of yes',
        'of ok',
        'sjkdflj',
        'foiwejfowi',
    ]
    obj = AttributeFunctionBase(attr_vals)
    # print obj.freq_dict
    print obj.attr_vals


