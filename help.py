# Python3 program to get selected
# value(s) from tkinter listbox
from tkinter import messagebox
from tkinter import  filedialog
from tkinter import *

# Import tkinter

institut = [
    {'nom': 'alu1', 'cognom':'cog1', 'edat': 16,'imatge':'images/student1.png'},
    {'nom': 'alu2', 'cognom':'cog2', 'edat': 17,'imatge':'images/student2.png'},
    {'nom': 'alu3', 'cognom':'cog3', 'edat': 18,'imatge':'images/student3.png'}
]







####### VEURE ALUMNE ############################
def show_alumne(listboxIndex):
    # si no hi ha cap alumne seccionat
    # la mida de la tupla d'elements seleccionats és cero
    if len(listboxIndex)==0:
        messagebox.showerror(title='Error', message='No hi ha cap alumne seleccionat')
        return

    w = Toplevel(root)
    w.grab_set()
    w.title('Show alumne')
    w.geometry('500x400')


    alumne = get_alumne_by_selected_item_from_listbox(listboxInstitut)



    # Sub funcio
    # Posar foto quan es fa click sobre el Label
    # Atenció als paràmetres:
    # - event es obligatori: no el fem servir
    # - rute foto: es rep des de Bind
    def poner_foto(event, ruta_foto):
        photo = PhotoImage(file=ruta_foto)
        #alumne = get_alumne_from_institut(COMO PASAR EL NOM)
        # Update the label's image attribute
        labelFoto.config(image=photo)
        labelFoto.image = photo


    # posem per exmeple els Labels amb les dades de l'alumne amb font Arial 14
    Label(w, text='Nom',font=('Arial 14')).place(x=50,y=50)
    Label(w, text=alumne['nom']).place(x=150, y=50)

    Label(w, text='Cognom',font=('Arial 14')).place(x=50,y=100)
    Label(w, text=alumne['cognom']).place(x=150, y=100)


    Label(w, text='Edat',font=('Arial 14')).place(x=50,y=150)
    Label(w, text=alumne['edat'] ).place(x=150, y=150)

    # es defineix el lable on posarem la foto d'un alummne
    labelFoto = Label(w, text='veure foto\nFes clic', bg='#FF0000', cursor="hand2")
    labelFoto.name = 'Label ALUMNE'
    labelFoto.place(x=250, y=50)

    # Aquesta és la part fonamental:
    # - sempre ha de ser xxxx.bind <Button-1> (butó esquerra del mouse
    # - lambda event: obligatori sempre
    # - el segon paràmetre és el que volem passara a la subfunciṕp poner_foto(event, ruta_foto)
    labelFoto.bind("<Button-1>", lambda  event, ruta_foto=alumne['imatge']: poner_foto(event,ruta_foto))


####### ADD ALUMNE ############################

# mostra el panell de afegir alumne
def show_add_alumne_form():
    # subfunció que recull les dades dels StirgVars dels Entry
    # i l'afageix a l'insitut i al listbox
    def add_alumne():
        # es recullen les dades dels strVars (variables String)
        # que corresponen a les etiquetes
        nom = nomStrVar.get()
        cog = cognomStrVar.get()
        edat = edatStrVar.get()
        imatge = imatgeStrVar.get()

        # es crea un diccionari
        alu = {'nom': nom,
               'cognom': cog,
               'edat':edat,
               'imatge':imatge
               }
        # s'afegeix el diccionari al llistat de diccionaris  (a l'insititut)
        institut.append(alu)
        # s'afegeix el nom de l'alumne al listbox amb la resta de noms d'alumnes
        # s'afegeix al principi
        listboxInstitut.insert(0,alu['nom'])

        # finalment es tanca la finestra w , no la root perquè estem a w
        w.destroy()

    # subfunció per obrir la foto de l'alumne
    # i posar-la al camp imatge
    def open_foto():
        # a askopenfilename se¡l passa amb initialdir el directori des d'in es vol obrir
        # el diàleg. En aquest cas 'images'
        filename = filedialog.askopenfilename(initialdir='images')  # show an "Open" dialog box and return the path to the selected file
        # es posa el nom de l'arxiu escollit no directament al Entry
        # sinó al StringVar que controla el seu text, és a dir a imatgeStrVar
        imatgeStrVar.set(filename)


    # interfície principal del panell.

    # es crea un panel (un TopLevel
    w = Toplevel(root)
    w.title('Add alumne')
    w.geometry('300x200')


    # es fa modal de forma que tingui el focus del ratolí fins que no es tanqui
    w.grab_set()

    # aquestes variables de tipus StringVar són les que recolliran les dades de les entrades de text que
    # es defineixen mes abaix.
    # Cadascuna és per una de les dades dle diccionari que representa un alumne: nom, cognom, edat, imatge
    nomStrVar = StringVar(w)
    cognomStrVar = StringVar(w)
    edatStrVar = StringVar(w)
    imatgeStrVar = StringVar(w)

    # Labels + Entry (entrades de text) per  nom, cognom, edat, imatge
    # cada Entry té associada una variable de tipus StrVar que és la equ recollirá el text

    # nom:
    Label(w, text='Nom').grid( row=0,column=0,)
    Entry(w, textvariable=nomStrVar).grid(row=0,column=1)

    # cognom
    Label(w, text='Cognom').grid(row=1, column=0)
    Entry(w,textvariable=cognomStrVar).grid(row=1,column=1)

    # edat
    Label(w, text='Edat').grid(row=2, column=0, )
    Entry(w, textvariable=edatStrVar).grid(row=2, column=1)

    # foto
    Button(w,text="Arxiu d'imatge",command=open_foto).grid(row=3, column=0)
    Entry(w, textvariable=imatgeStrVar).grid(row=3, column=1)


    # botó Add
    Button(w, text='Add', command=add_alumne).grid(column=0, row=6)



