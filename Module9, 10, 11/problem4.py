# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:49:31 2026

@author: daria
"""

def computePrice(msrp, make, model, electric):
    if electric == "y":
        discountPercent = 0.30
    elif make == "Toyota" and model == "Rav4":
        discountPercent = 0.15
    elif make == "Honda" and model == "Accord":
        discountPercent = 0.10
    else:
        discountPercent = 0.05
    discount = msrp * discountPercent
    newmsrp = msrp - discount
    tax = newmsrp * 0.07
    total = newmsrp + tax
    return total
totalmsrp = 0
totalSales = 0
loopResponse = "y"
while loopResponse == "y":
    make = input("Enter make: ").title()
    model = input("Enter model: ").title()
    electric = input("Is the vehicle electric? y/n: ")
    msrp = float(input("Enter MSRP: "))
    total = computePrice(msrp, make, model, electric)
    print("Make: ", make)
    print("Model: ", model)
    print(f"MSRP: ${msrp:.2f}")
    print(f"Out the door price: ${total:.2f}")
    totalmsrp = totalmsrp + msrp
    totalSales = totalSales + total 
    loopResponse = input("Would you like to continue? y/n: ")
print(f"Total MSRP: ${totalmsrp:.2f}")
print(f"Total sales price: ${totalSales:.2f}")