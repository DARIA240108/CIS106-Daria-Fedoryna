# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 09:54:06 2026

@author: daria
"""

student = {
    "Fedoryna": [77, 85, 81],
    "Grabchuk": [68, 53,42],
    "Shevchuk": [99, 56, 78],
    "Liush": [85, 67, 80],
    "Strytunska": [90, 69, 91],
    "Popil": [63, 94, 72],
    "Vintoniv": [74,58, 99],
    "Suleimanova": [82, 83, 90],
    "Boliukh": [100, 68, 90],
    "Smith": [65, 78, 97]
    }
def studentAvrg():
    for name in student:
        grades = student[name]
        total = grades[0] + grades[1] + grades[2]
        avrg = total / 3
        print(name, avrg)
studentAvrg()
grade1Total = 0
grade2Total = 0
grade3Total = 0
for name in student:
    grade1Total = grade1Total + student[name][0]
    grade2Total = grade2Total + student[name][1]
    grade3Total = grade3Total + student[name][2]
grade1Avrg = grade1Total / len(student)
grade2Avrg = grade2Total / len(student)
grade3Avrg = grade3Total / len(student)
print("Grade 1 class average: ", grade1Avrg)
print("Grade 2 class average: ", grade2Avrg)
print("Grade 3 class average", grade3Avrg)