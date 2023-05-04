from tkinter import *
# App main GUI
# Windows

root = Tk()
root.withdraw()
username_window = Toplevel()


#Func
def username_button_func():
    username_window.withdraw()
    root.deiconify()

#username
var_username = StringVar()
#
"""
Hacer que la string sea sustituida
if 1:
    var_username.set("Cojones")
"""


#Miau
#Parametros
#root
root.geometry('400x400')
root.title("Rock Python Scissors ")
root_label = Label(
    root,
    text="Rock Python Scissors",
    font = ("Opensans 25 bold")
)
root_label_username = Label(
    root,
    text="Username:",
    font = ("Opensans 20")
)
root_button = Button(
    root,
    text = "PLAY",
    font = ("Opensans 25 bold"),
)
root_user_var = Label(
    root,
    textvariable = var_username,
    font = ("Opensans 20")
)
#username_window
username_window.geometry("400x400")
username_window.title("Introduce your username")
username_window_label = Label(
    username_window,
    text="Introduce your username:"
)
username_window_entry = Entry(
    username_window,
    textvariable = var_username

)
username_window_button = Button(
    username_window,
    text= "Enter",
    font = ("Opensans 25 bold"),
    command = username_button_func
)
#Packing
root_label.pack()
root_label_username.pack()
root_user_var.pack()
root_button.pack()
username_window_label.pack()
username_window_entry.pack()
username_window_button.pack()
#INICIAR
root.mainloop()
