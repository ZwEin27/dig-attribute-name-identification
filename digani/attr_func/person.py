# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-08 13:48:43
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-09 16:25:27

from digani.res import person

def attr_func_person(attr_vals):

    count = 0
    size = len(attr_vals)
    for value in attr_vals:
        if not value or value == '':
            continue

        if person.match(value):
            # print value
            count += 1

    if count == 0:
        return False
    # print count, size
    if float(count) / size < 0.4:
        return False
    return True