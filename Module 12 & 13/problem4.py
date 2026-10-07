# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 09:54:06 2026

@author: daria
"""

student = {
    "Fedoryna": 77,
    "Grabchuk": 68,
    "Shevchuk": 99,
    "Liush": 85,
    "Strytunska": 90,
    "Popil": 63,
    "Vintoniv": 74,
    "Suleimanova": 82,
    "Boliukh": 100,
    "Smith": 65,
    }
print("Student", "Grade")
for name in student:
    print(name, student[name])
total = 0
for name in student:
    total = total + student[name]
avrg = total / len(student)
print("Class average: ", avrg)
