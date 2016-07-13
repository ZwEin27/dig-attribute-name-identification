# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-11 14:10:13
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-13 12:09:56


from digani.res.ethnicity import res_ethnicity_obj
from base import AttributeFunctionBase
# import re
# reg_en_color = r'(?:\s*(white|black|yellow)\s*)'
# re_en_color = re.compile(reg_en_color)
# string = re_en_color.sub('', string)

class AttributeFunctionEthnicity(AttributeFunctionBase):

    @staticmethod
    def valid_ethnicity(string):# check empty set
        extractions = string.split()
        if len(extractions) > 3:
            return False

        for extraction in extractions:
            if not res_ethnicity_obj.match(extraction):  
                return False
        return True

    @staticmethod
    def refine(attr_vals):
        # specific refine function here
        return attr_vals

    @staticmethod
    def match(attr_vals):
        # freq_dict = super(AttributeFunctionEthnicity, AttributeFunctionEthnicity).frequent_count(attr_vals)

        attr_vals = super(AttributeFunctionEthnicity, AttributeFunctionEthnicity).refine_attr_vals(attr_vals, AttributeFunctionEthnicity.refine)

        # print attr_vals
        if not super(AttributeFunctionEthnicity, AttributeFunctionEthnicity).pre_judge(attr_vals):
            return False

        if not super(AttributeFunctionEthnicity, AttributeFunctionEthnicity).valid_counts(attr_vals, AttributeFunctionEthnicity.valid_ethnicity, threshold=0.4):
            return False

        return True






if __name__ == '__main__':
    attr_vals = [
        'of hello',
        'of world',
        'of work',
        'of yes',
        'of ok',
        'of sjkdflj',
        'foiwejfowi',
    ]
    obj = AttributeFunctionEthnicity(attr_vals)
    print obj.attr_vals