# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-07 12:36:42
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-07 13:24:12

import os
import json


def load_domain_file_paths(root_dir):
    df_paths = {}
    for domain in os.listdir(root_dir):
        df_paths[domain] = []

        for subdir, dirs, files in os.walk(os.path.join(root_dir, domain)):
            for file in files:
                if '_extractions' in file:
                    path = os.path.join(subdir, file)
                    df_paths[domain].append(path)
    return df_paths


def load_jsonlines_from_file(filepath):
    json_list = []
    with open(filepath, 'rb') as filehandler:
        for jsonline in filehandler.readlines():
            json_list.append(json.loads(jsonline))
    return json_list

def load_jsonlines_from_filepath_list(filepath_list):
    jsonlines = []
    for filepath in filepath_list:
        jsonlines.extend(load_jsonlines_from_file(filepath))
    return jsonlines
       


if __name__ == '__main__':
    load_domain_file_paths('../../dig-data/sample-datasets/escorts/')