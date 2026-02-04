# # # importing only  those functions
# # # # which are needed
# from tkinter import *
# from tkinter.ttk import *
# from time import strftime

# # creating tkinter window
# root = Tk()
# root.title('Menu Demonstration')
# root.geometry("250x250")
# root.config(bg="black")

# # Creating Menubar
# menubar = Menu(root)
# def add():
#     print(10+10)

# # ;Adding File Menu and commands
# file = Menu(menubar, tearoff=1)
# menubar.add_cascade(label='File', menu=file)
# file.add_command(label='New File', command=None)
# file.add_command(label='Open...', command=None)
# file.add_command(label='Save', command=None)
# file.add_separator()
# file.add_command(label='Exit', command=root.destroy)

# # Adding Edit Menu and commands
# edit = Menu(menubar, tearoff=0)
# menubar.add_cascade(label='Edit', menu=edit)
# edit.add_command(label='Cut', command=None)
# edit.add_command(label='Copy', command=None)
# edit.add_command(label='Paste', command=None)
# edit.add_command(label='Select All', command=None)
# edit.add_separator()
# edit.add_command(label='Find...', command=None)
# edit.add_command(label='Find again', command=None)

# # Adding Help Menu
# help_ = Menu(menubar, tearoff=0)
# menubar.add_cascade(label='Help', menu=help_)
# help_.add_command(label='Tk Help', command=None)
# help_.add_command(label='Demo', command=None)
# help_.add_separator()
# help_.add_command(label='About Tk', command=None)

# # display Menu
# root.config(menu=menubar)
# mainloop()

#importing tkinter module
# from tkinter import *
# from tkinter.ttk import *

# # creating tkinter window
# root = Tk()

# # Progress bar widget
# progress = Progressbar(root, orient=HORIZONTAL,
#                        length=300, mode='determinate')

# # Function responsible for the updation
# # of the progress bar value
# def bar():
#     import time
#     progress['value'] = 20
#     root.update_idletasks()
#     time.sleep(1)

#     progress['value'] = 40
#     root.update_idletasks()
#     time.sleep(3)

#     progress['value'] = 50
#     root.update_idletasks()
#     time.sleep(1)

#     progress['value'] = 60
#     root.update_idletasks()
#     time.sleep(1)

#     progress['value'] = 80
#     root.update_idletasks()
#     time.sleep(3)
#     progress['value'] = 100


# progress.pack(pady=10)

# # This button will initialize
# # the progress bar
# Button(root, text='Start', command=bar).pack(pady=10)

# # infinite loop
# mainloop()


from tkinter import *

master = Tk()

w = Spinbox(master, from_=0, to=100)
w.pack()

mainloop()



from tkinter import *

# create a root window.
top = Tk()
top.title("My favorite Dishes")
# create listbox object
listbox = Listbox(top, height=10,
                  width=15,
                  bg="grey",
                  activestyle='dotbox',
                  font="Helvetica",
                  fg="yellow")

# Define the size of the window.
top.geometry("300x250")

# Define a label for the list.
label = Label(top, text=" FOOD ITEMS")

# insert elements by their
# index and names.
listbox.insert(1, "Nachos")
listbox.insert(2, "Sandwich")
listbox.insert(3, "Burger")
listbox.insert(4, "Pizza")
listbox.insert(5, "Burrito")
listbox.delete(1,END)

# pack the widgets
label.pack()
listbox.pack()

# Display untill User
# exits themselves.
top.mainloop()