#import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Creating the basic GUI template
class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("SYSC 2010 Lab 2")
        self.window.geometry("520x380")

        tk.Label(self.window, text="CSV File Name", font=('Arial', 11)).pack()
        self.entry_file = tk.Entry(self.window, width=40, font=('Arial', 11))
        self.entry_file.pack(pady=4)

        tk.Label(self.window, text="X-axis Column Name", font=('Arial', 11)).pack()
        self.entry_x = tk.Entry(self.window, width=40, font=('Arial', 11))
        self.entry_x.pack(pady=4)

        tk.Label(self.window, text="Y-axis Column Name", font=('Arial', 11)).pack()
        self.entry_y = tk.Entry(self.window, width=40, font=('Arial', 11))
        self.entry_y.pack(pady=4)

        tk.Button(self.window, text="Load & Plot", font=('Arial', 11),command=self.load_and_plot,width=15).pack()

        self.window.mainloop()

    def load_and_plot(self):
        filename = self.entry_file.get().strip()
        col_x = self.entry_x.get().strip()
        col_y = self.entry_y.get().strip()

        try:
            df = pd.read_csv(filename)

            plt.plot(df[col_x], df[col_y], color='teal')
            plt.title(f"{col_y} vs {col_x}")
            plt.xlabel(col_x)
            plt.ylabel(col_y)
            plt.grid(True)
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print("Error", str(e))

if __name__ == "__main__":
    app = GUI()

