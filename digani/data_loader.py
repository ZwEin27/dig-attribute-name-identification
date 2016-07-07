# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-07 12:36:42
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-07 12:45:17

import os


class DataLoader():

    @staticmethod
    def load_file_paths(root_dir):
        paths = []
        for subdir, dirs, files in os.walk(root_dir):
            for file in files:
                if '_extractions' in file:
                    path = os.path.join(subdir, file)
                    print path
                    paths.append(path)
        return paths

if __name__ == '__main__':
    DataLoader().load_file_paths('../../dig-data/sample-datasets/escorts/')