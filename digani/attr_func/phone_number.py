# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-07 14:30:09
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-07 15:53:19
import re

from pnmatcher import PhoneNumberMatcher
matcher = PhoneNumberMatcher()

re_alphabet = re.compile(r'[a-zA-Z]+')
re_digits = re.compile(r'[0-9]+')

def attr_func_phone_number(attr_vals):
    valid_pn = []
    exist_flag = False
    empty_count = 0
    size = len(attr_vals)
    for value in attr_vals:
        if not value or value == '':
            empty_count += 1
            continue

        if re_alphabet.findall(value):
            return False

        digits = re_digits.findall(value)
        if not digits:
            return False

        digits = ''.join(digits)
        if len(digits) < 6 or len(digits) > 13:
            return False

        extraction = matcher.match(value, source_type='text')
        # print value, extraction
        if not extraction:
            return False

    if size == empty_count:
        return False

    return True