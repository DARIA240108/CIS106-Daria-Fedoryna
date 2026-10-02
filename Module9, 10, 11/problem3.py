# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:28:14 2026

@author: daria
"""

def computeForecast(month, sales):
    if month == "Jan" or month == "Feb" or month == "Mar":
        forecastPercent = 0.10
    elif month == "Apr" or month == "May" or month == "Jun":
        forecastPercent = 0.15
    elif month == "Jul" or month == "Aug" or month == "Sep":
        forecastPercent = 0.20
    else:
        forecastPercent = 0.25
    nextMonthSales = sales * (1 + forecastPercent)
    return nextMonthSales
loopResponse = "y"
while loopResponse == "y":
    lastName = input("Enter last name: ")
    month = input("Enter month: ").title()
    sales = float(input("Enter sales: "))
    nextMonthSales = computeForecast(month, sales)
    print("Last name: ", lastName)
    print("Month: ", month)
    print(f"Next month sales: ${nextMonthSales:.2f}")
    loopResponse = input("Would you like to continue? y/n ")
    