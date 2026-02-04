# importing whole module
from tkinter import *
from tkinter.ttk import *

# importing strftime function to
# retrieve system's time
from time import strftime
# creating tkinter window
root = Tk()
root.title('Clock')
# This function is used to
# display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font=('calibri', 40, 'bold'),
            background='orange',
            foreground='white')

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()


import tkinter as tk
from time import strftime
import random

# Function to update the time and background/foreground colors
def time():
    # Get the current time
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)

    # Change the background and foreground color periodically
    bg_colors = ['#FF6347', '#FF4500', '#FFD700', '#98FB98', '#8A2BE2', '#20B2AA', '#FF1493']
    fg_colors = ['#FFFFFF', '#000000', '#0000FF', '#FF00FF', '#00FFFF', '#FFFF00', '#FF6347']
    
    random_bg_color = random.choice(bg_colors)
    random_fg_color = random.choice(fg_colors)
    
    root.config(bg=random_bg_color)
    label.config(background=random_bg_color, foreground=random_fg_color)

    # Call the time function after 1000ms (1 second)
    label.after(1000, time)

# Set up the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")

# Set up the label for displaying the time
label = tk.Label(root, font=('calibri', 40, 'bold'))
label.pack(anchor='center')

# Call the time function to start the clock
time()

# Run the Tkinter event loop
root.mainloop()
