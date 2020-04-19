"""
Luke Kurlandski
Tchisla Solver Manual Run
Spring 2020

User runs to solve a Tchisla puzzle.
"""

import tchisla

def command_line_runner():
    print("\nWelcome to Tchisla Solver! Enter \"Q\" to Quit.\n")
    while(True):
        print("Enter the number to find:")
        i = input()
        if i == "Q":
            break
        TARGET = int(i)
        print("Now enter a number to use:")
        i = input()
        if i == "Q":
            break
        USE = int(i)
        print("\nSolving.....")
        tchisla.calculate(TARGET, USE)
    print("\nHope you enjoyed cheating at Tchisla!")

def alt_runner1():
    for i in range(1, 10):
        print(tchisla.calculate(i, "100,101,102,103,104,105,106,107,108,109", 10000, 20000, 20000, 24),"\n\n\n")

def alt_runner2():
    print(tchisla.calculate(8, "100", 10000, 20000, 20000, 24))

alt_runner1()

