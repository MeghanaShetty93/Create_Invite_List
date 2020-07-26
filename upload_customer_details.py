#!/usr/bin/env python
# coding: utf-8

# In[3]:


import json
import os
import sys

def get_details():
    
    custList = []
    
    #Upload text file
    currentDirectory = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(currentDirectory, 'customers.txt')) as input:
   # with open('C:/Users/Dell/Anaconda3/FinalTest/customers.txt') as input :
        for line in input:
            custDict = json.loads(line)
            custList.append(custDict)
    return custList


# In[ ]:




