# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-08 13:47:38
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-11 15:45:45

from digani.res import city

def attr_func_city(attr_vals):

    count = 0
    size = len(attr_vals)
    for value in attr_vals:

        if not value or value == '':
            continue

        if city.match(value):
            # print 'value match', value
            count += 1

    if count == 0:
        return False
    # print float(count), size
    if float(count) / size < 0.6:
        return False
    return True

