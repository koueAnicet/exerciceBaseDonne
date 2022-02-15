#--------- verifier la copie du hachage et l'achage lui meme-----
# import hashlib
# plaintext = "hello".encode()
# d = hashlib.sha256(plaintext)
# d2 = d.copy()
# # d not equal to d2, but both returns the same has
# d_hash = d.hexdigest()
# d2_hash = d.hexdigest()
# print(d == d2) # returns False
# print(d_hash == d2_hash) # returns True
 #encodage


1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
# from tkinter import *
# import tkinter as tk
# from tkcalendar import DateEntry
# from dateutil.relativedelta import relativedelta
# from datetime import date, datetime
 
# #creer une premiere fenetre
# window = Tk()
 
# #personnalier la fenetrer
# window.title("Fiche Medicale")
# window.geometry("720x480")
# window.minsize(480, 360)
# window.iconbitmap("image/leH.ico")
# window.config(background="white")
 
 
# #creation dimage
# photo = PhotoImage(file="image/logoHermes3.png")
# label = Label(window, image=photo, bg="white")
# label.pack()
 
 
# #creer la frame pour indentifiants
# frame = Frame(window, bg="#F5CBA7", bd=1, relief=SUNKEN)
 
# #titre Frame titre Identifiant
# label_title = Label(frame, text = "identifiants patient", font= ("Courrier", 15),bg="#F5CBA7", fg = "black")
# label_title.grid(row=0, column=0)
 
# lmatricule = Label(frame, text="matricule",bg="#F5CBA7").grid(row=1, column=0)
# ematricule = Entry(frame).grid(row=1,column=1)
# lnom = Label(frame, text="nom",bg="#F5CBA7").grid(row=2, column=0)
# enom = Entry(frame).grid(row=2,column=1)
# lprenom = Label(frame, text="prenom",bg="#F5CBA7").grid(row=2, column=2)
# eprenom = Entry(frame).grid(row=2,column=3)
# lsex = Label(frame, text="sex",bg="#F5CBA7").grid(row=4, column=0)
# rbsex1 = Radiobutton(frame, text = "Feminin", value = '1',bg="#F5CBA7").grid(row = 4, column = 1)
# rbsex2 = Radiobutton(frame, text = "Masculin", value = '2',bg="#F5CBA7").grid(row = 4, column = 2)
# rbsex3 = Radiobutton(frame, text = "Autre", value = '3',bg="#F5CBA7").grid(row = 4, column = 3)
# lpays = Label(frame, text="pays",bg="#F5CBA7").grid(row=5, column=0)
# epays = Entry(frame).grid(row=5,column=1)
# lville = Label(frame, text="ville",bg="#F5CBA7").grid(row=5, column=2)
# eville = Entry(frame).grid(row=5,column=3)
# lcp = Label(frame, text="code postal",bg="#F5CBA7").grid(row=5, column=4)
# ecp = Entry(frame).grid(row=5,column=5)
# ladresse = Label(frame, text="adresse",bg="#F5CBA7").grid(row=6, column=0)
# eadresse = Entry(frame).grid(row=6,column=1)
# lnumero = Label(frame, text="numero de telephone",bg="#F5CBA7").grid(row=7, column=0)
# enumero = Entry(frame).grid(row=7,column=1)
# lemail = Label(frame, text="adresse mail",bg="#F5CBA7").grid(row=7, column=2)
# eemail = Entry(frame).grid(row=7,column=3)
 
# #ajouter date de naissance
# sel = tk.StringVar() # declaring string variable
# ldatedenaissance = Label(frame, text="date de naissance",bg="#F5CBA7").grid(row=3, column=0)
# cal=DateEntry(frame,selectmode='day',textvariable=sel)
# cal.grid(row=3,column=1,padx=20)
 
# def my_upd(*args): # triggered when value of string varaible changes
#     l1.config(text=sel.get()) # read and display date
 
 
# def my_upd(*args): # triggered when value of string varaible changes
#     if(len(sel.get())>4):
#         l1.config(text=sel.get()) # read and display date
#         dob = datetime.strptime(sel.get(),'%m/%d/%y')
#         dt=date.today()
#         dt3=relativedelta(dt,dob)
#         l2.config(text="Dayes:" + str(dt3.days) +"\n Months:"+ str(dt3.months) + "\n Years:"+ str(dt3.years) )
#         print("Dayes:",dt3.days," Months:",dt3.months," Years:", dt3.years)
 
 
# l1=tk.Label(frame,bg='yellow')  # Label to display date
# l1.grid(row=3,column=2)
 
# l2=tk.Label(frame)  # Label to display date
# l2.grid(row=3,column=3,padx=10)
 
# sel.trace('w',my_upd) # on change of string variable
 
 
 
# frame.pack(fill=X)
 
# #afficher
# window.mainloop()
