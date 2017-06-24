'''
Created on 04.03.2017

@author: Tomasz Marszalek	
@summary: element 0 in record is word for label, all next elements in line are words to guess.

@todo: add list all files in folder, dictionaries.
       change encoding for polish characters.
'''
# -*- coding: utf-8 -*-
import numpy as np
class DictParser:
    lista=[]
    lenLista=0
    
    def __init__(self, path):
        self.loadDictionary(path)
        
        
    def loadDictionary(self, path):
        with open(path, 'r') as fp:
            for el in fp:
                el=el.strip()
                lines = el.split('\r\n')
                for el in lines:
                    record = el.split(';')
                    self.lista.append(record)
            self.lenLista=len(self.lista)
            self.element = iter(self.lista)
     
    def _shuffle_data(self):
        np.random.shuffle(self.lista)
        self.element = iter(self.lista)

    def selectOneItemWithoutRepetitions(self):
        try:
            return next(self.element)
        except StopIteration:
            self._shuffle_data()
            return next(self.element)