# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-08 13:47:38
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-08 14:33:22

from digani.res import *

def attr_func_city(attr_vals):

    count = 0
    # size = len(attr_vals)
    for value in attr_vals:
        if not value or value == '':
            continue

        if value.strip().lower() in res_city_names:
            count += 1

    if count == 0:
        return False


    return True

# print res_city_names[:4]