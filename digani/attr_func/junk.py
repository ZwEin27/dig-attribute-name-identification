# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-07 15:54:26
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-09 16:30:04

import re


re_alphabet = re.compile(r'[a-zA-Z]+')
re_digits = re.compile(r'[0-9]+')


def frequency_count(attr_vals):
    freq_dict = {}
    for value in attr_vals:
        freq_dict.setdefault(value, 0)
        freq_dict[value] += 1
    return freq_dict

def attr_func_junk(attr_vals):
    size = len(attr_vals)
    freq_dict = frequency_count(attr_vals)

    if len(freq_dict.keys()) <= 5:
        return True

    return False