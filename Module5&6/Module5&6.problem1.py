# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:07:20 2026

@author: daria
"""

qnt = int(input("Enter quantity: "))
if qnt >= 1000:
    unitPrice = 3.00
else: 
    unitPrice = 5.00
    
extPrice = qnt * unitPrice 
tax = extPrice * 0.07
total = extPrice + tax
print(f"Quantity :  {qnt}")
print(f"Unit Price:  ${unitPrice:,.2f}")
print(f"Tax:   ${tax:,.2f}")
print(f"Total:  ${total:,.2f}")