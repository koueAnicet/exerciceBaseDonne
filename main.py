from tkinter import*
import sqlite3




fenetre= Tk()
fenetre.title("Interface(Inscription/Connnexion)")
fenetre.configure()



frame = Frame(fenetre, width=600 , height=1000, highlightcolor="red",highlightbackground='blue', highlightthickness=3,bg="lightblue")
frame.pack(expand=0, pady=100)

label1 = Label(frame, text="Nom", width=50, bg="red")
label1.pack(ipady=3, pady=10)
entry1=Entry(frame, width=50, borderwidth=4).pack()

label2 = Label(frame, text="Prenom", width=50, bg="red")
label2.pack(ipady=3, pady=10)
entry2=Entry(frame, width=50, borderwidth=4).pack()

label3 = Label(frame, text="Email", width=50, bg="red")
label3.pack(ipady=3, pady=10)
entry3=Entry(frame, width=50, borderwidth=4).pack()

label4 = Label(frame, text="mot de passe", width=50, bg="red", )
label4.pack(ipady=3, pady=10)
entry4=Entry(frame, width=50, borderwidth=4,show='*').pack()

label5 = Label(frame, text="Confirme mot de passe", width=50, bg="red")
label5.pack(ipady=3, pady=10)
entry5=Entry(frame, width=50, borderwidth=4, show='*').pack()

#def connexion():
 #  pass
def inscription():
     
    
    #connexion a la base de donnees
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    #creation de la table dans la base de donnees
    c.execute("""CREATE TABLE IF NOT EXISTS inscription(
        nom text,
        prenom text,
        email text,
        mdp integer,
        confirm_mdp integer
    )""")
   
   
    #enregistrement des element dans la base de donnees 
    c.execute("INSERT INTO inscription VALUES(:nom, :prenom, :email, :mdp, :confirm_mdp)",d={
        "nom": entry1.get(),
        "prenom": entry2.get(),
        "email": entry3.get(),
        "mdp": entry4.get(),
        "confirm_mdp": entry5.get()
    })
    
    #ajout dans la base de donnees
    conn.commit()
    conn.close()
    if conn.commit()!=0:
        
        frame.pack_forget()
        #callable(fenetre) #appeler dand sla meme fonction
        frame1 = Frame(fenetre, width=600 , height=1000, highlightcolor="red",highlightbackground='blue', highlightthickness=3,bg="lightblue")
        frame1.pack(expand=0, pady=100)
        label1 = Label(frame1, text="Email", width=50, bg="red")
        label1.pack(ipady=3, pady=10)
        entry1=Entry(frame1, width=50, borderwidth=4).pack()
        label2 = Label(frame1, text="Mot de passe", width=50, bg="red")
        label2.pack(ipady=3, pady=10)
        entry2=Entry(frame1, width=50, borderwidth=4).pack()

    Button(frame1, text="Se connecter", width=30,).pack(pady= 10,ipady=3)
Button(frame, text="S'insrire", width=30, command=inscription).pack(pady= 10,ipady=3)
fenetre.mainloop()