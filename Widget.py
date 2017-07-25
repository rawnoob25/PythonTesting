# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 20:48:00 2017

Simple class to model a python widget
"""

DEFAULT_SIZE = (50,50)

class Widget:
    def __init__(self,s):
        self.s=s
        self.dims=DEFAULT_SIZE
    
    def size(self):
        return self.dims
    
    def resize(self,dims):
        self.dims = dims