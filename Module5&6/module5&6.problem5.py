# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:34:29 2026

@author: daria
"""
ticketNumber = int(input("Enter number of tickets: "))

if ticketNumber >= 25:
    pricePerTicket = 50
elif ticketNumber >= 10 and ticketNumber <= 24:
    pricePerTicket = 60
elif ticketNumber >= 5 and ticketNumber <= 9:
    pricePerTicket = 70
else:
    pricePerTicket = 75
    
total = ticketNumber * pricePerTicket
print("Number of tickets: ", ticketNumber)
print(f"Price per ticket: ${pricePerTicket:.2f}")
print(f"Your total cost: ${total:.2f}")
    