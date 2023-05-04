from tkinter import *
# App main GUI
# Windows

root = Tk()
username_window = Toplevel()
rules_window = Toplevel()
highscore_window = Toplevel()
main_game_window = Toplevel()


#Hided Windows
root.withdraw()
rules_window.withdraw()
highscore_window.withdraw()



#Func
def username_button_func(): # Hides username_window and shows rules_window
    username_window.withdraw()
    rules_window.deiconify()
def rules_window_button_func(): #Hides rules_window and shows root
    rules_window.withdraw()
    root.deiconify()
def root_to_rules_window_func():
    root.withdraw() # Quizas quitar y poner un grabset
    rules_window.deiconify()
def root_show_highscore_window_func():
    highscore_window.deiconify()
    highscore_window.grab_set()
def highscore_window_close():
    highscore_window.withdraw()
    highscore_window.grab_release()


#username variable string
var_username = StringVar()
#
"""
Hacer que la string sea sustituida
if 1:
    var_username.set("wizard")
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
root_to_rules_window_button = Button(
    root,
    text = "RULES",
    font = ("Opensans 15 bold"),
    command = root_to_rules_window_func

)
root_show_highscore_window_func = Button(
    root,
    text = "HS",
    font = ("Opensans 15 bold"),
    command = root_show_highscore_window_func
)
#username_window
username_window.geometry("400x400")
username_window.title("Rock Python Scissors")
username_window_label = Label(
    username_window,
    text="Type your username:"
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
#rules_window
rules_window.geometry('400x400')
rules_window.title("Rock Python Scissors ")
rules_window_label = Label(
    rules_window,
    text="Rules",
    font = ("Opensans 25 bold")
)
rules_window_explanation = Label(
    rules_window,
    text="Esto es el piedra papel tijeras blablablaplaceholder",
    font = ("Opensans 20")
)
rules_window_button = Button(
    rules_window,
    text = "OK",
    font = ("Opensans 25 bold"),
    command = rules_window_button_func
)
# highscore_window
highscore_window.geometry('200x200')
highscore_window.title("Rock Python Scissors ")
highscore_window_label = Label(
    highscore_window,
    text="HIGHSCORE",
    font = ("Opensans 15 bold")
)
highscore_window_scores= Label(
    highscore_window,
    text="PLACEHOLDER SCORES",
    font = ("Opensans 10")
)
highscore_window_button = Button( #Puede eliminarse y esperar que el usuario cierre la pestaña de forma normal
    highscore_window,
    text = "CLOSE",
    font = ("Opensans 10 bold"),
    command = highscore_window_close
)


#Packing
#root_pack
root_label.pack()
root_label_username.pack()
root_user_var.pack()
root_button.pack()
root_to_rules_window_button.pack()
root_show_highscore_window_func.pack()
#username_pack
username_window_label.pack()
username_window_entry.pack()
username_window_button.pack()
#rules_pack
rules_window_label.pack()
rules_window_explanation.pack()
rules_window_button.pack()
#highscore_pack
highscore_window_label.pack()
highscore_window_scores.pack()
highscore_window_button.pack()
#INICIAR
root.mainloop()
