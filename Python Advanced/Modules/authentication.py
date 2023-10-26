import tkinter as tk
from canvas import root
from helpers import clean_screen

def register(**user_data):
    pass


def render_shop_screen():
    pass


def render_login_screen():
    clean_screen()
    tk.Label(text="User Name", bd=5, width=8, height=1).grid(row=0, column=1)
    username = tk.Entry(bg='white', bd=3)
    username.grid(row=0, column=0)
    tk.Label(text="Password", bd=5, width=8, height=1).grid(row=1, column=1)
    password = tk.Entry(bg='white', bd=3)
    password.grid(row=1, column=0)
    tk.Button(root, text="Login", bg="white", fg="black", command=render_shop_screen).grid(row=2, column=0)
    tk.Button(root, text="Back", bg="white", fg="black", command=render_main_enter_screen).grid(row=3, column=0)


def render_register_screen():
    clean_screen()
    username = tk.Entry(root, bg='white', bd=5, cursor="arrow")
    username.grid(row=0, column=0)
    password = tk.Entry(root, bg='white', bd=5, cursor="arrow")
    password.grid(row=1, column=0)
    first_name = tk.Entry(root, bg='white', bd=5, cursor="arrow")
    first_name.grid(row=2, column=0)
    last_name = tk.Entry(root, bg='white', bd=5, cursor="arrow")
    last_name.grid(row=3, column=0)
    tk.Button(root,
              text="Register",
              bg='white',
              fg='black',
              command= lambda: register(
                  username= username.get(),
                  password= password.get(),
                  first_name= first_name.get(),
                  last_name= last_name.get())
              ).grid(row=4, column=0)
    tk.Button(root, text="Back", bg="white", fg="black", command=render_main_enter_screen).grid(row=5, column=0)

def render_main_enter_screen():
    clean_screen()
    tk.Button(root, text="Register", bg="black", fg="white", command=render_register_screen).grid(row=1, column=2)
    tk.Button(root, text="Login", bg="white", fg="black", command=render_login_screen).grid(row=1, column=1)
