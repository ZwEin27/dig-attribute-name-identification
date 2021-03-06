# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-13 11:55:55
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-13 12:18:29


from digani.res.nationality import res_nationality_obj
from base import AttributeFunctionBase
# import re
# reg_en_color = r'(?:\s*(white|black|yellow)\s*)'
# re_en_color = re.compile(reg_en_color)
# string = re_en_color.sub('', string)

class AttributeFunctionNationality(AttributeFunctionBase):

    @staticmethod
    def valid_nationality(string):# check empty set
        extractions = string.split()
        if len(extractions) > 3:
            return False

        for extraction in extractions:
            if not res_nationality_obj.match(extraction):  
                return False
        return True

    @staticmethod
    def refine(attr_vals):
        # specific refine function here
        return attr_vals

    @staticmethod
    def match(attr_vals):
        # freq_dict = super(AttributeFunctionNationality, AttributeFunctionNationality).frequent_count(attr_vals)

        attr_vals = super(AttributeFunctionNationality, AttributeFunctionNationality).refine_attr_vals(attr_vals, AttributeFunctionNationality.refine)

        # print attr_vals
        if not super(AttributeFunctionNationality, AttributeFunctionNationality).pre_judge(attr_vals):
            return False

        if not super(AttributeFunctionNationality, AttributeFunctionNationality).valid_counts(attr_vals, AttributeFunctionNationality.valid_nationality, threshold=0.4):
            return False

        return True
