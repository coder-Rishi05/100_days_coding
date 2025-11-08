import tkinter as tk

# initailization for screen

def greet(l2,t1):
    name=t1.get()
    msg="Hello " + name + "how are you"
    l2.config(text=msg)

root = tk.Tk()
root.title("my gui application") # for title
root.geometry("600x400") #for screen w*h here *=> x
l1 = tk.Label(root,text="Enter your name : ") # create label
# l1.pack()
l1.grid(row=0,column=1) # place or size 


t1=tk.Entry(root,width=30) # placeholder
t1.grid(row=0,column=2) # placeholder size


l2 = tk.Label(root,text="Enter your name : ") # create label
# l2.pack()
l2.grid(row=2,column=1) # place or size 


b1=tk.Button(root,text="Enter", command=lambda:greet(l2,t1))
b1.grid(row=2,column=1)

root.mainloop()


# this will create a gui screen 