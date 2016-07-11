# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-11 11:01:02
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-11 14:53:27


import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# docs_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'docs.json'))

import re
from digani.res.base import ResourceBase

class RESMethods(unittest.TestCase):
    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    def test_res_base(self):
        obj = ResourceBase()

    
if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()

        suite.addTest(RESMethods('test_res_base'))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()

