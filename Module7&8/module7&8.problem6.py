# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 19:13:16 2026

@author: daria
"""

response = input("Do you want to enter data? Yes or No: ")
count = 0
while response.lower() == "yes":
    lastName = input("Enter last name: ")
    exam1 = float(input("Enter first exam score: "))
    exam2 = float(input("Enter second exam score: "))
    avrg = (exam1 + exam2) / 2
    print("Last name: ", lastName)
    print(f"Average exam score:  {avrg:.2f}")
    print()
    count = count + 1
    response = input("Do you want to enter another data? yes or no: ")
print("Number of students: ", count)
