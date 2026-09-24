# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:02:03 2026

@author: daria
"""

startVal = int(input("Enter start value: "))
stopVal = int(input("Enter stop value: "))
incrementVal = int(input("Enter increment value: "))
number =  startVal

while number <= stopVal:
    print(number)
    number = number + incrementVal
