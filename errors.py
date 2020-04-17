#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Luke Kurlandski
February 2020
Tchisla Solver Exceptions

Contains basic exceptions that may occur during the course of solving Tchisla.
"""

class NumberError(Exception):
    """
    Exception thrown for results that are defined as not permitted.
    """
    
    pass

class TargetFound(Exception):
    """
    Exception thrown when the target number is found.
    """
    
    def __init__(self, target, path, uses):
        self.target = target
        self.path = path
        self.uses = uses