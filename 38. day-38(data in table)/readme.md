### Day-38 (Data in table)

# 🧮 Tkinter Data Table GUI using Treeview

This Python project demonstrates how to create a **data table** using the `Treeview` widget from Tkinter’s `ttk` module.  
It displays product information in a clean tabular format with columns for **Item ID, Product Name, Price, and Stock**.

---

## 🎯 Project Overview

Have you ever wanted to create tables in Python without using Excel or web frameworks?  
Tkinter’s `Treeview` widget lets you do that easily — you can display structured data inside a GUI window like a spreadsheet.

This project is a simple example of how to:

- Create a Tkinter window
- Use `ttk.Treeview` to display tabular data
- Customize columns and headings
- Insert rows dynamically

---

## 🧩 Features

✅ Displays data in table format  
✅ Center-aligned columns  
✅ Uses sample product data  
✅ Easy to customize and extend

---

## 🧠 Code Explanation

### 1️⃣ Import Modules

```python
import tkinter as tk
from tkinter import ttk

```

2️⃣ Define Table Columns

```py
data_columns = ["Item ID","Product Name", "Price (INR)","Stock"]

sample_data = [
    (101,"Wireless Mouse",850,45),
    (102,"Mechanical Keyboard",4200,15),
    (103,"USB-C Hub",1500,70),
    (104,"Laptop Stand",990,55),
    (105,"Monitor Cable",450,120)
]
```

4️⃣ Create the GUI Window

```py
root = tk.Tk()
root.title("Data Table using Treeview")
root.geometry("800x800")


```

5️⃣ Create the Treeview Widget

```py
tree = ttk.Treeview(root, columns=data_columns, show='headings', height=10)
```

6️⃣ Configure Columns and Headings

```py

for col in data_columns:
    tree.column(col, anchor=tk.CENTER, width=120)
    tree.heading(col, text=col)
```

7️⃣ Insert Data

```py
for item in sample_data:
    tree.insert('', tk.END, values=item)
```

8️⃣ Display the Table

```py
tree.grid(row=10, column=0, sticky='nsew', padx=10)

```

9️⃣ Run the Application

```py
root.mainloop()
```

🚀 How to Run

1. Save the code as main.py

2. Run it in terminal or VS Code:

3. py main.py

**_Note_**

I created learn project from mySirg Channel,

vidio link : https://youtu.be/YP7xDYrgUr0?si=xR2kKRWcR-wIrgqO
