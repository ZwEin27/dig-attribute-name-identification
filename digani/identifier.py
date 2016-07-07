# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-07 13:16:06
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-07 13:26:18

import data_loader

def identify(filepath_list, output=None):
    jsonlines = data_loader.load_jsonlines_from_filepath_list(filepath_list)
    

    """
    if output:
        file_handler = open(path, 'wb')
        # do something
        file_handler.close()
    """