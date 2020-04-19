#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 07:05:13 2020

@author: luke
"""

import tkinter as tk
import threading
import time
from PIL import Image, ImageTk

import configs
import tchisla

def graphic_display():
    """
    Display a Tchisla image for a finit period of time.
    """
    
    img = Image.open("Tchisla.png")
    img = ImageTk.PhotoImage(img)
    lbl_img = tk.Label(root, image=img)
    lbl_img.pack(fill=tk.BOTH)
    return lbl_img, img

def alter_geometry(window_width=400, window_height=400, shift_x=0, shift_y=0):
    """
    Modify the geometry of the main window.
    """
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, 
            x+shift_x, y+shift_y))
    
def computational_details():
    """
    Launch a window for the user to modify the factors involved in solving.
    """
    
    def save():
        """
        Alter the contents of the configs file to user preference.
        """
        
        try:
            configs.TOO_BIG = int(float(ent_too_big.get()))
            configs.MAX_REC = int(ent_max_rec.get())
            configs.MAX_FACT = int(ent_max_fact.get())
            configs.MAX_POW = int(ent_max_pow.get())
        except Exception as e:
            popup_error = tk.Toplevel()
            popup_error.title("Error")
            tk.Label(popup, text="The following python error occurred:\n"+str(e))
            return
        popup_success = tk.Toplevel()
        popup_success.title("Success")
        t = ("New TOO_BIG: " + "{:.2E}".format(configs.TOO_BIG)
            + "\nNew MAX_REC: " + str(configs.MAX_REC)
            + "\nNew MAX_FACT: " + str(configs.MAX_FACT)
            + "\nNew MAX_POW: " + str(configs.MAX_POW))
        tk.Label(popup_success, text=t).pack()
        
    popup = tk.Toplevel()
    popup.title("Modify Computational Constants")
    general = """In this section, you may alter the constants which are 
        involved in the computational process of solving a tchisla puzzle. 
        With this power comes great responsibility. Your choices may cause the
        program to take an irrationally long amount of time to run, or may 
        cause the program to run out of memory."""
    mechanics = """First, you need to know a bit how the program works. 
        During computation, the program uses the \"use\" number and 
        mathematical operators to generate \"way-point\" numbers. These in turn
        are further combined with more mathematical operators until the 
        \"target\" number is found."""
    too_big = """If a way-point number is larger than this number, the program
        will delete it and not use it any further."""
    max_recursion = """When performing the uniary operations on a way-point
        number, the program will go no deeper than this recursive depth."""
    max_factorial = """If a way-point number is larger than this number, the
        program will not perform the factorial operation on it."""
    max_power = """If the product of two way-point numbers is greater than this
        number, the program will not perform the power operation between the 
        two numbers."""
    
    tk.Label(popup, text=general).pack()
    tk.Label(popup, text=mechanics).pack()
    
    tk.Label(popup, text=too_big).pack()
    ent_too_big = tk.Entry(popup, width=30)
    ent_too_big.insert(1, "{:.2E}".format(configs.TOO_BIG))
    ent_too_big.pack()
    
    tk.Label(popup, text=max_recursion).pack()
    ent_max_rec = tk.Entry(popup)
    ent_max_rec.insert(1, str(configs.MAX_REC))
    ent_max_rec.pack()
    
    tk.Label(popup, text=max_factorial).pack()
    ent_max_fact = tk.Entry(popup)
    ent_max_fact.insert(1, str(configs.MAX_FACT))
    ent_max_fact.pack()
    
    tk.Label(popup, text=max_power).pack()
    ent_max_pow = tk.Entry(popup)
    ent_max_pow.insert(1, str(configs.MAX_POW))
    ent_max_pow.pack()
    
    tk.Button(popup, text="Save Configurations", command=save).pack()
    popup.mainloop()

def compute(ent_nums, ent_use):
    """
    Perform the computation to find the target number.
    """
    
    nums = ent_nums.get().strip()
    nums = nums.split(",")
    use = int(ent_use.get())
    
    popup = tk.Toplevel()
    popup.title("Results")
    text = tk.Text(popup)
    text.pack(fill=tk.BOTH)
    
    for target in nums:
        uses, path = tchisla.calculate(target, use)
        text.insert(tk.END, str(target) + " = " + path + "  //" + uses + " uses\n")
    
def startup():
    """
    Launch the start up sequence.
    """
    
    alter_geometry(246, 246)
    root.title("...Launching...")
    return graphic_display()
    
def runtime():
    """
    Perform these actionas during runtime.
    """
    
    root.title("Tchisla Solver")
    alter_geometry(260, 500)
    
    tk.Label(root, text="Welcome to Tchisla Solver").pack()
    
    tk.Label(root, text="Enter one target number or"
             + "\ncomma-separated numbers to compute.").pack()
    ent_nums = tk.Entry(root)
    ent_nums.pack()
    
    tk.Label(root, text="Enter a number to use.").pack()
    ent_use = tk.Entry(root)
    ent_use.pack()
    
    tk.Label(root, text="Click below to customize computation."
             + "\n(Nerds Only)").pack()
    tk.Button(root, text="Computational Factors", 
              command=computational_details).pack()
    
    tk.Label(root, text="Click to start.").pack()
    tk.Button(root, text="Compute", 
              command=lambda:compute(ent_nums, ent_use)).pack()
    
root = tk.Tk()
lbl_img, img = startup()
root.after(1000, runtime)
root.mainloop()