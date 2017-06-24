'''
Created on 22.06.2017

@author: Tomek
'''
import unittest
from scoreWriter.scoreWriter import ScoreWriter

class Test(unittest.TestCase):

    def scoreWriterToFile(self):
        '''
        Write score to file. Display only 10 positions
        '''
        sw = ScoreWriter('score.csv')
        sw.write(3, 10, 'kut01')
        re=sw.read_10pos()
        print(sw.format_table(re))
    
    def testName(self):
        self.scoreWriterToFile()
        
    def testScoreRead(self):
        sw = ScoreWriter('score.csv')
        listaPunktow =sw.read()
        print(len(listaPunktow))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()