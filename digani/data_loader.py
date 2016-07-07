# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-07 12:36:42
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-07 13:03:30

import os


class DataLoader():

    @staticmethod
    def load_domain_file_paths(root_dir):
        df_paths = {}
        for domain in os.listdir(root_dir):
            paths[domain] = []

            for subdir, dirs, files in os.walk(os.path.join(root_dir, domain)):
                for file in files:
                    if '_extractions' in file:
                        path = os.path.join(subdir, file)
                        paths[domain].append(path)
        return df_paths

if __name__ == '__main__':
    DataLoader().load_file_paths('../../dig-data/sample-datasets/escorts/')