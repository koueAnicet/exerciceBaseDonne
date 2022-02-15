from gc import callbacks
import hashlib  # module d'harchage
import re  # module de verification email
import sqlite3
from tkinter import *
from tkinter import messagebox
from turtle import bgcolor
from PIL import ImageTk,Image #pour afficher les image

#installation de environement virtuel:python3  -m venv venv et son activation source venv venv
#les caracteres de verifcation de mot de passe
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

fenetre= Tk()
fenetre.title("Interface(Inscription/Connnexion)")
fenetre.configure(bg='red' )

#execution des  fonctions des boutons 
def inscription():
    ins = Tk()
    
    
    frame = Frame(ins, width=600 , height=1000, highlightcolor="red",highlightbackground='blue', highlightthickness=3,bg="lightblue")
    frame.pack()
    
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
    
    def conditionInscription():
            #encodage
        hash_mdp = entryConfirmPassWord.get().encode()

        # instancier l'objet sha3_256 
        d = hashlib.sha3_256(hash_mdp)

        #impression(hachage) 
        hachage = d.hexdigest() 

        print(hachage)
        
        #dictionnaire de recuperation
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
        elif(re.search(regex,entryEmail.get())):
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
            
        else:  
            messagebox.showerror('error',"Email Invalide!")
            #frame.destroy()
   

        
    
    entryNom.delete(0, END)
    entryPrenom.delete(0, END)
    entryEmail.delete(0, END)
    entryPassWord.delete(0, END)
    entryConfirmPassWord.delete(0, END)
    Button(frame, text="S'insrire", width=29, command=conditionInscription, font=("Italic",15, "bold"), bg="green", fg='white').pack(pady= 10,ipady=3)


    bnn=Button(frame, text="Retour",).pack(pady= 5)

    
   
def connexion():
    conne= Tk()
    #frameFenetre.pack_forget()
    

    
    #callable(fenetre) #appeler dand sla meme fonction
    frame1 = Frame(conne, width=600 , height=900, highlightcolor="red",highlightbackground='blue', highlightthickness=3,bg="lightblue")
    frame1.pack()

    lab1 = Label(frame1, text="Email", width=50, bg="red")
    lab1.pack(ipady=3, pady=10)

    entryEmailConnexion=Entry(frame1, width=50, borderwidth=4)
    entryEmailConnexion.pack()

    label2 = Label(frame1, text="Mot de passe", width=50, bg="red")
    label2.pack(ipady=3, pady=10)
    entryPassWordConnexion=Entry(frame1, width=50, borderwidth=4)
    entryPassWordConnexion.pack()

    def conditonConnexion():
        if entryPassWordConnexion.get() and entryEmailConnexion.get():
            
            #encodage
            hash_pwd_connexion = entryPassWordConnexion.get().encode()
            # instancier l'objet sha3_256 
            donnesConnexion= hashlib.sha3_256(hash_pwd_connexion)

            #impression(hachage) 
            hachees = donnesConnexion.hexdigest()
            d={"email": entryEmailConnexion.get(), "mdp": hachees}
            #--------------connexion a base de donne--------------------
            conn = sqlite3.connect('database.db')
            #designer le cursor "c"
            c =conn.cursor()

            c.execute("SELECT  email,mdp FROM inscription WHERE email=:email AND mdp=:mdp ",d)

            donneeParcourie=c.fetchall()
            print(donneeParcourie)
            
            if entryEmailConnexion.get() in donneeParcourie and hachees in donneeParcourie:
                print('ok')
                messagebox.showinfo('info',"vous etes connecté!")
            
                

    entryEmailConnexion.delete(0, END)
    entryPassWordConnexion.delete(0, END)
    Button(frame1, text="Se connecter", width=30,font=("Italic",15, "bold"), bg="red", fg='white', command=conditonConnexion).pack(pady= 10,ipady=3)
    Button(frame1, text="Retour", ).pack(pady= 5)
    conne.mainloop()
def detrui():
    
    btn1=Button(frameFenetre ,text="Inscription", font=("Italic", 20, "bold"), bg="yellow", command=inscription)
    btn1.grid(row=0 ,column=0, columnspan=1)

    btn2=Button(frameFenetre, text="Connexion", font=("Italic", 20, "bold"), bg="yellow", command=connexion)
    btn2.grid(row=0 ,column=1, )
    

frameFenetre= Frame(fenetre, width=899, bg="red")
frameFenetre.grid()

btn1=Button(frameFenetre ,text="Inscription", font=("Italic", 20, "bold"), bg="yellow", command=inscription)
btn1.grid(row=0 ,column=0)

btn2=Button(frameFenetre, text="Connexion", font=("Italic", 20, "bold"), bg="yellow", command=connexion)
btn2.grid(row=0 ,column=1)

img = ImageTk.PhotoImage(Image.open("large.png"))
img_label=Label(frameFenetre,image= img, width=1000, height=500).grid(row=1, column=0, columnspan=2, padx=40 )

"""if btn1.bind():
    inscription()
    
elif btn2.bind():
    connexion()
else:
    pass"""
fenetre.mainloop()
