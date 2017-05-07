'''
Created on 04.03.2017

@author: Tomasz Marszalek	
@summary: element 0 in record is word for label, all next elements in line are words to guess.

@todo: add list all files in folder, dictionaries.
       change encoding for polish characters.
'''
# -*- coding: utf-8 -*-
import csv
import random
import numpy as np

class DictParser:
    lista=[]
    lenLista=0
    
    def __init__(self, path):
        pass
        #fn='./dictionaries/dictionary1.csv'
        self.read_file(path)
        self.shuffle_data()
        print('init dict parser......')
        
    def read_file(self,filename):
        with open(filename,'r',encoding='utf-8') as fp:
            csvRead = csv.reader(fp, delimiter=';')
            for el in csvRead:
                self.lista.append(el)
        self.lenLista=len(self.lista)
        self.element = iter(self.lista)
        
    def shuffle_data(self):
        np.random.shuffle(self.lista)
        self.element = iter(self.lista)

    def pick_one(self):
        try:
            return next(self.element)
        except StopIteration:
            self.shuffle_data()
            return next(self.element)
        
            
if __name__ == '__main__':
    dp = DictParser('../dictionaries/dictionary1.csv')
    dp.shuffle_data()
    for _ in range(100):
        print(dp.pick_one())

    