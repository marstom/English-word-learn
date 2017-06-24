'''
Created on 24.06.2017

@author: Tomek
'''
import unittest
from scoreWriterM.scoreWriter import ScoreWriter

# class Test(unittest.TestCase):
#     def testName(self):
#         pass

def scoreTest():
    sw = ScoreWriter('./scoreTest.csv')
    sw.write(10, 10, 'Karotka')
    re=sw.read_10pos()
    print(sw.format_table(re))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
#     unittest.main()
    scoreTest()
