# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-07 15:52:57
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-08 13:32:10

import re
import dateutil.parser as dparser

irrelations = [
    r'\d{1,3}',
]
reg_irrelation = r'|'.join(irrelations)
# print reg_irrelation
re_irrelation = re.compile(reg_irrelation)

def has_date(string):
    try:
        date = dparser.parse(string) # fuzzy=True
    except:
        return False
    else:
        return True

def attr_func_date(attr_vals):
    count = 0
    for value in attr_vals:
        if not value or value == '':
            continue

        if re_irrelation.match(value):
            return False

        if not has_date(value):
            return False

        count += 1

    if count == 0:
        return False

    return True



if __name__ == '__main__':
    text = '201 s'
    if re_irrelation.match(text):
        print 'True'
    else:
        print 'False'