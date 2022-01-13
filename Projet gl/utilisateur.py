import sqlite3
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from locdb import Database
from reservation_management import *
from tkinter import messagebox

class utilisateur :
    def __init__(self,bf):
        self.gestionutilisateur = Frame(bf, bg="white", pady=10, padx=10)
        self.gestionutilisateur.grid(row=1, column=2)
        self.img6 = Image.open("images/utilisateur.jpg")
        self.img6.thumbnail((170, 170))
        self.new_img6 = ImageTk.PhotoImage(self.img6)
        self.imgutilisateur = Label(self.gestionutilisateur, image=self.new_img6, padx=10, pady=10)
        self.imgutilisateur.pack()
        self.btnutilisateur = Button(self.gestionutilisateur, text="gestion utilisateurs", bg="#1b9ea4", fg="white",padx=10, pady=10, font=("tahoma", 15), command=self.openGestionUtilisateur)
        self.btnutilisateur.pack()


    def openGestionUtilisateur(self):
        self.master = Toplevel()
        self.master.title("Gestion des utilisateurs")
        self.master.geometry("1200x500+150+150")
        ###top frame start here ###
        self.frametop2 = Frame(self.master, bg="#1b9ea4", height=150)
        self.frametop2.pack(fill=X)
        self.ldz = Label(self.frametop2, text="Gestion des utilisateurs", bg="#1b9ea4", fg="white", font=("tahoma", 50),pady=50)
        self.ldz.pack()
        ###top frame end here ###
        ###centre frame start here ###
        self.centreframe2 = Frame(self.master, bg="white")
        self.centreframe2.pack(fill=X)

        ###frame ajouter véhicule ###
        self.gestionvehicule2 = Frame(self.centreframe2, bg="white", pady=50, padx=30)
        self.gestionvehicule2.grid(row=0, column=0)
        self.btnvehicule2 = Button(self.gestionvehicule2, text="Ajouter utilisateur", bg="#1b9ea4", fg="white", padx=10,pady=10, font=("tahoma", 15), command=self.openajouter)
        self.btnvehicule2.pack()
        ###frame modifier véhicule ###
        self.gestionvehicule2 = Frame(self.centreframe2, bg="white", pady=50, padx=30)
        self.gestionvehicule2.grid(row=0, column=1)
        self.btnvehicule2 = Button(self.gestionvehicule2, text="Modifier utilisateur", bg="#1b9ea4", fg="white", padx=10,pady=10, font=("tahoma", 15), command=self.openmodifier)
        self.btnvehicule2.pack()
        self.centreframe2.grid_columnconfigure(0, weight=1)
        self.centreframe2.grid_columnconfigure(1, weight=1)
        self.centreframe2.grid_columnconfigure(2, weight=1)

        ###frame supprimer véhicule ###
        self.gestionvehicule2 = Frame(self.centreframe2, bg="white", pady=50, padx=30)
        self.gestionvehicule2.grid(row=0, column=2)
        self.btnvehicule2 = Button(self.gestionvehicule2, text="Supprimer utilisateur", bg="#1b9ea4", fg="white", padx=10, pady=10, font=("tahoma", 15), command=self.opensupprimer)
        self.btnvehicule2.pack()


    def clickajouterutilisateur(self):
        db = Database()
        usr = self.username.get()
        pswrd = self.password.get()
        nm = self.nom.get()
        pn = self.prenom.get()
        af = self.adminflag.get()

        ut = Utilisateur(usr, pswrd, nm,pn,af)
        try:
            db.ajouter_utilisateur(ut)
            messagebox.showinfo("Confirmation", "Utilisateur ajouté")
        except sqlite3.IntegrityError:
            messagebox.showerror("Erreur", "Utilisateur existant")

    def clickrechercheutilisateur(self):
        db = Database()
        rechuti = self.rechercheruti.get()
        resultats = db.afficher_utilisateur(rechuti)
        for res in resultats:
            self.table.insert('', 'end', values=res)

    def clicksupprimerutilisateur(self):
        db=Database()
        us = self.usr.get()
        try:
            db.supprimer_utilisateur(us)
            messagebox.showinfo("Confirmation", "Utilisateur supprimé")
        except sqlite3.IntegrityError:
            messagebox.showerror("Erreur", "Utilisateur inexistant")

    def clickmodifierutilisateur(self):
        db=Database()
        us2 = self.user.get()
        ps = self.passw.get()
        nm = self.nomm.get()
        pn = self.pre.get()
        af = self.adminflag2.get()

        u3 = Utilisateur(us2, ps, nm,pn,af)
        db.modifier_utilisateur(u3)
        messagebox.showinfo("Confirmation", "Donnee modifiés")

    def clickconsulterutilisateur(self):
        db = Database()
        us = self.user.get()
        resultats2 = db.afficher_utilisateur(us)
        # delete pour vider la zone d'ecriture, insert pour inserer les nouvelles données
        self.passw.insert(0, ''+str(resultats2[0][1]))
        self.nomm.insert(0, '' + str(resultats2[0][2]))
        self.pre.insert(0, '' + str(resultats2[0][3]))
        self.adminflag2.insert(0, '' + str(resultats2[0][4]))



    def openajouter(self):
        self.master = Toplevel()
        self.master.title("Ajouter un utilisateurs")
        self.master.geometry("1200x500+150+150")
        ##############################################
        self.frameleft = Frame(self.master, width=500)
        self.frameleft.pack(side=LEFT, fill=Y)
        ##################LABELS############################
        self.lblusername = Label(self.frameleft, text="username", font=("tahoma", 15))
        self.lblusername.place(x=20, y=30)
        self.lblpasword = Label(self.frameleft, text="password", font=("tahoma", 15))
        self.lblpasword.place(x=20, y=90)
        self.lblnom = Label(self.frameleft, text="nom", font=("tahoma", 15))
        self.lblnom.place(x=20, y=150)
        self.lblprenom = Label(self.frameleft, text="prénom", font=("tahoma", 15))
        self.lblprenom.place(x=20, y=210)
        self.lbladminflag = Label(self.frameleft, text="adminflag", font=("tahoma", 15))
        self.lbladminflag.place(x=20, y=270)
        self.lbladminflaginfo = Label(self.frameleft, text="(0 si admin , 1 sinon )", font=("tahoma", 10))
        self.lbladminflaginfo.place(x=10, y=300)

        ##################ENTRIES############################
        self.username = Entry(self.frameleft, font=("tahoma", 15))
        self.username.place(x=200, y=30)
        self.password = Entry(self.frameleft, font=("tahoma", 15))
        self.password.place(x=200, y=90)
        self.nom = Entry(self.frameleft, font=("tahoma", 15))
        self.nom.place(x=200, y=150)
        self.prenom = Entry(self.frameleft, font=("tahoma", 15))
        self.prenom.place(x=200, y=210)
        self.adminflag = Entry(self.frameleft,  font=("tahoma", 15))
        self.adminflag.place(x=200, y=270)
        ##################BUTTONS############################
        self.ajouter = Button(self.frameleft, text="ajouter", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickajouterutilisateur)
        self.ajouter.place(x=200, y=380)
        ###########################
        self.frameright = Frame(self.master, width=700)
        self.frameright.pack(side=RIGHT, fill=BOTH)
        self.topframeright = Frame(self.frameright, height=150, padx=5, pady=5, width=700)
        self.topframeright.pack(fill=X)
        self.rechercheruti = Entry(self.topframeright, font=("tahoma", 15), width=50)
        self.rechercheruti.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.rechercher = Button(self.topframeright, text="rechercher", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickrechercheutilisateur)
        self.rechercher.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.topframeright.grid_columnconfigure(0, weight=1)
        self.topframeright.grid_columnconfigure(1, weight=1)
        ########################frame tree view#######
        self.frameview = Frame(self.frameright)
        self.frameview.pack(fill=BOTH)
        self.table = ttk.Treeview(self.frameview,columns=("username", "password", "nom", "prénom","adminflag"),show="headings")
        self.table.pack(fill=BOTH)
        self.table.heading("username", text="username")
        self.table.heading("password", text="password")
        self.table.heading("nom", text="nom")
        self.table.heading("prénom", text="prénom")
        self.table.heading("adminflag", text="adminflag")
        self.table.column("username", anchor=W, width=15)
        self.table.column("password", anchor=W, width=15)
        self.table.column("nom", anchor=W, width=15)
        self.table.column("prénom", anchor=W, width=15)
        self.table.column("adminflag", anchor=W, width=15)



    def openmodifier(self):
        self.master = Toplevel()
        self.master.title("Modifier client")
        self.master.geometry("1200x500+150+150")
        ##############################################
        self.frameleft = Frame(self.master, width=500)
        self.frameleft.pack(side=LEFT, fill=Y)
        ##################LABELS############################
        self.matricle = Label(self.frameleft, text="username", font=("tahoma", 15))
        self.matricle.place(x=20, y=30)
        self.marque = Label(self.frameleft, text="password", font=("tahoma", 15))
        self.marque.place(x=20, y=90)
        self.modele = Label(self.frameleft, text="nom", font=("tahoma", 15))
        self.modele.place(x=20, y=150)
        self.ppk = Label(self.frameleft, text="prénom", font=("tahoma", 15))
        self.ppk.place(x=20, y=210)
        self.lbladminflag = Label(self.frameleft, text="adminflag", font=("tahoma", 15))
        self.lbladminflag.place(x=20, y=270)
        self.lbladminflaginfo = Label(self.frameleft, text="(0 si admin , 1 sinon )", font=("tahoma", 10))
        self.lbladminflaginfo.place(x=10, y=300)

        ##################ENTRIES############################
        self.user = Entry(self.frameleft, text="code_res", font=("tahoma", 15))
        self.user.place(x=200, y=30)
        self.passw = Entry(self.frameleft, text="matricule", font=("tahoma", 15))
        self.passw.place(x=200, y=90)
        self.nomm = Entry(self.frameleft, text="date_deb", font=("tahoma", 15))
        self.nomm.place(x=200, y=150)
        self.pre = Entry(self.frameleft, text="durée", font=("tahoma", 15))
        self.pre.place(x=200, y=210)
        self.adminflag2 = Entry(self.frameleft, font=("tahoma", 15))
        self.adminflag2.place(x=200, y=270)
        ##################BUTTONS############################
        self.modifier = Button(self.frameleft, text="Modifier", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickmodifierutilisateur)
        self.modifier.place(x=300, y=380)
        self.consulter = Button(self.frameleft, text="Consulter", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickconsulterutilisateur)
        self.consulter.place(x=100, y=380)
        ###########################
        self.frameright = Frame(self.master, width=700)
        self.frameright.pack(side=RIGHT, fill=BOTH)
        self.topframeright = Frame(self.frameright, height=150, padx=5, pady=5, width=700)
        self.topframeright.pack(fill=X)
        self.rechercheruti = Entry(self.topframeright, font=("tahoma", 15), width=50)
        self.rechercheruti.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.rechercher = Button(self.topframeright, text="rechercher", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickrechercheutilisateur)
        self.rechercher.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.topframeright.grid_columnconfigure(0, weight=1)
        self.topframeright.grid_columnconfigure(1, weight=1)
        ########################frame tree view#######
        self.frameview = Frame(self.frameright)
        self.frameview.pack(fill=BOTH)
        self.table = ttk.Treeview(self.frameview, columns=("username", "password", "nom", "prénom","adminflag"), show="headings")
        self.table.pack(fill=BOTH)
        self.table.heading("username", text="username")
        self.table.heading("password", text="password")
        self.table.heading("nom", text="nom")
        self.table.heading("prénom", text="prénom")
        self.table.heading("adminflag", text="adminflag")
        self.table.column("username", anchor=W, width=15)
        self.table.column("password", anchor=W, width=15)
        self.table.column("nom", anchor=W, width=15)
        self.table.column("prénom", anchor=W, width=15)
        self.table.column("adminflag", anchor=W, width=15)

    def opensupprimer(self):
        self.master = Toplevel()
        self.master.title("Supprimer client")
        self.master.geometry("1200x500+150+150")
        ##############################################
        self.frameleft = Frame(self.master, width=500)
        self.frameleft.pack(side=LEFT, fill=Y)
        ##################LABELS############################
        self.matricle = Label(self.frameleft, text="username", font=("tahoma", 15))
        self.matricle.place(x=20, y=30)
        self.marque = Label(self.frameleft, text="password", font=("tahoma", 15))
        self.marque.place(x=20, y=90)
        self.modele = Label(self.frameleft, text="nom", font=("tahoma", 15))
        self.modele.place(x=20, y=150)
        self.ppk = Label(self.frameleft, text="prénom", font=("tahoma", 15))
        self.ppk.place(x=20, y=210)

        ##################ENTRIES############################
        self.usr = Entry(self.frameleft, font=("tahoma", 15))
        self.usr.place(x=200, y=30)
        self.marque = Entry(self.frameleft, font=("tahoma", 15))
        self.marque.place(x=200, y=90)
        self.modele = Entry(self.frameleft, font=("tahoma", 15))
        self.modele.place(x=200, y=150)
        self.ppk = Entry(self.frameleft, font=("tahoma", 15))
        self.ppk.place(x=200, y=210)
        ##################BUTTONS############################
        self.ajouter = Button(self.frameleft, text="supprimer", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clicksupprimerutilisateur)
        self.ajouter.place(x=200, y=380)
        ###########################
        self.frameright = Frame(self.master, width=700)
        self.frameright.pack(side=RIGHT, fill=BOTH)
        self.topframeright = Frame(self.frameright, height=150, padx=5, pady=5, width=700)
        self.topframeright.pack(fill=X)
        self.rechercheruti = Entry(self.topframeright, font=("tahoma", 15), width=50)
        self.rechercheruti.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.rechercher = Button(self.topframeright, text="rechercher", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickrechercheutilisateur)
        self.rechercher.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.topframeright.grid_columnconfigure(0, weight=1)
        self.topframeright.grid_columnconfigure(1, weight=1)
        ########################frame tree view#######
        self.frameview = Frame(self.frameright)
        self.frameview.pack(fill=BOTH)
        self.table = ttk.Treeview(self.frameview, columns=("username", "password", "nom", "prénom","adminflag"), show="headings")
        self.table.pack(fill=BOTH)
        self.table.heading("username", text="username")
        self.table.heading("password", text="password")
        self.table.heading("nom", text="nom")
        self.table.heading("prénom", text="prénom")
        self.table.heading("adminflag", text="adminflag")
        self.table.column("username", anchor=W, width=15)
        self.table.column("password", anchor=W, width=15)
        self.table.column("nom", anchor=W, width=15)
        self.table.column("prénom", anchor=W, width=15)
        self.table.column("adminflag", anchor=W, width=15)