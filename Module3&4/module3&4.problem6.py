# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:25:41 2026

@author: daria
"""

pricePerShare = float(input("Enter price per share: "))
stockPrice = float(input("Enter stock price: "))
qntStock = int(input("Enter quantity of stock: "))
valueChange = (stockPrice - pricePerShare) * qntStock
print(f"Value change: {valueChange:.2f}")