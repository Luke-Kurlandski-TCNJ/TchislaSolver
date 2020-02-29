#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Luke Kurlandski
February 2020
Tchisla Solver Run File

User runs to solve a Tchisla puzzle.
"""

import tchisla

print("\nWelcome to Tchisla Solver! Enter \"Q\" to Quit.\n")
while(True):
    print("Enter the number to find:", end="")
    i = input()
    if i == "Q":
        break
    TARGET = int(i)
    print("Now enter a number to use:", end="")
    i = input()
    if i == "Q":
        break
    USE = int(i)
    print("\nSolving.....")
    tchisla.calculate(TARGET, USE)
print("\nHope you enjoyed cheating at Tchisla!")

