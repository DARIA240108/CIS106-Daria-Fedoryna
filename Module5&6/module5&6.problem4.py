# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:26:50 2026

@author: daria
"""

principal = float(input("Enter principal amount: "))
years = int(input("Enter year to maturity: "))

if principal > 100000 and years == 5:
    interestRate = 0.06
elif principal >= 50000 and principal <= 100000 and years == 10:
    interestRate = 0.05
elif principal >= 50000 and principal <= 100000 and years == 5:
    interestRate = 0.04
else:
    interestRate = 0.02

interest = principal *interestRate
print(f"Principal: ${principal:.2f}")
print(f"Interest rate: {interestRate * 100:.0f}%")
print(f"Interest: ${interest:.2f}")