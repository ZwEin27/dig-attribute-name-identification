# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-07 13:16:06
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-07 14:15:57

import json
import data_loader

def dummy():
    pass


ATTRIBUTE_NAMES = {
    'phone_number': dummy,
    'date': dummy,
    'email': dummy,
    'text': dummy,
    'junk': dummy
}

def load_attribute_values(jsonlines):
    attribute_values_dict = {}
    for jsonline in jsonlines:
        json_obj = json.loads(jsonline)
        for (k, v) in json_obj.items():
            attribute_values_dict.setdefault(k, [])
            attribute_values_dict[k].append(v)
    return attribute_values_dict


def identify_attribute_name(attr_vals, attr_func_handlers=ATTRIBUTE_NAMES):
    pass


def identify(filepath, output=None):
    
    mapping = {}

    jsonlines = data_loader.load_jsonlines_from_file(filepath)
    attribute_values_dict = load_attribute_values(jsonlines)

    for (attribute, values) in attribute_values_dict:
        pred_attr_name = identify_attribute_name(values)
        mapping[attribute] = pred_attr_name


    """
    if output:
        file_handler = open(path, 'wb')
        # do something
        file_handler.close()
    """ 

if __name__ == '__main__':
    pass