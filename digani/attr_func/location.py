# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-11 18:03:13
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-13 10:17:08


from digani.res.city import res_city_obj
from digani.res.state import res_state_obj
from digani.res.country import res_country_obj
from base import AttributeFunctionBase

class AttributeFunctionLocation(AttributeFunctionBase):

    @staticmethod
    def valid_location(string):
        def is_valid(string):
            if not (res_city_obj.match(string) or res_state_obj.match(string) or res_country_obj.match(string)):
                return False
            return True
            
        tokens = string.split(',')
        if len(tokens) > 1:
            for token in tokens:
                if not is_valid(string):
                    return False
        else:
            return is_valid(string)
        return True

    @staticmethod
    def refine(attr_vals):
        # specific refine function here
        return attr_vals

    @staticmethod
    def match(attr_vals):
        # freq_dict = super(AttributeFunctionLocation, AttributeFunctionLocation).frequent_count(attr_vals)

        attr_vals = super(AttributeFunctionLocation, AttributeFunctionLocation).refine_attr_vals(attr_vals, AttributeFunctionLocation.refine)

        if not super(AttributeFunctionLocation, AttributeFunctionLocation).pre_judge(attr_vals):
            return False

        if not super(AttributeFunctionLocation, AttributeFunctionLocation).valid_counts(attr_vals, AttributeFunctionLocation.valid_location, threshold=0.4):
            return False

        return True

"""

(super(AttributeFunctionLocation, AttributeFunctionLocation).valid_counts(attr_vals, res_city_obj.match, threshold=0.4) or \
super(AttributeFunctionLocation, AttributeFunctionLocation).valid_counts(attr_vals, res_state_obj.match, threshold=0.4) or \
super(AttributeFunctionLocation, AttributeFunctionLocation).valid_counts(attr_vals, res_country_obj.match, threshold=0.4) \
):
"""