# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-07 14:30:09
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-12 19:06:45

import re
from base import AttributeFunctionBase
from pnmatcher import PhoneNumberMatcher
re_alphabet = re.compile(r'[a-zA-Z]+')
re_digits = re.compile(r'[0-9]+')
matcher = PhoneNumberMatcher()

class AttributeFunctionTelephone(AttributeFunctionBase):

    @staticmethod
    def valid_telephone(string):

        def has_only_digits(string):
            try:
                int(string)
            except:
                return False
            return True

        def valid_digit_length(string):
            digits = re_digits.findall(string)
            digits = ''.join(digits)
            if len(digits) < 6 or len(digits) > 13:
                return False
            return True

        if not has_only_digits(string):
            return False

        if not valid_digit_length(string):
            return False

        if not matcher.match(string, source_type='text'):
            return False

        return True

    @staticmethod
    def refine(attr_vals):
        # specific refine function here
        return attr_vals

    @staticmethod
    def match(attr_vals):
        # freq_dict = super(AttributeFunctionTelephone, AttributeFunctionTelephone).frequent_count(attr_vals)

        attr_vals = super(AttributeFunctionTelephone, AttributeFunctionTelephone).refine_attr_vals(attr_vals, AttributeFunctionTelephone.refine)

        if not super(AttributeFunctionTelephone, AttributeFunctionTelephone).pre_judge(attr_vals):
            return False

        if not super(AttributeFunctionTelephone, AttributeFunctionTelephone).valid_counts(attr_vals, AttributeFunctionTelephone.valid_telephone, threshold=0.8):
            return False

        return True


"""
import re

from pnmatcher import PhoneNumberMatcher
matcher = PhoneNumberMatcher()

re_alphabet = re.compile(r'[a-zA-Z]+')
re_digits = re.compile(r'[0-9]+')

def attr_func_telephone(attr_vals):

    
    count = 0
    size = len(attr_vals)
    
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
    if float(count) / size < 0.8:
        return False
    return True
"""