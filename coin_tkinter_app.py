import tkinter as tk
from tkinter import ttk
from greedy_coin_algorithm import get_exact_change

def calculate_change():
    try:
        amount = float(entry_amount.get())
        change = get_exact_change(amount)
        result = "\n".join([f"{count} - {denom}" for denom, count in change.items()])
        output_label.config(text=result)
    except ValueError:
        output_label.config(text="Please enter a valid amount.")


window = tk.Tk()
window.title("Exact Change Calculator")
window.geometry("400x300")
window.resizable(False, False)
window.configure(bg="#f0f0f0")

style = ttk.Style()
style.configure("TButton", padding=10)
style.configure("TLabel")

label_amount = ttk.Label(window, text="Enter the amount in dollars:")
label_amount.pack(pady=10)

entry_amount = ttk.Entry(window, width=20)
entry_amount.pack(pady=5)

button_calculate = ttk.Button(window, text="Calculate Change", command=calculate_change)
button_calculate.pack(pady=10)

output_label = ttk.Label(window, text="", background="#f0f0f0", anchor="center")
output_label.pack(pady=20)

window.mainloop()
