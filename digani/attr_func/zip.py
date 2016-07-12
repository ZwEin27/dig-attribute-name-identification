# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-11 18:03:23
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-12 10:50:00

from base import AttributeFunctionBase
from digani.res.zip import res_zip_obj

import re
re_alphabet = re.compile(r'[a-zA-Z]+')
re_digits = re.compile(r'[0-9]+')

class AttributeFunctionZip(AttributeFunctionBase):

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
            if len(digits) != 6:    # 3-6 for US zip
                return False
        return True

    @staticmethod
    def refine(attr_vals):
        # specific refine function here
        return attr_vals

    @staticmethod
    def match(attr_vals):
        # freq_dict = super(AttributeFunctionZip, AttributeFunctionZip).frequent_count(attr_vals)
        
        if not has_only_digits(attr_vals):
            return False

        if not valid_digit_length(attr_vals):
            return False

        attr_vals = super(AttributeFunctionZip, AttributeFunctionZip).refine_attr_vals(attr_vals, AttributeFunctionZip.refine)
        
        if not super(AttributeFunctionZip, AttributeFunctionZip).pre_judge(attr_vals):
            return False

        if not super(AttributeFunctionZip, AttributeFunctionZip).valid_counts(attr_vals, res_zip_obj.match, threshold=0.4):
            return False

        return True
