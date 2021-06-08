# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ranzhi_project
# FileName:     Test_unittest
# Author:      Jakiro
# Datetime:    2020/12/8 10:22
# Description:
# -----------------------------------------------------------------------------------

import unittest

class Test23(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('setUpClass')

    @classmethod
    def tearDownClass(self):
        print('tearDownClass')

    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_1(self):
        print('test_1')

if __name__ == '__main__':
    unittest.main()