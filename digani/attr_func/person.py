# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-08 13:48:43
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-09 11:44:39

from digani.res import person

def attr_func_person(attr_vals):

    count = 0
    # size = len(attr_vals)
    for value in attr_vals:
        if not value or value == '':
            continue

        if person.match(value):
            count += 1

    if count == 0:
        return False
    return True