# importing tkinter and tkinter.ttk
#and all their functions and classes
from tkinter import * 
from tkinter.ttk import *
  
# importing askopenfile function
# from class filedialog
from tkinter.filedialog import askopenfile
  
root = Tk()
root.geometry('200x100')
  
# This function will be used to open
# file in read mode and only Python files
# will be opened
def open_file():
    file = askopenfile(mode ='r', filetypes =[('All Files', '*.*')])
    if file is not None:
        content = file.read()
        print(content)
  
btn = Button(root, text ='Open', command = lambda:open_file())
btn.pack(side = TOP, pady = 10)
  
mainloop()


# importing all files  from tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# import only asksaveasfile from filedialog
# which is used to save file in any extension
from tkinter.filedialog import asksaveasfile

root = Tk()
root.geometry('200x150')

# function to call when user press
# the save button, a filedialog will
# open and ask to save file
def save():
   files = [('All Files', '*.*'),
            ('Python Files', '*.py'),
            ('Text Document', '*.txt')]
   file = asksaveasfile(filetypes = files, defaultextension = files)


btn = ttk.Button(root, text = 'Save', command = lambda : save())

btn.pack(side = TOP, pady = 20)
messagebox.askyesno("Saving","Are you sure you want to save?")
messagebox.showinfo("Saving","Your file will be saved")
mainloop()
# 1. showinfo(): Show some relevant information to the user.
# 2. showwarning(): Display the warning to the user.
# 3. showerror(): Display the error message to the user.
# 4. askquestion(): Ask a question and the user has to answer yes or no.
# 5. askokcancel(): Confirm the user's action regarding some application activity.
# 6. askyesno(): The user can answer yes or no for some action.
# 7. askretrycancel(): Ask the user about doing a particular task again or not.
