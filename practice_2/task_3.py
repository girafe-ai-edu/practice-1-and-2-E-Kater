# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. 
The user must enter their height and weight, after which you use one of the formulas below to determine the index.
BMI = weight/height**2 
Assumption: weight and height should be in kg and sm => we can read them as integer
"""
weight = int(input())
height = int(input())

print((weight  / height**2))

#code here

