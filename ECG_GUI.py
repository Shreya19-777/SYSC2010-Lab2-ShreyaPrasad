#import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np


#Creating the basic GUI template
class myGUI :
    def __init__ (self) :
        self.window = tk.Tk()
        self.window.title("SYSC_2010_Lab_2")
        self.window.geometry("500x300")
        
        #Getting the first textbox
        self.label_1 = tk.Label(self.window, text="CSV File Name", font=('Arial', 10))
        self.label_1.pack(padx=10, pady=10)
        self.textbox1 = tk.Text(self.window, height=0.5, font=('Arial', 10))
        self.textbox1.pack(pady=5, padx=60)
        
        self.label2 = tk.Label(self.window, text = "X-axis Column Name", font=('Arial', 10))
        self.label2.pack()
        self.textbox2 = tk.Text(self.window, height=0.5, font=('Arial', 10))
        self.textbox2.pack(pady=5, padx=60)
        
        
        
        self.button1 = tk.Button(self.window, text="Load & Plot")
        self.button1.pack()

        
gui = myGUI()
gui.window.mainloop()



