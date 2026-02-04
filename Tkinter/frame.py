from tkinter import *

root = Tk()
root.geometry("300x150")

w = Label(root, text='Chocos And IceCreams', font="50")
w.pack()

frame = Frame(root,background='blue')
frame.pack()

bottomframe = Frame(root,background="cyan")
bottomframe.pack(side=BOTTOM)

b1_button = Button(frame, text="Choco", fg="red",bg="blue")
b1_button.pack(side=LEFT)

b2_button = Button(frame, text="Dark Choco", fg="brown",bg="beige")
b2_button.pack(side=LEFT)

b3_button = Button(frame, text="White Choco", fg="blue",bg="beige")
b3_button.pack(side=LEFT)

b4_button = Button(bottomframe, text="Pastry", fg="green",bg="yellow")
b4_button.pack(side=BOTTOM)

b5_button = Button(bottomframe, text="Cake", fg="green",bg="pink")
b5_button.pack(side=BOTTOM)

b6_button = Button(bottomframe, text="Tiramisu", fg="green",bg="cyan")
b6_button.pack(side=BOTTOM)

root.mainloop()

# from tkinter import *

# # create a root window.
# top = Tk()
# top.title("My favorite Dishes")
# # create listbox object
# listbox = Listbox(top, height=10,
#                   width=15,
#                   bg="grey",
#                   activestyle='dotbox',
#                   font="Helvetica",
#                   fg="yellow")

# # Define the size of the window.
# top.geometry("300x250")

# # Define a label for the list.
# label = Label(top, text=" FOOD ITEMS")

# # insert elements by their
# # index and names.
# listbox.insert(1, "Nachos")
# listbox.insert(2, "Sandwich")
# listbox.insert(3, "Burger")
# listbox.insert(4, "Pizza")
# listbox.insert(5, "Burrito")
# listbox.delete(3)
# # pack the widgets
# label.pack()
# listbox.pack()
# # Display untill User
# # exits themselves.
# top.mainloop()


from tkinter import *

root = Tk()
root.geometry("150x200")

w = Label(root, text='HelloHello',
          font="50")

w.pack()

scroll_bar = Scrollbar(root)

scroll_bar.pack(side=RIGHT,
                fill=Y)

mylist = Listbox(root,
                 yscrollcommand=scroll_bar.set)

for line in range(1, 26):
    mylist.insert(END, "Hi " + str(line))

mylist.pack(side=LEFT, fill=BOTH)

scroll_bar.config(command=mylist.yview)

root.mainloop()


