# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-11 11:01:02
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-11 23:16:21


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

class AttributeFunctionMethods(unittest.TestCase):
    def setUp(self):
        self.attr_vals = ['black', 'white', 'black', 'white', 'white', 'black', 'white']
        
    def tearDown(self):
        pass

    def test_func_base(self):
        pass

    def test_func_person(self):
        attr_vals = [
            'anna (0)',
            'roslyn (1)'
        ]
        print AttributeFunctionPerson.match(attr_vals)
    
if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()

        # suite.addTest(AttributeFunctionMethods('test_func_base'))
        suite.addTest(AttributeFunctionMethods('test_func_person'))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()

