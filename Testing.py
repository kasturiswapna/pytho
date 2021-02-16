# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:38:14 2021

@author: kastu
"""

# This program says hello and asks for my name.

print('Hello, world!')
print('What is your name?')    # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('what is your age')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')