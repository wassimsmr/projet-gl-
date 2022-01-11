import sqlite3
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from locdb import Database
from reservation_management import *
from tkinter import messagebox

class contrat :
    def __init__(self,bf):
        self.gestioncontrat = Frame(bf, bg="white", pady=10, padx=10)
        self.gestioncontrat.grid(row=1, column=1)
        self.img5 = Image.open("images/contrat.jpg")
        self.img5.thumbnail((170, 170))
        self.new_img5 = ImageTk.PhotoImage(self.img5)
        self.imgcontrat = Label(self.gestioncontrat, image=self.new_img5, padx=10, pady=10)
        self.imgcontrat.pack()
        self.btncontrat = Button(self.gestioncontrat, text="gestion contrat", bg="#1b9ea4", fg="white", padx=10,
                                 pady=10, font=("tahoma", 15), command=self.openGestionContrat)
        self.btncontrat.pack()

    def openGestionContrat(self):
        self.master = Toplevel()
        self.master.title("Gestion de contrats")
        self.master.geometry("1200x500+150+150")
        ###top frame start here ###
        self.frametop2 = Frame(self.master, bg="#1b9ea4", height=150)
        self.frametop2.pack(fill=X)
        self.ldz = Label(self.frametop2, text="Gestion de contrats", bg="#1b9ea4", fg="white", font=("tahoma", 50), pady=50)
        self.ldz.pack()
        ###top frame end here ###
        ###centre frame start here ###
        self.centreframe2 = Frame(self.master, bg="white")
        self.centreframe2.pack(fill=X)

        ###frame ajouter véhicule ###
        self.gestionvehicule2 = Frame(self.centreframe2, bg="white", pady=50, padx=30)
        self.gestionvehicule2.grid(row=0, column=0)
        self.btnvehicule2 = Button(self.gestionvehicule2, text="Ajouter contrat", bg="#1b9ea4", fg="white", padx=10,
                                   pady=10, font=("tahoma", 15), command=self.openajouter)
        self.btnvehicule2.pack()
        ###frame modifier véhicule ###
        self.gestionvehicule2 = Frame(self.centreframe2, bg="white", pady=50, padx=30)
        self.gestionvehicule2.grid(row=0, column=1)
        self.btnvehicule2 = Button(self.gestionvehicule2, text="Modifier contrat", bg="#1b9ea4", fg="white", padx=10,pady=10, font=("tahoma", 15), command=self.openmodifier)
        self.btnvehicule2.pack()
        self.centreframe2.grid_columnconfigure(0, weight=1)
        self.centreframe2.grid_columnconfigure(1, weight=1)
        self.centreframe2.grid_columnconfigure(2, weight=1)

        ###frame supprimer véhicule ###
        self.gestionvehicule2 = Frame(self.centreframe2, bg="white", pady=50, padx=30)
        self.gestionvehicule2.grid(row=0, column=2)
        self.btnvehicule2 = Button(self.gestionvehicule2, text="Supprimer contrat", bg="#1b9ea4", fg="white", padx=10,pady=10, font=("tahoma", 15), command=self.opensupprimer)
        self.btnvehicule2.pack()

    def clickajoutercontrat(self):
        db = Database()
        cd = self.coderes.get()
        np = self.nump.get()
        mt = self.mat.get()

        co1 = Contrat(cd, np, mt)
        try:
            db.ajouter_contrat(co1)
            messagebox.showinfo("Confirmation", "Contrat ajouté")
        except sqlite3.IntegrityError:
            messagebox.showerror("Erreur", "contrat existant")

    def clickrecherchecontrat(self):
        db = Database()
        rechco = self.rechercherco.get()
        resultats = db.afficher_contrat(rechco)
        for res in resultats:
            self.table.insert('', 'end', values=res)

    def clicksupprimercontrat(self):
        db=Database()
        cd3 = self.coderes.get()
        try:
            db.supprimer_contrat(cd3)
            messagebox.showinfo("Confirmation", "Contrat supprimé")
        except sqlite3.IntegrityError:
            messagebox.showerror("Erreur", "Contrat inexistant")

    def clickmodifiercontrat(self):
        db=Database()
        cd2 = self.coderes.get()
        np2 = self.numper.get()
        mt4 = self.mt.get()

        c3 = Contrat(cd2, np2, mt4)
        db.modifier_contrat(c3)
        messagebox.showinfo("Confirmation", "Donnee modifiés")

    def clickconsultercontrat(self):
        db = Database()
        cd5 = self.coderes.get()
        resultats2 = db.afficher_contrat(cd5)
        # delete pour vider la zone d'ecriture, insert pour inserer les nouvelles données
        self.numper.insert(0, ''+str(resultats2[0][1]))
        self.mt.insert(0, '' + str(resultats2[0][2]))
        self.numper.delete(0, END)
        self.mt.delete(0, END)




    def openajouter(self):
        self.master = Toplevel()
        self.master.title("Ajouter un contrat")
        self.master.geometry("1200x500+150+150")
        ##############################################
        self.frameleft = Frame(self.master, width=500)
        self.frameleft.pack(side=LEFT, fill=Y)
        ##################LABELS############################
        self.matricle = Label(self.frameleft, text="code_res", font=("tahoma", 15))
        self.matricle.place(x=20, y=30)
        self.marque = Label(self.frameleft, text="num permis", font=("tahoma", 15))
        self.marque.place(x=20, y=90)
        self.modele = Label(self.frameleft, text="Matricule", font=("tahoma", 15))
        self.modele.place(x=20, y=150)

        ##################ENTRIES############################
        self.coderes = Entry(self.frameleft, text="code_res", font=("tahoma", 15))
        self.coderes.place(x=200, y=30)
        self.nump = Entry(self.frameleft, text="num_permis", font=("tahoma", 15))
        self.nump.place(x=200, y=90)
        self.mat = Entry(self.frameleft, text="Matricule", font=("tahoma", 15))
        self.mat.place(x=200, y=150)

        ##################BUTTONS############################
        self.ajouter = Button(self.frameleft, text="ajouter", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickajoutercontrat)
        self.ajouter.place(x=200, y=380)
        ###########################
        self.frameright = Frame(self.master, width=700)
        self.frameright.pack(side=RIGHT, fill=BOTH)
        self.topframeright = Frame(self.frameright, height=150, padx=5, pady=5, width=700)
        self.topframeright.pack(fill=X)
        self.rechercherco = Entry(self.topframeright, font=("tahoma", 15), width=50)
        self.rechercherco.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.rechercher = Button(self.topframeright, text="rechercher", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickrecherchecontrat)
        self.rechercher.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.topframeright.grid_columnconfigure(0, weight=1)
        self.topframeright.grid_columnconfigure(1, weight=1)
        ########################frame tree view#######
        self.frameview = Frame(self.frameright)
        self.frameview.pack(fill=BOTH)
        self.table = ttk.Treeview(self.frameview,columns=("code_res", "num_permis", "Matricule"),show="headings")
        self.table.pack(fill=BOTH)
        self.table.heading("code_res", text="code_res")
        self.table.heading("num_permis", text="num_permis")
        self.table.heading("Matricule", text="Matricule")
        self.table.column("code_res", anchor=W, width=15)
        self.table.column("num_permis", anchor=W, width=15)
        self.table.column("Matricule", anchor=W, width=15)


    def openmodifier(self):
        self.master = Toplevel()
        self.master.title("Modifier client")
        self.master.geometry("1200x500+150+150")
        ##############################################
        self.frameleft = Frame(self.master, width=500)
        self.frameleft.pack(side=LEFT, fill=Y)
        ##################LABELS############################
        self.matricle = Label(self.frameleft, text="code_res", font=("tahoma", 15))
        self.matricle.place(x=20, y=30)
        self.marque = Label(self.frameleft, text="num_permis", font=("tahoma", 15))
        self.marque.place(x=20, y=90)
        self.modele = Label(self.frameleft, text="Matricule", font=("tahoma", 15))
        self.modele.place(x=20, y=150)

        ##################ENTRIES############################
        self.coderes = Entry(self.frameleft, text="code_res", font=("tahoma", 15))
        self.coderes.place(x=200, y=30)
        self.numper = Entry(self.frameleft, text="num_permis", font=("tahoma", 15))
        self.numper.place(x=200, y=90)
        self.mt = Entry(self.frameleft, text="Matricule", font=("tahoma", 15))
        self.mt.place(x=200, y=150)

        ##################BUTTONS############################
        self.modifier = Button(self.frameleft, text="Modifier", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickmodifiercontrat)
        self.modifier.place(x=300, y=380)
        self.consulter = Button(self.frameleft, text="Consulter", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickconsultercontrat)
        self.consulter.place(x=100, y=380)
        ###########################
        self.frameright = Frame(self.master, width=700)
        self.frameright.pack(side=RIGHT, fill=BOTH)
        self.topframeright = Frame(self.frameright, height=150, padx=5, pady=5, width=700)
        self.topframeright.pack(fill=X)
        self.rechercherco = Entry(self.topframeright, font=("tahoma", 15), width=50)
        self.rechercherco.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.rechercher = Button(self.topframeright, text="rechercher", bg="#1b9ea4", fg="white", font=("tahoma", 15))
        self.rechercher.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.topframeright.grid_columnconfigure(0, weight=1)
        self.topframeright.grid_columnconfigure(1, weight=1)
        ########################frame tree view#######
        self.frameview = Frame(self.frameright)
        self.frameview.pack(fill=BOTH)
        self.table = ttk.Treeview(self.frameview, columns=("code_res", "num_permis", "Matricule"), show="headings")
        self.table.pack(fill=BOTH)
        self.table.heading("code_res", text="code_res")
        self.table.heading("num_permis", text="num_permis")
        self.table.heading("Matricule", text="Matricule")
        self.table.column("code_res", anchor=W, width=15)
        self.table.column("num_permis", anchor=W, width=15)
        self.table.column("Matricule", anchor=W, width=15)

    def opensupprimer(self):
        self.master = Toplevel()
        self.master.title("Supprimer client")
        self.master.geometry("1200x500+150+150")
        ##############################################
        self.frameleft = Frame(self.master, width=500)
        self.frameleft.pack(side=LEFT, fill=Y)
        ##################LABELS############################
        self.matricle = Label(self.frameleft, text="code_res", font=("tahoma", 15))
        self.matricle.place(x=20, y=30)
        self.marque = Label(self.frameleft, text="num_permis", font=("tahoma", 15))
        self.marque.place(x=20, y=90)
        self.modele = Label(self.frameleft, text="Matricule", font=("tahoma", 15))
        self.modele.place(x=20, y=150)

        ##################ENTRIES############################
        self.coderes = Entry(self.frameleft, text="code_res", font=("tahoma", 15))
        self.coderes.place(x=200, y=30)
        self.marque = Entry(self.frameleft, text="num_permis", font=("tahoma", 15))
        self.marque.place(x=200, y=90)
        self.modele = Entry(self.frameleft, text="Matricule", font=("tahoma", 15))
        self.modele.place(x=200, y=150)

        ##################BUTTONS############################
        self.ajouter = Button(self.frameleft, text="supprimer", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clicksupprimercontrat)
        self.ajouter.place(x=200, y=380)
        ###########################
        self.frameright = Frame(self.master, width=700)
        self.frameright.pack(side=RIGHT, fill=BOTH)
        self.topframeright = Frame(self.frameright, height=150, padx=5, pady=5, width=700)
        self.topframeright.pack(fill=X)
        self.rechercherco = Entry(self.topframeright, font=("tahoma", 15), width=50)
        self.rechercherco.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.rechercher = Button(self.topframeright, text="rechercher", bg="#1b9ea4", fg="white", font=("tahoma", 15))
        self.rechercher.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.topframeright.grid_columnconfigure(0, weight=1)
        self.topframeright.grid_columnconfigure(1, weight=1)
        ########################frame tree view#######
        self.frameview = Frame(self.frameright)
        self.frameview.pack(fill=BOTH)
        self.table = ttk.Treeview(self.frameview, columns=("code_res", "num_permis", "Matricule"), show="headings")
        self.table.pack(fill=BOTH)
        self.table.heading("code_res", text="code_res")
        self.table.heading("num_permis", text="num_permis")
        self.table.heading("Matricule", text="Matricule")
        self.table.column("code_res", anchor=W, width=15)
        self.table.column("num_permis", anchor=W, width=15)
        self.table.column("Matricule", anchor=W, width=15)
