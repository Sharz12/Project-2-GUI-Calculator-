import tkinter as tk
import math

# Button click handler
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Clear all
def clear():
    entry.delete(0, tk.END)

# Delete last character
def delete():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

# Calculate expression
def calculate():
    try:
        expression = entry.get()
        expression = expression.replace('^', '**')
        expression = expression.replace('sin', 'math.sin')
        expression = expression.replace('cos', 'math.cos')
        expression = expression.replace('tan', 'math.tan')
        expression = expression.replace('log', 'math.log')
        expression = expression.replace('sqrt', 'math.sqrt')
        expression = expression.replace('pi', str(math.pi))
        expression = expression.replace('e', str(math.e))

        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main window
window = tk.Tk()
window.title("Colorful Scientific Calculator")
window.geometry("420x600")
window.config(bg="#1e1e1e")   # dark theme background

# Styled entry display
entry = tk.Entry(window, font=("Arial", 22, "bold"), justify="right", bg="#333333", fg="white", borderwidth=5)
entry.grid(row=0, column=0, columnspan=5, pady=10, padx=10, ipady=10)

# Button configurations (colors)
btn_color = "#4e8cff"       # blue buttons
op_color = "#ff7043"        # orange operators
sp_color = "#66bb6a"        # green functions
eq_color = "#d4af37"        # gold for '='

# All Buttons
buttons = [
    ('sin', sp_color), ('cos', sp_color), ('tan', sp_color), ('log', sp_color), ('sqrt', sp_color),
    ('pi', sp_color), ('e', sp_color), ('^', op_color), ('(', op_color), (')', op_color),
    ('7', btn_color), ('8', btn_color), ('9', btn_color), ('/', op_color), ('C', "#e53935"),
    ('4', btn_color), ('5', btn_color), ('6', btn_color), ('*', op_color), ('DEL', "#e53935"),
    ('1', btn_color), ('2', btn_color), ('3', btn_color), ('-', op_color), ('=', eq_color),
    ('0', btn_color), ('.', btn_color), ('+', op_color)
]

# Create Buttons Dynamically
row, col = 1, 0
for (button, color) in buttons:
    def action(x=button):
        if x == '=':
            calculate()
        elif x == 'C':
            clear()
        elif x == 'DEL':
            delete()
        else:
            button_click(x)

    tk.Button(
        window, text=button, command=action,
        width=7, height=3, bg=color, fg="white",
        activebackground="#222222", font=("Arial", 10, "bold")
    ).grid(row=row, column=col, padx=3, pady=3)

    col += 1
    if col > 4:
        col = 0
        row += 1

window.mainloop()
