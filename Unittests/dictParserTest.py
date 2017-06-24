'''
Created on 22.06.2017

@author: Tomek
'''

# -*- coding: utf-8 -*-

import unittest

from dictParser.dictParser import DictParser

class Test(unittest.TestCase):
    def testGenerateRandowDict(self):
        dp = DictParser('../dictionaries/dictionary1.csv')
        dp._shuffle_data()
        for _ in range(100):
            item = dp.selectOneItemWithoutRepetitions()
            self.assertTrue((item in dp.lista), 'Item is wrong type! Should be list.')

def printLista():
    dp = DictParser('../dictionaries/dictionary1.csv')
    print(dp.lista)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    printLista()
    unittest.main()
    