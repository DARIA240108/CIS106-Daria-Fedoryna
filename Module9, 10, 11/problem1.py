# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 09:45:19 2026

@author: daria
"""

def computeTotal(qty, price):
    total = qty * price
    if total > 10000:
        discount = total * 0.10
        total = total - discount
        return total
totalExtPrice = 0
loopResponse = "y"

while loopResponse == "y":
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    extendedPrice = computeTotal(qty, price)
    print("Quantity: ", qty)
    print(f"Price: ${price:.2f}")
    print(f"Extended price : ${extendedPrice:.2f}")
    totalExtPrice = totalExtPrice + extendedPrice
    loopResponse = input("Would you like to continue? y/n: ")
    
print(f"Total extended price: ${totalExtPrice:.2f}" )

        
    