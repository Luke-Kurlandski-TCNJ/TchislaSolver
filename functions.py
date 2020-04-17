#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Luke Kurlandski
February 2020
Tchisla Solver Functions

Contains functions for computing results of mathematical operations Tchisla uses.
"""

import math
import configs
from errors import NumberError

def factorial(n):
    """
    Compute and return the factorial of n, raise NumberError as needed.
    """
    
    if n > configs.MAX_FACT or n < 3:
        raise NumberError
    r = math.factorial(n)
    if r > configs.TOO_BIG:
        raise NumberError
    return int(r)

def negation(n):
    """
    Compute and return the negation of n, raise NumberError as needed.
    """
    
    r = -1 * n
    if r > configs.TOO_BIG or r < (-1*configs.TOO_BIG):
        raise NumberError
    return int(r)

def root(n):
    """
    Compute and return the negation of n, raise NumberError as needed.
    """
    
    if  n < 2:
        raise NumberError
    r = math.sqrt(n)
    if r > configs.TOO_BIG or r < (-1*configs.TOO_BIG) or not r.is_integer():
        raise NumberError
    return int(r)

def addition(n, m):
    """
    Compute and return the sum of n and m, raise NumberError as needed.
    """
    
    r = m + n
    if r > configs.TOO_BIG or r < (-1*configs.TOO_BIG):
        raise NumberError
    return int(r)

def subtraction(n, m):
    """
    Compute and return the difference of n and m, raise NumberError as needed.
    """
    
    r = n - m
    if r > configs.TOO_BIG or r < (-1*configs.TOO_BIG):
        raise NumberError
    return int(r)

def multiplication(n, m):
    """
    Compute and return the product of n and m, raise NumberError as needed.
    """
    
    r = m * n
    if r > configs.TOO_BIG or r < (-1*configs.TOO_BIG):
        raise NumberError
    return int(r)

def division(n, m):
    """
    Compute and return the quotient of n and m, raise NumberError as needed.
    """

    if m == 0:
        raise NumberError
    r = n / m
    if r > configs.TOO_BIG or r < (-1*configs.TOO_BIG) or not r.is_integer():
        raise NumberError
    return int(r)

def exponentiation(n, m):
    """
    Compute and return n to the power of m, raise NumberError as needed.
    """
    
    if n * m > configs.MAX_POW:
        raise NumberError
    r = math.pow(n, m)
    if r > configs.TOO_BIG or r < (-1*configs.TOO_BIG) or not r.is_integer():
        raise NumberError
    return int(r)

def symbol(name):
    """
    Return the appropriate mathematical symbol for a function name.
    """

    if name == "factorial":
        return "!"
    if name == "root":
        return "sq"
    if name == "negation":
        return "-"
    if name == "addition":
        return "+"
    if name == "subtraction":
        return "-"
    if name == "multiplication":
        return "*"
    if name == "division":
        return "/"
    if name == "exponentiation":
        return "^"

# Store the permitted operations in a list.
configs.uniary_ops = [factorial, negation, root]
configs.binary_ops = [addition, subtraction, multiplication, division, exponentiation]