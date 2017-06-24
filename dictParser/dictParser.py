'''
Created on 04.03.2017

@author: Tomasz Marszalek	
@summary: element 0 in record is word for label, all next elements in line are words to guess.

@todo: add list all files in folder, dictionaries.
       change encoding for polish characters.
'''
# -*- coding: utf-8 -*-


import numpy as np
import urllib.request
class DictParser:
    lista=[]
    lenLista=0
    
    def __init__(self, path):
        self.loadDictionary(path)
        
    def loadDictionary(self, path):
        self.getFromURL()
        self._shuffle_data()
        print('init dict parser......') 
         
    def getFromURL(self):
        url = 'http://tommarsoftware.esy.es/dictionary1.csv'
        f = urllib.request.urlopen(url)
        mbytes = f.read()
        mystr = mbytes.decode('utf8')
        
        self.lista = self.createDictList(mystr)
        self.lenLista = len(self.lista)
        self.element = iter(self.lista)

    def createDictList(self, mystr):
        element = []
        records = mystr.split('\r\n')   
        for el in records:
            element.append(el.split(';'))
        return element
     
    def _shuffle_data(self):
        np.random.shuffle(self.lista)
        self.element = iter(self.lista)

    def selectOneItemWithoutRepetitions(self):
        try:
            return next(self.element)
        except StopIteration:
            self._shuffle_data()
            return next(self.element)
        
            
if __name__ == '__main__':
    dp = DictParser('../dictionaries/dictionary1.csv')
    dp._shuffle_data()
    for _ in range(100):
        print(dp.selectOneItemWithoutRepetitions())
        
    dp.getFromURL()

    