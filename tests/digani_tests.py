
import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# docs_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'docs.json'))

import re
import json
import digani

class TestMainMethods(unittest.TestCase):
    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    def test_digani(self):
        digani.run('../../dig-data/sample-datasets/escorts/')
       
if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()

        suite.addTest(TestMainMethods('test_digani'))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()

