# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 18:48:59 2026

@author: daria
"""

file = open("items.txt", "r")
total = 0
count = 0
item = file.readline().strip()

while item != "":
    qnt = int(file.readline())
    price = float(file.readline())
    extendedPrice = qnt * price
    
    print("Item: ", item)
    print("Quantity: ", qnt)
    print("Price: ", price)
    print("Extended Price: ", extendedPrice)
    print()
    total = total + extendedPrice
    count = count + 1
    item = file.readline().strip()
file.close()

avrg = total / count
print("Total extended Prices: ", total)
print("Count of orders: ", count)
print("Average order: ", avrg)
