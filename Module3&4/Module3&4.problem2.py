# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 12:42:05 2026

@author: daria
"""

ticker = input("Enter the stock ticker symbol:  ")
shares = int(input("Enter your number of shares: "))
cost = float(input("Enter cost per share: "))
amountInvested = shares * cost
print(f"Amount invested: ${amountInvested:.2f}")