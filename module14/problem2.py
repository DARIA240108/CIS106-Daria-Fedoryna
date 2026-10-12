# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:33:05 2026

@author: daria
"""

class Student:
    def __init__(self, first, last, district, credits):
        self.first = first
        self.last = last
        self.district = district
        self.credits = credits
    def tuition(self):
        if self.district == "I":
            return self.credits * 250
        else:
            return self.credits * 500
student1 = Student("Daria", "Fedoryna", "I", 12)
print(student1.tuition())