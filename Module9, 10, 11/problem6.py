# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:32:20 2026

@author: daria
"""

def computeScore(score1, score2, score3):
    totalPoints = score1 + score2 + score3
    avrg = totalPoints / 3
    return totalPoints, avrg
loopResponse = "y"
while loopResponse == "y":
    lastName = input("Enter student last name: ")
    score1 = float(input("Enter score from first exam: "))
    score2 = float(input("Enter score from second exam: "))
    score3 = float(input("Enter score from third exam: "))
    totalPoints, avrg = computeScore(score1, score2, score3)
    print("Last name: ", lastName)
    print(f"Total points: {totalPoints:.2f}")
    print(f"Average exam score: {avrg:.2f}")
    loopResponse = input("Would you like to enter another student? y/n: ")
    