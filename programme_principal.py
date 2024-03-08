from tkinter import *
from fonction import *

try:
    n=input("Entrer le nom du  fichier à lire: ")
    print("Lecture en cours ...")
    lire_pdf(n)
except:ValueError
print("Désolé, une erreur est survenue!")