import tkinter as tk
from tkinter import ttk

def convert_length(val, unit):
    if unit == 'meters':
        return val * 100  # to centimeters
    elif unit == 'centimeters':
        return val / 100  # to meters
    elif unit == 'feet':
        return val * 30.48  # to centimeters
    elif unit == 'inches':
        return val * 2.54  # to centimeters
    else:
        return val

def convert(t1, selected_unit, l1):
    try:
        result = convert_length(float(t1.get()), selected_unit.get())
        l1.config(text=f"Converted value: {result:.2f}")
    except ValueError:
        l1.config(text="Enter a valid number")

def main():
    root = tk.Tk()
    root.geometry("400x400")

    t1 = ttk.Entry(root, width=20, font=('Arial', 20))
    units = ['meters', 'centimeters', 'feet', 'inches']
    selected_unit = tk.StringVar()
    cb1 = ttk.Combobox(root, textvariable=selected_unit, values=units, font=('Arial', 20))
    cb1.set(units[0])

    l1 = tk.Label(root, text='', font=('Arial', 20))

    b1 = tk.Button(root, text='Convert', font=('Arial', 20), command=lambda: convert(t1, selected_unit, l1))

    t1.pack(padx=10, pady=10)
    cb1.pack(padx=10, pady=10)
    b1.pack(padx=10, pady=10)
    l1.pack(padx=10, pady=10)

    root.mainloop()

if __name__ == '__main__':
    main()
