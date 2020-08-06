# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 20:42:55 2020

@author: Tom

This shows usage of the "muse finder" function set. Just a fun way to pick who
you should use as inspiration, based on the box office results on the day of
your birth.
"""

import muse_finder

month = 'Oct'
day = 26
year = 1990

print(muse_finder.getMuse(month,day,year))