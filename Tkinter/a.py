from tkinter import *

window = Tk()
window.title("My App")
window.geometry("500x500")


lbl = Label(text="My App", fg="white", bg="#5F0707", height=5, width=100)
lbl.pack()

lbl2 = Label(text="Welcome to my App", fg="white", bg="#65B8F0", height=5, width=100)
lbl2.pack()

btn = Button(text="Welcome to my App", fg="white", bg="#65B8F0", height=5, width=20)
btn.pack()
window.mainloop()