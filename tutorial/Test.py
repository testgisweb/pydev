# -*- coding: utf-8 -*-
# Test.py

import os

class Car:

    def __init__(self,color,size):
        self.color = color
        self.size = size

    def get_color(self):
        print "Color is : " , self.color

my_car = Car("blue",12)
my_car.get_color()
