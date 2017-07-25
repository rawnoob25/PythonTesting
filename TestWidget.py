# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 22:28:45 2017

This is a basic testing example.
The class DefaultWidgetSizeTestCase extends
unittest.TestCase. It inherits all methods
from unittest.TestCase.

The class provides a static method to setUp the 
test class as well as static methods to test the init
and resize methods in class Widget.

The static methods to test Widget.init() (test_default_widget_size)
and Widget.resize() (test_widget_resize) make calls
to the instance methods assertEqual(), assertTrue(),
and assertFalse(); these methods are inherited
from class unittest.TestCase.

"""

import os
print(os.getcwd())
from Widget import Widget
from Widget import DEFAULT_SIZE
import unittest


    
class WidgetTest(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The Widget')
       
    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), DEFAULT_SIZE)
        self.assertTrue(self.widget.size() == DEFAULT_SIZE)
        self.assertFalse(self.widget.size() == (40,50))
    
    def test_widget_resize(self):
        self.widget.resize((100,150))
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')
        self.assertFalse(self.widget.size() == (50,50))
        self.assertTrue(self.widget.size() == (100,150))
        
if __name__ == '__main__':
    unittest.main()
