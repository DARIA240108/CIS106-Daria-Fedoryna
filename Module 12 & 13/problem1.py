# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 09:12:40 2026

@author: daria
"""

lastName = ["Smith", "Fedoryna", "Grabchuk", "Shevchuk", "Liush", "Strutynska", "Popil", "Vintoniv", "Suleimanova", "Boliukh"]
def displayName():
    for name in lastName:
        print(name)
displayName()

def displayReverse():
    index = len(lastName) - 1
    while index >= 0:
        print(lastName[index])
        index = index -1
displayReverse()