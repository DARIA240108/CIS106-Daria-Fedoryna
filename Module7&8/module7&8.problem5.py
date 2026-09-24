# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 19:02:58 2026

@author: daria
"""

file = open("students.txt", "r")
totalTuition = 0
studentCount = 0
lastName = file.readline().strip()

while lastName != "":
    districtCode = file.readline().strip()
    credits = int(file.readline())
    
    if districtCode == "I":
        tuition = credits * 250
    else:
        tuition = credits * 500
    print("Last name: ", lastName)
    print("Credits taken: ", credits)
    print("Tuition owed: ", tuition)
    print()
    totalTuition = totalTuition + tuition
    studentCount = studentCount + 1
    lastName = file.readline().strip()
file.close()
print("Total tuition owed: ", totalTuition)
print("Number of students: ", studentCount)
        