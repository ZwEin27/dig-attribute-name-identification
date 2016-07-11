# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-11 11:01:02
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-11 11:20:01


import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# docs_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'docs.json'))

import re
import json
from digani.attr_func import *
from digani.res import city

class FuncCityMethods(unittest.TestCase):
    def setUp(self):
        self.attr_vals = ['black', 'white', 'black', 'white', 'white', 'black', 'white']
        
    def tearDown(self):
        pass

    def test_func_city(self):
        print attr_func_city(self.attr_vals)

    def test_res_city(self):
        value = 'white'
        print city.match(value)
    
if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()

        # suite.addTest(FuncCityMethods('test_func_city'))
        suite.addTest(FuncCityMethods('test_res_city'))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()

