#Imports the gui to create the calculator
import tkinter as tk

calculation = ""

#add the number in the textbox
def add_calculator(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

#Calculates the string
def evaluate_calculator():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_calculator()
        text_result.insert(1.0, "Error")
        pass

#clear button
def clear_calculator():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
    pass

#Creates the calculator
root = tk.Tk()
root.geometry("300x275")

#Top textbox of the calculator
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

#Creates every button for the calculator
#
btn_1 = tk.Button(root, text="1", command=lambda: add_calculator(1), width=5, font =("Arial", 14))
btn_1.grid(column=1, row=2)
btn_2 = tk.Button(root, text="2", command=lambda: add_calculator(2), width=5, font =("Arial", 14))
btn_2.grid(column=2, row=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_calculator(3), width=5, font =("Arial", 14))
btn_3.grid(column=3, row=2)
btn_4 = tk.Button(root, text="4", command=lambda: add_calculator(4), width=5, font =("Arial", 14))
btn_4.grid(column=1, row=3)
btn_5 = tk.Button(root, text="5", command=lambda: add_calculator(5), width=5, font =("Arial", 14))
btn_5.grid(column=2, row=3)
btn_6 = tk.Button(root, text="6", command=lambda: add_calculator(6), width=5, font =("Arial", 14))
btn_6.grid(column=3, row=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_calculator(7), width=5, font =("Arial", 14))
btn_7.grid(column=1, row=4)
btn_8 = tk.Button(root, text="8", command=lambda: add_calculator(8), width=5, font =("Arial", 14))
btn_8.grid(column=2, row=4)
btn_9 = tk.Button(root, text="9", command=lambda: add_calculator(9), width=5, font =("Arial", 14))
btn_9.grid(column=3, row=4)
btn_0 = tk.Button(root, text="0", command=lambda: add_calculator(0), width=5, font =("Arial", 14))
btn_0.grid(column=2, row=5)
btn_plus = tk.Button(root, text="+", command=lambda: add_calculator("+"), width=5, font =("Arial", 14))
btn_plus.grid(column=4, row=2)
btn_minus = tk.Button(root, text="-", command=lambda: add_calculator("-"), width=5, font =("Arial", 14))
btn_minus.grid(column=4, row=3)
btn_mul = tk.Button(root, text="*", command=lambda: add_calculator("*"), width=5, font =("Arial", 14))
btn_mul.grid(column=4, row=4)
btn_div = tk.Button(root, text="/", command=lambda: add_calculator("/"), width=5, font =("Arial", 14))
btn_div.grid(column=4, row=5)
btn_open = tk.Button(root, text="(", command=lambda: add_calculator("("), width=5, font =("Arial", 14))
btn_open.grid(column=1, row=5)
btn_close = tk.Button(root, text=")", command=lambda: add_calculator(")"), width=5, font =("Arial", 14))
btn_close.grid(column=3, row=5)

#calls function dont use lambda
btn_equals = tk.Button(root, text="=", command= evaluate_calculator, width=11, font =("Arial", 14))
btn_equals.grid(column=3, row=6, columnspan=2)
btn_clear = tk.Button(root, text="C", command= clear_calculator, width=11, font =("Arial", 14))
btn_clear.grid(column=1, row=6, columnspan=2)


root.mainloop()