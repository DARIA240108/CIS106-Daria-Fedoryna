# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:18:29 2026

@author: daria
"""

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    def bonus(self, rate):
        b = float(rate) * float(self.pay)
        return b 
empl1 = Employee('Frank', 'Alvino', 60000.00)
print(empl1.email)
print(empl1.first)
print(empl1.last)
print(empl1.pay)
print(empl1.bonus(0.10))
print(empl1.bonus(0.20))