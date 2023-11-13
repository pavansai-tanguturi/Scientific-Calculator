import tkinter as tk
import math

def click(val):
    e = entry.get()
    ans=" "

    try:
        if val == "C":
            e = e[0:len(e) - 1]
            entry.delete(0, "end")
            entry.insert(0,e)
            return
        elif val == "CE":
            entry.delete(0,"end")
        elif val == "√":
            ans = math.sqrt(eval(e))
        elif val == "π":
            ans = math.pi
        elif val == "cosθ":
            ans = math.cos(math.radians(eval(e)))
        elif val == "sinθ":
            ans = math.sin(math.radians(eval(e)))
        elif val == "tanθ":
            ans = math.tan(math.radians(eval(e)))
        elif val == "2π":
            ans = 2 * math.pi
        elif val == "cosh":
            ans = math.cosh(eval(e))
        elif val == "sinh":
            ans = math.sinh(eval(e))
        elif val == "tanh":
            ans = math.tanh(eval(e))

        elif val == chr(8731):
            ans = eval(e) ** (1 / 3)

        elif val == "x\u02b8": 
            entry.insert("end", "**") 
            return

        elif val == "x\u00B3":
            ans = eval(e) ** 3

        elif val == "x\u00B2":  
            ans = eval(e) ** 2

        elif val == "In":  
            ans = math.log2(eval(e))

        elif val == "deg": 
            ans = math.degrees (eval(e))

        elif val == "rad":  
            ans = math.radians(eval(e))

        elif val == "e":  
            ans = math.e

        elif val == "log10": 
            ans = math.log10(eval(e))

        elif val == "x!":
            ans = math.factorial(eval(e))

        elif val == chr(247):  
            entry.insert("end", "/")
            return

        elif val == "=": 
            ans = eval(e)

        else: 
            entry.insert("end", val)
            return
        
        entry.delete(0,"end")
        entry.insert(0, ans)

    except SyntaxError:
        pass

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("350x650+100+100")

entry = tk.Entry(root, font=("arial", 20, "bold"), bd=10, width=20)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

button_list = [
    ["C", "CE", "√", "π"],
    ["cosθ", "sinθ", "tanθ", "+"],
    ["2π", "cosh", "tanh", "sinh"],
    ["x³", "x²", "x!", "-"],
    ["1", "2", "3", "*"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "+"],
    ["e", "0", ".", "%"],
    ["log10", "(", ")", "="]
]

for i, row in enumerate(button_list):
    for j, button_label in enumerate(row):
        button = tk.Button(root, width=6, height=3, text=button_label, font=("arial", 12, "bold"),
                            command=lambda button=button_label: click(button))
        button.grid(row=i + 1, column=j, padx=5, pady=5)

root.mainloop()