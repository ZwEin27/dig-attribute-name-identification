# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-07 14:30:09
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-08 13:49:26
import re

from pnmatcher import PhoneNumberMatcher
matcher = PhoneNumberMatcher()

re_alphabet = re.compile(r'[a-zA-Z]+')
re_digits = re.compile(r'[0-9]+')

def attr_func_telephone(attr_vals):

    # size = len(attr_vals)
    count = 0
    
    for value in attr_vals:
        if not value or value == '':
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

        count += 1

    if count == 0:
        return False

    return True