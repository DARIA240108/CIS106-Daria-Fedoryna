# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:12:34 2026

@author: daria
"""

def compBattingAverage(hits, atBats):
    battingAverage = hits / atBats
    return battingAverage 
count = 0
loopResponse = "y"

while loopResponse == "y":
    lastName = input("Enter player last name: ")
    hits = int(input("Enter number of hits: "))
    atBats = int(input("Enter number of at bats: "))
    battingAverage = compBattingAverage(hits, atBats)
    print("Last name", lastName)
    print(f"Batting average: {battingAverage:.3f}")
    count = count + 1
    loopResponse = input("Would you like to continue? y/n: ")
print("Number of players entered: ", count)
