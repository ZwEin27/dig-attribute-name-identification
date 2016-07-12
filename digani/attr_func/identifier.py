# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-10 21:44:02
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-12 10:49:47

from base import AttributeFunctionBase

import re
re_alphabet = re.compile(r'[a-zA-Z]+')
re_digits = re.compile(r'[0-9]+')

class AttributeFunctionIdentifier(AttributeFunctionBase):

    @staticmethod
    def has_only_digits(attr_vals):
        for value in attr_vals:
            try:
                int(value)
            except:
                return False
        return True

    @staticmethod
    def valid_digit_length(attr_vals):
        for value in attr_vals:
            digits = re_digits.findall(value)
            digits = ''.join(digits)
            if len(digits) < 6:
                return False
        return True

    @staticmethod
    def refine(attr_vals):
        # specific refine function here
        return attr_vals

    @staticmethod
    def match(attr_vals):
        # freq_dict = super(AttributeFunctionIdentifier, AttributeFunctionIdentifier).frequent_count(attr_vals)

        if not has_only_digits(attr_vals):
            return False

        if not valid_digit_length(attr_vals):
            return False

        attr_vals = super(AttributeFunctionIdentifier, AttributeFunctionIdentifier).refine_attr_vals(attr_vals, AttributeFunctionIdentifier.refine)
        
        if not super(AttributeFunctionIdentifier, AttributeFunctionIdentifier).pre_judge(attr_vals):
            return False

        return True
