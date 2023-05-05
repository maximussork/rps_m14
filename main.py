from tkinter import *
# App main GUI
# Windows

root = Tk()
username_window = Toplevel()
rules_window = Toplevel()
highscore_window = Toplevel()
choose_game_window = Toplevel()
main_game_window = Toplevel()

#Hided Windows
root.withdraw()
rules_window.withdraw()
highscore_window.withdraw()
choose_game_window.withdraw()
main_game_window.withdraw()
#var
rock = 1
paper = 3
scis = 9

#Func
def username_button_func(): # Hides username_window and shows rules_window
    username_window.withdraw()
    rules_window.deiconify()
def rules_window_button_func(): #Hides rules_window and shows root
    rules_window.withdraw()
    rules_window.grab_release()
    root.deiconify()
def root_to_rules_window_func():
    #root.withdraw() # Quizas quitar y poner un grabset
    rules_window.deiconify()
    rules_window.grab_set()
def root_show_highscore_window_func():
    highscore_window.deiconify()
    highscore_window.grab_set()
def highscore_window_close():
    highscore_window.withdraw()
    highscore_window.grab_release()
def play():
    root.withdraw()
    choose_game_window.deiconify()
def choose():
    choose_game_window.withdraw()
    main_game_window.deiconify()
def rps():
    userinput =1
    machineinput = "random"
    sumchoice = userinput + machineinput
    if sumchoice == 2 or 6 or 18:
        print("Tie")



#username variable string
var_username = StringVar()
#
"""
Hacer que la string sea sustituida
if 1:
    var_username.set("wizard")
"""


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
    command = play
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
    text = "pla",
    font = ("Opensans 10 bold"),
    command = highscore_window_close
)
#choose_game_window
choose_game_window.geometry('200x200')
choose_game_window.title("Rock Python Scissors ")
choose_game_window_label = Label(
    choose_game_window,
    text="CHOOSE",
    font = ("Opensans 15 bold")
)
choose_game_window_button_rock = Radiobutton(
    choose_game_window,
    value= 1 ,
    text = "R",
    font = ("Opensans 10")
)
choose_game_window_button_paper = Radiobutton(
    choose_game_window,
    value= 2 ,
    text = "P",
    font = ("Opensans 10")
)
choose_game_window_button_scissors = Radiobutton(
    choose_game_window,
    value = 3,
    text = "S",
    font = ("Opensans 10")
)
choose_game_window_button_confirm = Button(
    choose_game_window,
    text = "CONFIRM",
    font = ("Opensans 15 bold"),
    command = choose
)
#main_game_window
main_game_window.geometry("400x400")
main_game_window.title("Rock Python Scissors")
main_game_window_label = Label(
    main_game_window,
    text="PLACEHOLDER COMEBACK LATER"
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
#choose_game_window_pack
choose_game_window_label.pack()
choose_game_window_button_rock.pack()
choose_game_window_button_paper.pack()
choose_game_window_button_scissors.pack()
choose_game_window_button_confirm.pack()
#main_game_window_pack
main_game_window_label.pack()
#INICIAR
root.mainloop()
