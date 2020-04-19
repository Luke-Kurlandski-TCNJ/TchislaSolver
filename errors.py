"""
Luke Kurlandski
Tchisla Solver Exceptions
Spring 2020

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