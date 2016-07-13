# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-11 18:04:06
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-13 12:23:58




from digani.res.breast import res_breast_obj
from base import AttributeFunctionBase

import re
reg_breast = r'(?:\w+)'
re_breast = re.compile(reg_breast)

class AttributeFunctionBreast(AttributeFunctionBase):

    @staticmethod
    def valid_breast(string):
        extractions = re_breast.findall(string)
        for extraction in extractions:
            try:
                integer_ext = int(extraction)
                if integer_ext >=28 and integer_ext <= 45:
                    continue
            except Exception as e:
                pass
            if not res_breast_obj.match(extraction):  
                return False
        return True

    @staticmethod
    def refine(attr_vals):
        # specific refine function here
        return attr_vals

    @staticmethod
    def match(attr_vals):
        # freq_dict = super(AttributeFunctionBreast, AttributeFunctionBreast).frequent_count(attr_vals)

        # attr_vals = super(AttributeFunctionBreast, AttributeFunctionBreast).refine_attr_vals(attr_vals, AttributeFunctionBreast.refine)

        # print attr_vals
        if not super(AttributeFunctionBreast, AttributeFunctionBreast).pre_judge(attr_vals):
            return False

        if not super(AttributeFunctionBreast, AttributeFunctionBreast).valid_counts(attr_vals, AttributeFunctionBreast.valid_breast, threshold=0.4):
            return False

        return True