# 🎨 Tkinter Color Changer App

A simple GUI application built using **Tkinter** (Python’s built-in GUI toolkit).  
This program demonstrates basic Tkinter concepts such as creating windows, labels, buttons, and event handling using the `command` attribute.

---

## 🧠 Overview

This project lets you change the color of a label text by clicking different color buttons.  
It’s a beginner-friendly example to learn event handling and widget customization in Tkinter.

---

## 🪄 Preview

![App Screenshot](https://via.placeholder.com/400x200.png?text=Tkinter+Color+Changer+Preview)

---

## 🧰 Technologies Used

- 🐍 Python 3.x  
- 🪟 Tkinter (Standard GUI library)

---

## ⚙️ Basic Tkinter Commands Used

| Command | Description |
|----------|--------------|
| `Tk()` | Creates the main application window. |
| `Label()` | Displays text or images. |
| `Button()` | Creates clickable buttons. |
| `pack()` | Places widgets in the window. |
| `config()` | Changes widget properties dynamically. |
| `mainloop()` | Keeps the app running and listens for events. |

---

## 🧩 Code Explanation

### 1️⃣ Import Tkinter
```python
import tkinter as tk
```

### 2️⃣ Define Function to Change Text Color
```python
def setTextColor(l1, color):
    l1.config(fg=color)
```

### 3️⃣ Create Main Window and Widgets
```python
root = tk.Tk()
root.geometry("400x400")

l1 = tk.Label(root, text="Change my color", font=('Arial', 20))
l1.pack(pady=20)
```

### 4️⃣ Create Buttons with Commands
```python
b1 = tk.Button(root, text="RED", command=lambda: setTextColor(l1, 'red'))
b2 = tk.Button(root, text="BLUE", command=lambda: setTextColor(l1, 'blue'))
b3 = tk.Button(root, text="GREEN", command=lambda: setTextColor(l1, 'green'))
```

### 5️⃣ Pack Buttons
```python
b1.pack()
b2.pack()
b3.pack()
```

### 6️⃣ Run the App
```python
root.mainloop()
```

---

## 💡 Output Behavior

✅ The window opens with a label “Change my color.”  
🎨 Clicking on **RED**, **BLUE**, or **GREEN** instantly changes the label’s text color.

---

## 🚀 Run the Program

Save the code as `color_changer.py` and run:

```bash
python color_changer.py
```

Make sure Python is installed and Tkinter is available (comes built-in with Python).

---

## 🧠 Learnings

- How to create a window using `Tk()`  
- How to create buttons and labels  
- How to connect button clicks to functions using `command`  
- How to dynamically modify widget properties with `.config()`  

---

## 💡 Future Enhancements

- Add user input to choose custom colors  
- Add a background color changer  
- Add animations or hover effects for buttons  

---

By **rishi**  
A mini Tkinter project to understand the basics of Python GUI development.
