import tkinter as tk
from tkinter import ttk

# --- Conversion Logic ---
def convert_value(value, category, from_unit, to_unit):
    if category == "Length":
        conversions = {
            "meters": 1.0,
            "centimeters": 0.01,
            "feet": 0.3048,
            "inches": 0.0254,
            "kilometers": 1000,
            "miles": 1609.34,
        }
        return value * (conversions[from_unit] / conversions[to_unit])

    elif category == "Weight":
        conversions = {
            "kilograms": 1.0,
            "grams": 0.001,
            "pounds": 0.453592,
            "ounces": 0.0283495,
            "tons": 1000,
        }
        return value * (conversions[from_unit] / conversions[to_unit])

    elif category == "Temperature":
        # Temperature requires a different formula
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value  # same unit

    else:
        return value


# --- Function called on Convert Button ---
def convert(t1, category_var, from_unit_var, to_unit_var, result_label):
    try:
        val = float(t1.get())
        category = category_var.get()
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()

        result = convert_value(val, category, from_unit, to_unit)
        result_label.config(text=f"{val} {from_unit} = {result:.4f} {to_unit}", fg="green")

    except ValueError:
        result_label.config(text="❌ Please enter a valid number", fg="red")


# --- Update unit options based on selected category ---
def update_units(category_var, from_cb, to_cb):
    category = category_var.get()
    if category == "Length":
        units = ["meters", "centimeters", "feet", "inches", "kilometers", "miles"]
    elif category == "Weight":
        units = ["kilograms", "grams", "pounds", "ounces", "tons"]
    elif category == "Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]
    else:
        units = []

    from_cb["values"] = units
    to_cb["values"] = units
    from_cb.set(units[0])
    to_cb.set(units[1])


# --- Main Function ---
def main():
    root = tk.Tk()
    root.title("Universal Unit Converter")
    root.geometry("500x500")
    root.resizable(False, False)

    # Title
    tk.Label(root, text="🌍 Universal Unit Converter", font=("Arial", 22, "bold"), fg="#007acc").pack(pady=10)

    # Input field
    t1 = ttk.Entry(root, width=20, font=('Arial', 18))
    t1.pack(pady=10)

    # Category Selection
    tk.Label(root, text="Select Category:", font=('Arial', 14)).pack(pady=5)
    category_var = tk.StringVar(value="Length")
    category_cb = ttk.Combobox(root, textvariable=category_var, values=["Length", "Weight", "Temperature"], font=('Arial', 14))
    category_cb.pack(pady=5)

    # Unit Selection
    from_unit_var = tk.StringVar()
    to_unit_var = tk.StringVar()

    tk.Label(root, text="From:", font=('Arial', 14)).pack()
    from_cb = ttk.Combobox(root, textvariable=from_unit_var, font=('Arial', 14))
    from_cb.pack(pady=5)

    tk.Label(root, text="To:", font=('Arial', 14)).pack()
    to_cb = ttk.Combobox(root, textvariable=to_unit_var, font=('Arial', 14))
    to_cb.pack(pady=5)

    # Set default units initially
    update_units(category_var, from_cb, to_cb)

    # Update units when category changes
    category_cb.bind("<<ComboboxSelected>>", lambda e: update_units(category_var, from_cb, to_cb))

    # Convert Button
    convert_btn = tk.Button(
        root,
        text="Convert",
        font=('Arial', 18, 'bold'),
        bg="#007acc",
        fg="white",
        activebackground="#005f99",
        relief="raised",
        command=lambda: convert(t1, category_var, from_unit_var, to_unit_var, result_label)
    )
    convert_btn.pack(pady=15)

    # Result Label
    result_label = tk.Label(root, text="", font=('Arial', 16))
    result_label.pack(pady=10)

    root.mainloop()


if __name__ == '__main__':
    main()
