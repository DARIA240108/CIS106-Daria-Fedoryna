# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:21:28 2026

@author: daria
"""

def computeDiscount(quantity, price, discountRate):
     totalPrice = quantity * price
     discountAmount = totalPrice * discountRate
     discountedPrice = totalPrice - discountAmount
     return discountAmount, discountedPrice
loopResponse = "y"
while loopResponse == "y":
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    discountRate = float(input("Enter discount rate: "))
    discountAmount, discountedPrice = computeDiscount(quantity, price, discountRate)
    print("Quantity:", quantity)  
    print(f"Price: ${price:.2f}")
    print(f"Discount amount: ${discountAmount:.2f}")
    print(f"Discounted price: ${discountedPrice:.2f}")
    loopResponse = input("Would you like to continue? y/n: ")