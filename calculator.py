from tkinter import*
import tkinter as tk

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count =len(button_values)
column_count =len(button_values[0])

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"



#window

window = Tk()
window.title("Calculator")  #create a window with title "Calculator
window.resizable(False,False)

frame=tk.Frame(window)
Label=tk.Label(frame, text="0", font=("Ariel",45),background=color_black, foreground="white",anchor="e")
frame.pack()
Label.grid(row=0, column=0, columnspan=column_count,sticky="we")

for row in range(row_count):
    for column in range(column_count):
        values=button_values[row][column]
        button=tk.Button(frame, text=values, font=("Ariel",30),width=column_count-1,height=1,command=lambda values=values: button_click(values))

        button.grid(row=row+1, column=column)

        
        if values in top_symbols:
            button.config(foreground=color_black, background=color_light_gray)
        elif values in right_symbols:
            button.config(foreground=color_white, background=color_orange)
        else:
            button.config(foreground=color_white, background=color_dark_gray)

def button_click(value):
    pass
window.mainloop()
