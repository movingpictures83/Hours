#!/usr/bin/env python
# coding: utf-8

# In[143]:


import pandas as pd
import numpy as np



class HoursPlugin:
    def input(self, filename):
       self.df = pd.read_csv(filename)
       self.df.head()
    def run(self):
       datetime_series = pd.to_datetime(self.df['Time'])
       self.df['Timestamp'] = pd.DatetimeIndex(datetime_series.values)
       self.df = self.df.set_index('Timestamp')
       self.df.resample('H').mean()
    def output(self, filename):
       self.df.to_csv(filename)