####### DELETE ALUMNE ############################

# Esborra un alumne
# mostra un diàleg demanant si s'estar segur de voler esborrar l'alumne
# en cas que sí:
#   esobrra l'alumne de les dades. És a dir l'esborra de l'institut
# en case que NO
#   tanca la finestra i retorna al pare

def show_delete_alumne():
    # es crea un panel (un TopLevel
    w = Toplevel(root)
    w.title('Delete  alumne')
    w.geometry('300x200')

    # es fa modal de forma que tingui el focus del ratolí fins que no es tanqui
    w.grab_set()
    resposta = messagebox.askyesno('Esborrar','Estàs segur/a ?')
    print(resposta) # fem un print de la resposta per esbrinar quin tipus de dades és
    if resposta == True:
        # elimina l'alumne del institut
        # obté l'alumne seleccionat al listbox
        alumne = get_alumne_by_selected_item_from_listbox(listboxInstitut)

        # elimina l'amne de l'institut
        institut.remove(alumne)
        print(institut)
        # elimina l'element selecctionat del listbox que representa l'institut
        listboxInstitut.delete(ACTIVE)






####### FUNCIONS UTILS ##################

# mostrar l'element seleccionat d'un listbox
def print_selected_item():
    # Traverse the tuple returned by
    # curselection method and print
    # corresponding value(s) in the listbox
    for i in listboxInstitut.curselection():
        print(listboxInstitut.get(i))
        print(institut[i])

# obtenir un alunmne sencer des del institut a partir d'un nom
# institut és una llista de diccionaris
# cada diccionari té les dades d'un únic alumne
def get_alumne_by_nom(nom):
    for alumne in institut:
        print(alumne)
        if alumne['nom'] == nom:
            return alumne

# obtenir un alunmne a part listbox del element seleccionatdel listbox de l'institut
# cal passar un listbox (el de l'institut)
def get_alumne_by_selected_item_from_listbox(listbox):
    # s'agafa la selecció actual
    listboxIndex = listbox.curselection()
    # s'obté el nom de la selecció actual
    nom_selected = listbox.get(listboxIndex)
    # es crida a obtenir per nom un alumne de l'insitut
    # se crida a la funció get_alumne_by_nom() amb el nom obtingut
    return  get_alumne_by_nom(nom_selected)



# Tanca l'aplicació completement
# s'ha de cridar a destroy sobre l'element arrel de l'aplicació --> root
def sortir_aplicacio():
    root.destroy()

##### PANEL PRINCIPAL ################

# Apliació principal
root = Tk()
root.geometry('400x400')


# Posar un marc (decoració visual)
# com que volem un marc extern per agrupar visualment els elements, els afegim a al marc extern i no pas al root
# ja que els elements pengen del marcExtern

marcExternFrame =Frame(root, width=350, height=300, relief='solid', borderwidth=1).place(x=5, y=5)
# Crea Label
Label(marcExternFrame, text="Gestio d'alumnes", width=20).place(x=10, y=20)

# Create un listbox que contindrà el només el nom dels alumnes
listboxInstitut = Listbox(marcExternFrame, width=20, height=10, selectmode=SINGLE)
listboxInstitut.place(x=10, y=50)

# afegir alumnes al listbox
for i in range(len(institut)):
    listboxInstitut.insert(i, institut[i]['nom'])

btnAdd = Button(marcExternFrame, text='Add alumne', command=show_add_alumne_form).place(x=200, y=50)
btnView = Button(marcExternFrame, text='View alumne', command=lambda : show_alumne(listboxInstitut.curselection())).place(x=200, y =100)
btnDelete = Button(marcExternFrame, text='Delete', command=show_delete_alumne).place(x=200, y =150)
btnExit = Button(marcExternFrame, text='Exit', command=sortir_aplicacio).place(x=200, y =200)




############ COMENÇAR !! #########################################
root.mainloop()
