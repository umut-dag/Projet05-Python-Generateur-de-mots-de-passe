import string
from random import choice
from tkinter import *

#######################################################

def generator_password():

    # Initialisation des variables
    all_chars = ""
    password = ""

    # Efface le mot de passe affiché
    output.delete(0, END)

    # Récupère la longueur du mot de passe souhaitée
    password_lenght = int(lenght.get())

    if password_lenght > 26:
        # Lenght
        lenght.delete(0, END)
        lenght.insert(0, "26")  # Default length
        password_lenght = int(lenght.get())

    if majuscules.get() == False and minuscules.get() == False and chiffres.get() == False and symboles.get() == False:
        majuscules.set(True)
        minuscules.set(True)

    if majuscules.get() == True:
        # upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # uall_chars += upper
        all_chars += string.ascii_uppercase

    if minuscules.get() == True:
        # lower = "abcdefghijklmnopqrstuvwxyz"
        all_chars += string.ascii_lowercase

    if chiffres.get() == True:
        # numbers = "0123456789"
        all_chars += string.digits

    if symboles.get() == True:
        # symbols = "[]{}()*:;/_-"
        all_chars += string.punctuation

    # Le souci avec Sample : ValueError: Sample larger than population or is negative
    # Si on choisi slt les chiffres + longueur = 12 = impossible car il y a slt 10 chiffres uniques (0-9)
    # password = "".join(random.sample(all_chars, password_lenght))
    password = "".join(choice(all_chars) for x in range(password_lenght))

    # On insère le résultat dans output
    output.insert(0, password)

#######################################################

# Création d'une fenêtre
window = Tk()

# Personnaliser la fenêtre
window.title("Générateur de mot de passe")
window.geometry("550x500")
window.config(background="#4065A4")

# Création d'une frame, pour centrer le tout
frame = Frame(window, bg="#4065A4")

#######################################################

# Titre
Label(frame, text="Générateur de mots de passe en Python", font=("Helvetica 18 bold"), bg="#4065A4",
                     fg="white").grid(row=0, columnspan=2, pady=15, sticky='ew')

# Output
output = Entry(frame, text="En attente ...", font=("Helvetica 17 bold"), bg="#4065A4", fg="white", justify="center")
output.grid(row=1, columnspan=2, padx=20, pady=5, sticky='ew')
output.insert(0, "En attente ...")
#######################################################

# Column 0

Label(frame, text="Longueur du mot de passe", font=("Helvetica", 16), bg="#4065A4", fg="white", anchor="w").grid(row=2, column=0, padx=20, pady=3, sticky='ew')
Label(frame, text="Lettres en majuscule", font=("Helvetica", 16), bg="#4065A4", fg="white", anchor="w").grid(row=3, column=0, padx=20, pady=3, sticky='ew')
Label(frame, text="Lettres en minuscule", font=("Helvetica", 16), bg="#4065A4", fg="white", anchor="w").grid(row=4, column=0, padx=20, pady=3, sticky='ew')
Label(frame, text="Chiffres", font=("Helvetica", 16), bg="#4065A4", fg="white", anchor="w").grid(row=5, column=0, padx=20, pady=3, sticky='ew')
Label(frame, text="Symboles", font=("Helvetica", 16), bg="#4065A4", fg="white", anchor="w").grid(row=6, column=0, padx=20, pady=3, sticky='ew')


#######################################################

# Column 1

# Déclaration des variables des checkbox
majuscules = BooleanVar()
majuscules.set(True)
minuscules = BooleanVar()
minuscules.set(True)
chiffres = BooleanVar()
symboles = BooleanVar()

# Entry lenght
lenght = Entry(frame, width=5)
lenght.insert(0, "16")  # Default length
lenght.grid(row=2, column=1, pady=5)

Checkbutton(frame, text="", variable=majuscules, onvalue=True, offvalue=False).grid(row=3, column=1, pady=3)
Checkbutton(frame, text="", variable=minuscules, onvalue=True, offvalue=False).grid(row=4, column=1, pady=3)
Checkbutton(frame, text="", variable=chiffres, onvalue=True, offvalue=False).grid(row=5, column=1, pady=3)
Checkbutton(frame, text="", variable=symboles, onvalue=True, offvalue=False).grid(row=6, column=1, pady=3)

#######################################################

# Bouton GENERATOR
Button(frame, text="Générer", font=("Helvetica", 16), bg="#4065A4", fg="white" , command=generator_password).grid(row=7, columnspan=2, sticky='ew', pady=15, padx=20)

# Bouton QUITTER
Button(frame, text="Quitter", font=("Helvetica", 16), bg="#4065A4", fg="white", command=window.destroy).grid(row=8, columnspan=2, sticky='ew', padx=20)

#######################################################

frame.pack(expand=True)
window.mainloop()