# #import tkinter as tk
# from tkinter import *
# window = Tk()
# window.title("My App")
# window.geometry("300x300")

# window.config(background="blue")

# title_label = Label(window,text="Welcome to My App1",fg="yellow",bg="black")
# title_label.pack(side="top")

# title_label2 = Label(window,text="Welcome to My App2",fg="yellow",bg="black")
# title_label2.pack(side="bottom")

# title_label3 = Label(window,text="Welcome to My App3",fg="yellow",bg="black")
# title_label3.pack(side="left")

# title_label4 = Label(window,text="Welcome to My App4",fg="yellow",bg="black")
# # title_label4.pack(side="right")

# b1 = Button(window,text="B1",fg="yellow",bg="black")
# b1.grid(row=0,column=0)

# b2 = Button(window,text="B2",fg="yellow",bg="black")
# b2.grid(row=1,column=0)

# b3 = Button(window,text="B3",fg="yellow",bg="black")
# b3.grid(row=2,column=0)

# e1 = Entry()
# e1.place(x=200,y=200)
# window.mainloop()









from tkinter import *

window = Tk()
window.title("Login Me")
window.geometry("450x300")
window.config(background="blue")

# the label for user_name
user_name = Label(window,
                  text="Username",background="yellow").place(x=40,
                                         y=60)

# the label for user_password
user_password = Label(window,
                      text="Password").place(x=40,
                                             y=100)

submit_button = Button(window,
                       text="Login").place(x=40,
                                            y=130)

user_name_input_area = Entry(window,
                             width=30).place(x=110,
                                             y=60)

user_password_entry_area = Entry(window,show='*',relief="sunken",background="red",
                                 width=30).place(x=110,
                                                 y=100)

window.mainloop()

# def add():
#     print(10+10)
# # #import everything from tkinter module
# from tkinter import *

# # create a tkinter window
# root = Tk()

# # Open window having dimension 100x100
# root.geometry('300x300')
# root.config(bg="blue")
# # Create a Button
# btn = Button(root, text='Click me !', bd='5',background="cyan",command=add)
# btn1 = Button(root, text='Click me !', bd='5',background="red",command=add)
# btn2 = Button(root, text='Click me !', bd='5',background="red",command=add)
# # Set the position of button on the window of window.
# #try side = bottom, right, left

# btn.pack(side='right')
# btn1.pack(side="right")
# btn2.pack(side="top")
# root.mainloop()