# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-07 13:16:06
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-08 10:24:51

import re
import json
import data_loader
from attr_func import *

def dummy(attr_vals):
    return False

ATTRIBUTE_NAMES = { # in order
    'phone_number': attr_func_phone_number,
    'date': attr_func_date,
    'email': attr_func_email,
    'state': dummy,
    'city': dummy,
    'name': dummy,
    'text': attr_func_text,
    'junk': attr_func_junk,
    'unkown': lambda _: True
}

IGNORED_ATTRIBUTE_NAMES = [
    '_url',
    '_cdr_id'
]

def load_attribute_values(jsonlines):
    attribute_values_dict = {}
    for jsonline in jsonlines:
        try:
            json_obj = json.loads(jsonline)
        except Exception as e:
            raise Exception(e, 'parse json string error')
        for (k, v) in json_obj.items():
            attribute_values_dict.setdefault(k, [])
            attribute_values_dict[k].append(v)
    return attribute_values_dict


def identify_attribute_name(attr_vals, attr_func_handlers=ATTRIBUTE_NAMES):
    for (attr_name, attr_func) in attr_func_handlers.items():
        if attr_func(attr_vals):
            return attr_name
    return None


def identify(filepath, output=None):
    
    mapping = {}

    jsonlines = data_loader.load_jsonlines_from_file(filepath)
    attribute_values_dict = load_attribute_values(jsonlines)

    for (attribute, values) in attribute_values_dict.items():
        if attribute in IGNORED_ATTRIBUTE_NAMES:
            continue
        mapping[attribute] = identify_attribute_name(values)

    if output:
        file_handler = open(output, 'wb')
        file_handler.write(json.dumps(mapping))
        file_handler.close()

if __name__ == '__main__':
    pass

