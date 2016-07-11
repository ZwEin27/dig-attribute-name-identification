# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-10 21:44:02
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-10 21:54:03

import re
re_alphabet = re.compile(r'[a-zA-Z]+')
re_digits = re.compile(r'[0-9]+')

def attr_func_identifier(attr_vals):

    count = 0
    size = len(attr_vals)
    for value in attr_vals:
        if not value or value == '':
            continue

        if re_alphabet.search(value):
            return False

        try:
            int(value)
        except:
            return False

        digits = re_digits.findall(value)
        digits = ''.join(digits)
        if len(digits) != 6:
            return False

        count += 1

    if count == 0:
        return False
    if float(count) / size < 0.8:
        return False
    return True


if __name__ == '__main__':
    values = [
        '248449'
    ]
    print attr_func_identifier(values)

