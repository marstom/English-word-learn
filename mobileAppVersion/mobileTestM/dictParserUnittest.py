'''
Created on 24.06.2017

@author: Tomek
'''

# -*- coding: utf-8 -*-
# import unittest
from dictParserM.dictParser import DictParser

# class Test(unittest.TestCase):

#     def testName(self):
#         pass


def printDictionaries():
    dp = DictParser('./dictionaries/dictionary1.csv')
    print(dp.lista)
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    printDictionaries()
    # unittest.main()