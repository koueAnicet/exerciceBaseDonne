from tkinter import * 
from tkinter.ttk import *
  
# créer une fenêtre tkinter
gui = Tk() 
  
# Ajout de widgets à la fenêtre
Label(gui, text='Setting', font=('Verdana', 15)).pack(side=TOP, pady=10) 
  
# Créer un objet photoimage pour utiliser l'image
photo = PhotoImage(file = r"C:\Users\WTLX\Desktop\icon.png") 
# Ajouter l'image dans le bouton 
Button(gui, image=photo).pack(side=TOP) 
  
mainloop()