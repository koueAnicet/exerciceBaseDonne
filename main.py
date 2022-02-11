from tkinter import*
import sqlite3
from tkinter import messagebox
import re #module de verification email

import hashlib #module d'harchage

#installation de environement virtuel:python3  -m venv venv et son activation source venv venv
#les caracteres de verifcation de mot de passe
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

fenetre= Tk()
fenetre.title("Interface(Inscription/Connnexion)")
fenetre.configure()



frame = Frame(fenetre, width=600 , height=900, highlightcolor="red",highlightbackground='blue', highlightthickness=3,bg="lightblue")
frame.pack(expand=0, pady=300)

label1 = Label(frame, text="Nom", width=50, bg="red")
label1.pack(ipady=3, pady=10)
entryNom=Entry(frame, width=50, borderwidth=4)
entryNom.pack()



label2 = Label(frame, text="Prenom", width=50, bg="red")
label2.pack(ipady=3, pady=10)
entryPrenom=Entry(frame, width=50, borderwidth=4)
entryPrenom.pack()


label3 = Label(frame, text="Email", width=50, bg="red")
label3.pack(ipady=3, pady=10)
entryEmail=Entry(frame, width=50, borderwidth=4)
entryEmail.pack()

label4 = Label(frame, text="mot de passe", width=50, bg="red", )
label4.pack(ipady=3, pady=10)
entryPassWord=Entry(frame, width=50, borderwidth=4,show='*')
entryPassWord.pack()

label5 = Label(frame, text="Confirme mot de passe", width=50, bg="red")
label5.pack(ipady=3, pady=10)
entryConfirmPassWord=Entry(frame, width=50, borderwidth=4, show='*')
entryConfirmPassWord.pack()

#encodage
hash_mdp = entryConfirmPassWord.get().encode()

# instancier l'objet sha3_256 
d = hashlib.sha3_256(hash_mdp)

#impression(hachage) 
hachage = d.hexdigest() 

print(hachage)
#def connexion():
 #  pass

def inscription():
    
    d={
        "nom": entryNom.get(),
        "prenom": entryPrenom.get(),
        "email": entryEmail.get(),
        "mdp": hachage
    }
    if entryNom.get()=="" and entryPrenom.get()=="" and entryEmail.get()=="" and entryPassWord.get()=="" and entryConfirmPassWord.get()=="":
        messagebox.showerror("error","Remplissez tous les champs!")
    elif entryEmail.get().isspace():
        if entryPassWord.get().isspace():
            if entryConfirmPassWord.get().isspace():   
                messagebox.showerror('error',"pas d'espacement!")
    
    elif entryPassWord.get() != entryConfirmPassWord.get():
        messagebox.showerror('error',"mot de pass n'est pas identique!")
    

    #----------verificationde email------------
    if(re.search(regex,entryEmail.get())):
        messagebox.showinfo("validEmail","Inscription reusie!")
        
        #-------------connexion a la base de donnees---------------
        conn = sqlite3.connect("database.db")
        
        c = conn.cursor()
        
        #--------------creation de la table dans la base de donnees---------
        c.execute("""CREATE TABLE IF NOT EXISTS inscription(
            nom text,
            prenom text,
            email text,
            mdp integer
        )""")


        #--------enregistrement des element dans la base de donnees---------- 
        c.execute("INSERT INTO inscription VALUES(:nom, :prenom, :email, :mdp)", d)
        
        #---------ajout dans la base de donnees-----
        conn.commit()
        conn.close()
        #--------fermer une frame------
        frame.pack_forget()
        #callable(fenetre) #appeler dand sla meme fonction
        frame1 = Frame(fenetre, width=600 , height=900, highlightcolor="red",highlightbackground='blue', highlightthickness=3,bg="lightblue")
        frame1.pack(expand=0, pady=200)

        lab1 = Label(frame1, text="Email", width=50, bg="red")
        lab1.pack(ipady=3, pady=10)

        entryEmailConnexion=Entry(frame1, width=50, borderwidth=4)
        entryEmailConnexion.pack()

        label2 = Label(frame1, text="Mot de passe", width=50, bg="red")
        label2.pack(ipady=3, pady=10)
        entryPassWordConnexion=Entry(frame1, width=50, borderwidth=4)
        entryPassWordConnexion.pack()
        
        
        entryEmailConnexion.delete(0, END)
        entryPassWordConnexion.delete(0, END)
        Button(frame1, text="Se connecter", width=30,).pack(pady= 10,ipady=3)
    else:  
        messagebox.showerror('error',"Email Invalide!")
        #frame.destroy()
    
        
    # if conn.commit()!=0:
        
    #     frame.pack_forget()
    #     #callable(fenetre) #appeler dand sla meme fonction
    #     frame1 = Frame(fenetre, width=600 , height=900, highlightcolor="red",highlightbackground='blue', highlightthickness=3,bg="lightblue")
    #     frame1.pack(expand=0, pady=200)
    #     lab1 = Label(frame1, text="Email", width=50, bg="red")
    #     lab1.pack(ipady=3, pady=10)
    #     entryEmailConnexion=Entry(frame1, width=50, borderwidth=4)
    #      .pack()
    #     label2 = Label(frame1, text="Mot de passe", width=50, bg="red")
    #     label2.pack(ipady=3, pady=10)
    #     entryPassWordConnexion=Entry(frame1, width=50, borderwidth=4).pack()

    #Button(frame, text="Se connecter", width=30,).pack(pady= 10,ipady=3)
    entryNom.delete(0, END)
    entryPrenom.delete(0, END)
    entryEmail.delete(0, END)
    entryPassWord.delete(0, END)
    entryConfirmPassWord.delete(0, END)
Button(frame, text="S'insrire", width=30, command=inscription).pack(pady= 10,ipady=3)
fenetre.mainloop()