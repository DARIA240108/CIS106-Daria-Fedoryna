# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:33:05 2026

@author: daria
"""
tuitionRates = {"I": 250, "O": 500, "X": 800, "G": 250}
class Student:
    def __init__(self, first, last, district, credits):
        self.first = first
        self.last = last
        self.district = district
        self.credits = credits
    def tuition(self):
       return self.credits * tuitionRates[self.district]
   
student1 = Student("Daria", "Fedoryna", "I", 12)
student2 = Student("Denys", "Grabchuk", "O", 14)
student3 = Student("Vicky", "Liush", "X", 10)
student4 = Student("Lily", "Strutynska", "G", 16)
print(student1.first, student1.last, student1.tuition())
print(student2.first, student2.last, student2.tuition())
print(student3.first, student3.last, student3.tuition())
print(student4.first, student4.last, student4.tuition())