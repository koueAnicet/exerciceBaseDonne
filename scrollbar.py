from tkinter import *
gui = Tk()
scrollbar = Scrollbar(gui)
scrollbar.pack( side = RIGHT, fill = Y )
liste = Listbox(gui, yscrollcommand = scrollbar.set )
for i in range(200):
   liste.insert(END, str(i) + " - Hello World!")
liste.pack(side = LEFT, fill = BOTH )
scrollbar.config(command = liste.yview )
gui.mainloop()