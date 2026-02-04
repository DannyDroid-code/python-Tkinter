# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.title("Food Delivery App")
# root.geometry("600x600")
# root.configure(bg="red")

# # ---------- EMAIL ----------
# tk.Label(root, text="Email", bg="red", fg="white", font=("Arial", 12, "bold")).pack(pady=5)
# email_entry = tk.Entry(root, width=40)
# email_entry.pack(pady=5)

# # ---------- PASSWORD ----------
# tk.Label(root, text="Password", bg="red", fg="white", font=("Arial", 12, "bold")).pack(pady=5)
# password_entry = tk.Entry(root, width=40, show="*")
# password_entry.pack(pady=5)

# # ---------- FOOD DROPDOWN ----------
# tk.Label(root, text="What food would you like: Chicken sandwich, B.L.T, Veg sandwich or None?", 
#          bg="red", fg="white", wraplength=550).pack(pady=10)

# food_options = ["Chicken Sandwich", "B.L.T", "Veg Sandwich", "None"]
# food_choice = ttk.Combobox(root, values=food_options, width=30)
# food_choice.pack()

# # ---------- BEVERAGE DROPDOWN ----------
# tk.Label(root, text="What beverage would you like: Cola, Fanta, Orange Juice, Water or None?", 
#          bg="red", fg="white", wraplength=550).pack(pady=10)

# beverage_options = ["Cola", "Fanta", "Orange Juice", "Water", "None"]
# beverage_choice = ttk.Combobox(root, values=beverage_options, width=30)
# beverage_choice.pack()

# # ---------- DESSERT DROPDOWN ----------
# tk.Label(root, text="What dessert would you like: Ice Cream, Ice Lolly, Chocolate Cake or None?", 
#          bg="red", fg="white", wraplength=550).pack(pady=10)

# dessert_options = ["Ice Cream", "Ice Lolly", "Chocolate Cake", "None"]
# dessert_choice = ttk.Combobox(root, values=dessert_options, width=30)
# dessert_choice.pack()

# # ---------- SUBMIT BUTTON ----------
# submit_btn = tk.Button(root, text="Submit Order", font=("Arial", 12), width=20)
# submit_btn.pack(pady=20)

# root.mainloop()




import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Food Delivery App")
root.geometry("600x600")
root.configure(bg="red")

# ---------- EMAIL ----------
tk.Label(root, text="Email", bg="red", fg="white", font=("Arial", 12, "bold")).pack(pady=5)
email_entry = tk.Entry(root, width=40)
email_entry.pack(pady=5)

# ---------- PASSWORD ----------
tk.Label(root, text="Password", bg="red", fg="white", font=("Arial", 12, "bold")).pack(pady=5)
password_entry = tk.Entry(root, width=40, show="*")
password_entry.pack(pady=5)

# ---------- FOOD QUANTITY ----------
tk.Label(root, text="Enter quantity of food you want:", 
         bg="red", fg="white", font=("Arial", 11)).pack(pady=10)

food_qty = tk.Spinbox(root, from_=0, to=10, width=10)
food_qty.pack()

# ---------- BEVERAGE QUANTITY ----------
tk.Label(root, text="Enter quantity of beverages you want:", 
         bg="red", fg="white", font=("Arial", 11)).pack(pady=10)

bev_qty = tk.Spinbox(root, from_=0, to=10, width=10)
bev_qty.pack()

# ---------- DESSERT QUANTITY ----------
tk.Label(root, text="Enter quantity of desserts you want:", 
         bg="red", fg="white", font=("Arial", 11)).pack(pady=10)

dessert_qty = tk.Spinbox(root, from_=0, to=10, width=10)
dessert_qty.pack()

# ---------- SUBMIT BUTTON ----------
submit_btn = tk.Button(root, text="Submit Order", font=("Arial", 12), width=20)
submit_btn.pack(pady=20)

root.mainloop()
