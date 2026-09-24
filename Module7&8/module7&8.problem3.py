# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:08:34 2026

@author: daria
"""

file = open("employees.txt", "r")
name = file.readline().strip()
totalBonus = 0

while name != "":
    salary = float(file.readline().strip())
    if salary >= 100000:
        bonusRate = 0.20
    elif salary >= 50000:
        bonusRate = 0.15
    else:
        bonusRate = 0.10
        
    bonus = salary * bonusRate
    totalBonus = totalBonus + bonus
    print("Name: ", name)
    print("Salary: ", salary)
    print("Bonus", bonus)
    print()
    
    name = file.readline().strip()
    
file.close()
print("Total bonuses", totalBonus)
  