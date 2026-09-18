# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:42:52 2026

@author: daria
"""
lastName = input("Enter employee last name: ")
salary = float(input("Enter salary: "))
jobLevel = int(input("Enter job level: "))

if jobLevel >= 10:
    bonusRate = 0.25
elif jobLevel >= 5 and jobLevel <= 9:
    bonusRate = 0.20
else:
    bonusRate = 0.10
    
bonus = salary * bonusRate
print("Employee last name: ", lastName)
print(f"Bonus: ${bonus:.2f}")

