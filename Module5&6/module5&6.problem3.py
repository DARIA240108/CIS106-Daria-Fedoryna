# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:15:32 2026

@author: daria
"""

partNumber = input("Enter part number: ")
qnt = int(input("Enter quantity: "))

if partNumber == "10" or partNumber == "55":
    unitCost = 1.00
elif partNumber == "99":
    unitCost = 2.00
elif partNumber == "80" or partNumber == "70":
    unitCost = 3.00
else:
    unitCost = 5.00
    
total = qnt * unitCost
print("part number:  ", partNumber)
print(f"Cost per unit: ${unitCost:.2f}")
print(f"Total: ${total:.2f}")
