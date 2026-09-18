
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
qnt = int(input("Enter quantity of widgets: "))

if qnt > 1000:
    price = 10
elif qnt >= 5000:
    price = 20
else: 
    price = 30
    
extPrice = qnt * price 
tax = extPrice * 0.07
total = extPrice + tax 

print(f"Extended Price:  ${extPrice:.2f}")
print(f"Tax:   ${tax:.2f}")
print(f"Total:  ${total:.2f}")
    
