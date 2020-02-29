#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Luke Kurlandski
February 2020
Tchisla Solver Settings

Contains setting for global variables that impact solving Tchisla.
"""

# Prevent program breaking due to large factorial.
MAX_FACT = 20000 
# Prevent program breaking due to large exponentiation.
MAX_POW = 140 * 140 # prevent a^b if a*b > 140*140
# Prevent program breaking due to excessive recursion.
MAX_REC = 10000 
# Prevent program breaking by storing excessivly large numbers.
TOO_BIG = 999999999999999999999999 

# The target number to compute.
TARGET = -1
# The number to use to compute the target number.
USE = -1

# The mathematical operations that use one number.
uniary_ops = []
# The mathematical operations that use two numbers.
binary_ops = []

