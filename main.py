from tkinter import *
import random
"""
a = paper
b = rock
c = scissors
Use match statement:
tie = ["aa", "bb", "cc"]
win = ["ba", "ac", "cb"]
lose = ["ab", "bc", "ca"]
"""
# App main GUI
# Windows

root = Tk()
username_window = Toplevel()
rules_window = Toplevel()
highscore_window = Toplevel()
choose_game_window = Toplevel()
choose_game_window_popout = Toplevel()
main_game_window = Toplevel()
end_window_popout = Toplevel()
#Hided Windows
root.withdraw()
rules_window.withdraw()
highscore_window.withdraw()
choose_game_window.withdraw()
choose_game_window_popout.withdraw()
main_game_window.withdraw()
end_window_popout.withdraw()
#var
choose_list = ["a", "b", "c"]
radio = StringVar()
time = 0
highscore_content = []
streak = IntVar(value=0)

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
    highscore_read()
    highscore_window.deiconify()
    highscore_window.grab_set()
def highscore_window_close():
    highscore_window.withdraw()
    highscore_window.grab_release()
def choose_game_window_popout_close():
    choose_game_window_popout.grab_release()
    choose_game_window_popout.withdraw()
def play():
    root.withdraw()
    choose_game_window.deiconify()
def choose():
    value = radio.get()
    print('choose()  value:',value)
    if value not in choose_list:
        choose_game_window_popout.deiconify()
        choose_game_window_popout.grab_set()
    else:
        choose_game_window.withdraw()
        print('choose()  value:', value)
        print("choose() list", choose_list)
        if value == choose_list[0]:
            main_game_window_rock.pack()
        elif value == choose_list[1]:
            main_game_window_paper.pack()
        elif value == choose_list[2]:
            main_game_window_scis.pack()
        rps()

def choose_machine():
    machine_input = random.choice(choose_list)
    if machine_input == choose_list[0]:
        main_game_window_rock_machine.pack()
    elif machine_input == choose_list[1]:
        main_game_window_paper_machine.pack()
    elif machine_input == choose_list[2]:
        main_game_window_scis_machine.pack()
    return machine_input
def rps(): #Try match statement maybe?
    game_conditions = [["aa", "bb", "cc"], ["ba", "ac", "cb"], ["ab", "bc", "ca"]]
    user_input = radio.get()
    main_game_window.deiconify()
    sum_choice = user_input + choose_machine()
    main_game_window.after(1000, timer, time)
    print('sum_choice',sum_choice)
    if sum_choice in game_conditions[0]:
        choose_game_window.deiconify()
        highscore_write()
        print("Tie")
        streak.set(0)
    elif sum_choice in game_conditions[1]:
        choose_game_window.deiconify()
        print("Ganas")
        streak.set(streak.get()+1)
    else:
        main_game_window.withdraw()
        root.deiconify()
        highscore_write()
        print("Pierdes")
        streak.set(0)

def timer(time):
    main_game_window_timer_label["text"] = time
    if time >= 0:
        main_game_window.after(1000, timer, time+1)

def highscore_write():
    if streak.get() > 0:
        with open("highscore", "w") as f:
            f.write(str(var_username.get()) + " " + str(streak.get()) + "\n")
def highscore_read():
    with open("highscore", "r") as f:
        highscore_content = f.readlines()


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
    text=str(highscore_content[0:]),
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
    variable= radio,
    value= "a" ,
    text = "R",
    font = ("Opensans 10")
)
choose_game_window_button_paper = Radiobutton(
    choose_game_window,
    variable=radio,
    value= "b" ,
    text = "P",
    font = ("Opensans 10")
)
choose_game_window_button_scissors = Radiobutton(
    choose_game_window,
    variable=radio,
    value = "c",
    text = "Scissors",
    font = ("Opensans 10")
)
choose_game_window_button_confirm = Button(
    choose_game_window,
    text = "CONFIRM",
    font = ("Opensans 15 bold"),
    command = choose
)
#choose_game_window_popout
choose_game_window_popout.geometry("400x125")
choose_game_window_popout_label = Label(
    choose_game_window_popout,
    text = "Please choose an option"
)
choose_game_window_popout_button = Button(
    choose_game_window_popout,
    text = "OK",
    command = choose_game_window_popout_close
)
#main_game_window
main_game_window.geometry("400x400")
main_game_window.title("Rock Python Scissors")
main_game_window_label = Label(
    main_game_window,
    text="PLACEHOLDER COMEBACK LATER"
)

main_game_window_streak_label = Label(
    main_game_window,
    text="streak:",
    textvariable=streak
)

main_game_window_highscore_label = Label(
    main_game_window,
    text = "Highscore: "
)

main_game_window_currentime_label = Label( #Desde la última jugada
    main_game_window,
    text = "Placeholdertime"
)
main_game_window_totaltime_label = Label( #Desde inicio de la partida
    main_game_window,
    text = "Such time"
)

main_game_window_rock = Label(
    main_game_window,
    text= "Rock"
)
main_game_window_paper = Label(
    main_game_window,
    text = "Paper"
)
main_game_window_scis = Label(
    main_game_window,
    text = "Scissors"
)
main_game_window_rock_machine = Label(
    main_game_window,
    text= "Rock"
)
main_game_window_paper_machine = Label(
    main_game_window,
    text = "Paper"
)
main_game_window_scis_machine = Label(
    main_game_window,
    text = "Scissors"
)
main_game_window_timer_label = Label(
    main_game_window,
    text = time
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
#choose_game_window_popout_pack
choose_game_window_popout_label.pack()
choose_game_window_popout_button.pack()
#main_game_window_pack
main_game_window_label.pack()
main_game_window_streak_label.place(x= 75, y=75)
main_game_window_highscore_label.place(x= 150, y=75)
main_game_window_currentime_label.place(x= 150, y= 100)
main_game_window_totaltime_label.place(x= 175 , y=115)
main_game_window_timer_label.pack()
#INICIAR
root.mainloop()
