# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:04:21 2026

@author: daria
"""

lastName = input("Enter your last name: ")
midScore = float(input("Enter your midterm score: "))
finalScore = float(input("Enter your final score: "))
totalPoints = (midScore * 0.4) + (finalScore * 0.6)
print(f"{lastName} {totalPoints:.2f}")