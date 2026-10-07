# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 09:12:40 2026

@author: daria
"""

lastName = ["Smith", "Fedoryna", "Grabchuk", "Shevchuk", "Liush", "Strutynska", "Popil", "Vintoniv", "Suleimanova", "Boliukh"]
examScore = [65, 73, 95, 100, 88, 86, 45, 66, 99, 78]
def displayName():
    index = 0
    while index < len(lastName):
        print(lastName[index], examScore[index])
        index = index + 1
displayName()

def displayReverse():
    index = len(lastName) - 1
    while index >= 0:
        print(lastName[index], examScore[index])
        index = index -1
displayReverse()