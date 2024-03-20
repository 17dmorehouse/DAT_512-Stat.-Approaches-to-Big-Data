# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 19:08:34 2024

@author: dev46
"""
import easygui as g

title = 'grab a file'
filename = g.fileopenbox( title )

print(filename)
