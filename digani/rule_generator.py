# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-09 14:35:51
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-09 14:50:36

import os
import codecs
import json

FILIENAME_RULES_STEP01 = 'step01_rules.json'
FILIENAME_RULES_STEP02 = 'step02_rules.json'


def generate_step02_rules(mapping, step01_rules_path):
    rules = json.load(codecs.open(step01_rules_path, 'r', 'utf-8'))
    for rule in rules:
        rule['name'] = mapping[rule['name']]
    return rules


def generate(mapping, output_dir, show_mapping=False):

    step01_rules_path = os.path.join(output_dir, FILIENAME_RULES_STEP01)
    step02_rules_path = os.path.join(output_dir, FILIENAME_RULES_STEP02)
    file_handler = open(step02_rules_path, 'wb')

    rules = mapping if show_mapping else generate_step02_rules(mapping, step01_rules_path)
    
    file_handler.write(json.dumps(rules, indent=2, sort_keys=True))
    file_handler.close()