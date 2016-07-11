# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-07 15:54:26
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-10 21:42:21

import re
# from digani.common import string_helper

re_alphabet = re.compile(r'[a-zA-Z]+')
re_digits = re.compile(r'[0-9]+')

reg_junks = [
    # r'[0-9]+.*[a-z]+',
    # r'[a-z]+.*[0-9]+'
    r'(?:\d+)'
]
re_junks = re.compile(r'^' + r'|'.join(reg_junks) + r'$')

def frequency_count(attr_vals):
    freq_dict = {}
    for value in attr_vals:
        freq_dict.setdefault(value, 0)
        freq_dict[value] += 1
    return freq_dict

def attr_func_junk(attr_vals):
    size = len(attr_vals)

    # number of attribute values, junk if less than 5
    freq_dict = frequency_count(attr_vals)
    if len(freq_dict.keys()) <= 5:
        return True

    # if string_helper.is_integer(content):
    for value in attr_vals:
        if not value or value == '':
            continue

        if re_junks.search(value):
            return True

    return False


if __name__ == '__main__':
    # text = ': 34-35 34 B Eyes: Brown Smokes: Yes but not with '
    text = '2015'
    print re_junks.findall(text)