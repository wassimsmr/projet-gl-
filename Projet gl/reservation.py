import sqlite3
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from locdb import Database
from reservation_management import *
from tkinter import messagebox

class reservation :
    def __init__(self, cf):
        self.gestionreservation = Frame(cf, bg="white", pady=10, padx=10)
        self.gestionreservation.grid(row=0, column=2)
        self.img3 = Image.open("images/reservation.jpg")
        self.img3.thumbnail((170, 170))
        self.new_img3 = ImageTk.PhotoImage(self.img3)
        self.imgreservation = Label(self.gestionreservation, image=self.new_img3, padx=10, pady=10)
        self.imgreservation.pack()
        self.btnreservation = Button(self.gestionreservation, text="gestion réservations", bg="#1b9ea4", fg="white",padx=10, pady=10, font=("tahoma", 15), command=self.openGestionReservation)
        self.btnreservation.pack()


    def clickajouterres(self):
        db = Database()
        cd1 = self.coderes.get()
        mat = self.matricule.get()
        dd = self.datedeb.get()
        duree1 = self.duree.get()
        df = self.datefin.get()
        r1 = Reservation(cd1, mat, dd, duree1, df)
        try:
            db.ajouter_reservation(r1)
            messagebox.showinfo("Confirmation", "Réservation enregistré")
        except sqlite3.IntegrityError:
            messagebox.showerror("Erreur", "Véhicule existant")

    def clickrechercheres(self):
        db = Database()
        res1 = self.rechercherres.get()
        resultats = db.afficher_reservation(res1)
        for res in resultats:
            self.table.insert('','end',values=res)

    def clicksupprimerres(self):
        db = Database()
        cod1 = self.coderes.get()
        try:
            db.supprimer_reservation(cod1)
            messagebox.showinfo("Confirmation", "Réservation supprimé")
        except sqlite3.IntegrityError:
            messagebox.showerror("Erreur", "Véhicule existant")

    def clickconsulterres(self):
        db = Database()
        cd2 = self.coderes1.get()
        resultats2 = db.afficher_reservation(cd2)
        # delete pour vider la zone d'ecriture, insert pour inserer les nouvelles données
        self.mat1.delete(0, END)
        self.mat1.insert(0, ''+str(resultats2[0][1]))

        self.datd.delete(0, END)
        self.datd.insert(0, ''+str(resultats2[0][2]))

        self.dur.delete(0, END)
        self.dur.insert(0, ''+str(resultats2[0][3]))

        self.datf.delete(0, END)
        self.datf.insert(0, '' + str(resultats2[0][4]))

    def clickmodifierres(self):
        db=Database()
        c1 = self.coderes1.get()
        ma2 = self.mat1.get()
        dd = self.datd.get()
        dr = self.dur.get()
        df = self.datf.get()
        r2 = Reservation(c1, ma2, dd, dr,df)
        db.modifier_reservation(r2)
        messagebox.showinfo("Confirmation", "Donnee modifiés")

    def openGestionReservation(self):
        self.master = Toplevel()
        self.master.title("Gestion de réservations")
        self.master.geometry("1200x500+150+150")
        ###top frame start here ###
        self.frametop2 = Frame(self.master, bg="#1b9ea4", height=150)
        self.frametop2.pack(fill=X)
        self.ldz = Label(self.frametop2, text="Gestion de réservations", bg="#1b9ea4", fg="white", font=("tahoma", 50),pady=50)
        self.ldz.pack()
        ###top frame end here ###
        ###centre frame start here ###
        self.centreframe2 = Frame(self.master, bg="white")
        self.centreframe2.pack(fill=X)

        ###frame ajouter véhicule ###
        self.gestionvehicule2 = Frame(self.centreframe2, bg="white", pady=50, padx=30)
        self.gestionvehicule2.grid(row=0, column=0)
        self.btnvehicule2 = Button(self.gestionvehicule2, text="Ajouter réservation", bg="#1b9ea4", fg="white", padx=10,pady=10, font=("tahoma", 15), command=self.openajouter)
        self.btnvehicule2.pack()
        ###frame modifier véhicule ###
        self.gestionvehicule2 = Frame(self.centreframe2, bg="white", pady=50, padx=30)
        self.gestionvehicule2.grid(row=0, column=1)
        self.btnvehicule2 = Button(self.gestionvehicule2, text="Modifier réservation", bg="#1b9ea4", fg="white", padx=10,pady=10, font=("tahoma", 15), command=self.openmodifier)
        self.btnvehicule2.pack()
        self.centreframe2.grid_columnconfigure(0, weight=1)
        self.centreframe2.grid_columnconfigure(1, weight=1)
        self.centreframe2.grid_columnconfigure(2, weight=1)

        ###frame supprimer véhicule ###
        self.gestionvehicule2 = Frame(self.centreframe2, bg="white", pady=50, padx=30)
        self.gestionvehicule2.grid(row=0, column=2)
        self.btnvehicule2 = Button(self.gestionvehicule2, text="Supprimer réservation", bg="#1b9ea4", fg="white", padx=10, pady=10, font=("tahoma", 15), command=self.opensupprimer)
        self.btnvehicule2.pack()


    def openajouter(self):
        self.master = Toplevel()
        self.master.title("Ajouter une réservation")
        self.master.geometry("1200x500+150+150")
        ##############################################
        self.frameleft = Frame(self.master, width=500)
        self.frameleft.pack(side=LEFT, fill=Y)
        ##################LABELS############################
        self.matricle = Label(self.frameleft, text="code_res", font=("tahoma", 15))
        self.matricle.place(x=20, y=30)
        self.marque = Label(self.frameleft, text="matricule", font=("tahoma", 15))
        self.marque.place(x=20, y=90)
        self.modele = Label(self.frameleft, text="date_deb", font=("tahoma", 15))
        self.modele.place(x=20, y=150)
        self.ppk = Label(self.frameleft, text="durée", font=("tahoma", 15))
        self.ppk.place(x=20, y=210)
        self.pj = Label(self.frameleft, text="date_fin", font=("tahoma", 15))
        self.pj.place(x=20, y=270)
        ##################ENTRIES############################
        self.coderes = Entry(self.frameleft, text="code_res", font=("tahoma", 15))
        self.coderes.place(x=200, y=30)
        self.matricule = Entry(self.frameleft, text="matricule", font=("tahoma", 15))
        self.matricule.place(x=200, y=90)
        self.datedeb = Entry(self.frameleft, text="date_deb", font=("tahoma", 15))
        self.datedeb.place(x=200, y=150)
        self.duree = Entry(self.frameleft, text="durée", font=("tahoma", 15))
        self.duree.place(x=200, y=210)
        self.datefin = Entry(self.frameleft, text="date_finr", font=("tahoma", 15))
        self.datefin.place(x=200, y=270)
        ##################BUTTONS############################
        self.ajouter = Button(self.frameleft, text="ajouter", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickajouterres)
        self.ajouter.place(x=200, y=380)
        ###########################
        self.frameright = Frame(self.master, width=700)
        self.frameright.pack(side=RIGHT, fill=BOTH)
        self.topframeright = Frame(self.frameright, height=150, padx=5, pady=5, width=700)
        self.topframeright.pack(fill=X)
        self.rechercherres = Entry(self.topframeright, font=("tahoma", 15), width=50)
        self.rechercherres.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.rechercher = Button(self.topframeright, text="rechercher", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickrechercheres)
        self.rechercher.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.topframeright.grid_columnconfigure(0, weight=1)
        self.topframeright.grid_columnconfigure(1, weight=1)
        ########################frame tree view#######
        self.frameview = Frame(self.frameright)
        self.frameview.pack(fill=BOTH)
        self.table = ttk.Treeview(self.frameview,columns=("code_res", "matricule", "date_deb", "durée", "date_fin"),show="headings")
        self.table.pack(fill=BOTH)
        self.table.heading("code_res", text="code_res")
        self.table.heading("matricule", text="matricule")
        self.table.heading("date_deb", text="date_deb")
        self.table.heading("durée", text="durée")
        self.table.heading("date_fin", text="date_fin")
        self.table.column("code_res", anchor=W, width=15)
        self.table.column("matricule", anchor=W, width=15)
        self.table.column("date_deb", anchor=W, width=15)
        self.table.column("durée", anchor=W, width=15)
        self.table.column("date_fin", anchor=W, width=15)


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
        self.marque = Label(self.frameleft, text="matricule", font=("tahoma", 15))
        self.marque.place(x=20, y=90)
        self.modele = Label(self.frameleft, text="date_deb", font=("tahoma", 15))
        self.modele.place(x=20, y=150)
        self.ppk = Label(self.frameleft, text="durée", font=("tahoma", 15))
        self.ppk.place(x=20, y=210)
        self.pj = Label(self.frameleft, text="date_fin", font=("tahoma", 15))
        self.pj.place(x=20, y=270)
        ##################ENTRIES############################
        self.coderes1 = Entry(self.frameleft, text="code_res", font=("tahoma", 15))
        self.coderes1.place(x=200, y=30)
        self.mat1 = Entry(self.frameleft, text="matricule", font=("tahoma", 15))
        self.mat1.place(x=200, y=90)
        self.datd = Entry(self.frameleft, text="date_deb", font=("tahoma", 15))
        self.datd.place(x=200, y=150)
        self.dur = Entry(self.frameleft, text="durée", font=("tahoma", 15))
        self.dur.place(x=200, y=210)
        self.datf = Entry(self.frameleft, text="date_finr", font=("tahoma", 15))
        self.datf.place(x=200, y=270)
        ##################BUTTONS############################
        self.modifier = Button(self.frameleft, text="Modifier", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickmodifierres)
        self.modifier.place(x=300, y=380)
        self.consulter = Button(self.frameleft, text="Consulter", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickconsulterres)
        self.consulter.place(x=100, y=380)
        ###########################
        self.frameright = Frame(self.master, width=700)
        self.frameright.pack(side=RIGHT, fill=BOTH)
        self.topframeright = Frame(self.frameright, height=150, padx=5, pady=5, width=700)
        self.topframeright.pack(fill=X)
        self.rechercherres = Entry(self.topframeright, font=("tahoma", 15), width=50)
        self.rechercherres.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.rechercher = Button(self.topframeright, text="rechercher", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickrechercheres)
        self.rechercher.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.topframeright.grid_columnconfigure(0, weight=1)
        self.topframeright.grid_columnconfigure(1, weight=1)
        ########################frame tree view#######
        self.frameview = Frame(self.frameright)
        self.frameview.pack(fill=BOTH)
        self.table = ttk.Treeview(self.frameview, columns=("code_res", "matricule", "date_deb", "durée", "date_fin"),show="headings")
        self.table.pack(fill=BOTH)
        self.table.heading("code_res", text="code_res")
        self.table.heading("matricule", text="matricule")
        self.table.heading("date_deb", text="date_deb")
        self.table.heading("durée", text="durée")
        self.table.heading("date_fin", text="date_fin")
        self.table.column("code_res", anchor=W, width=15)
        self.table.column("matricule", anchor=W, width=15)
        self.table.column("date_deb", anchor=W, width=15)
        self.table.column("durée", anchor=W, width=15)
        self.table.column("date_fin", anchor=W, width=15)

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
        self.marque = Label(self.frameleft, text="matricule", font=("tahoma", 15))
        self.marque.place(x=20, y=90)
        self.modele = Label(self.frameleft, text="date_deb", font=("tahoma", 15))
        self.modele.place(x=20, y=150)
        self.ppk = Label(self.frameleft, text="durée", font=("tahoma", 15))
        self.ppk.place(x=20, y=210)
        self.pj = Label(self.frameleft, text="date_fin", font=("tahoma", 15))
        self.pj.place(x=20, y=270)
        ##################ENTRIES############################
        self.coderes = Entry(self.frameleft, text="code_res", font=("tahoma", 15))
        self.coderes.place(x=200, y=30)
        self.marque = Entry(self.frameleft, text="matricule", font=("tahoma", 15))
        self.marque.place(x=200, y=90)
        self.modele = Entry(self.frameleft, text="date_deb", font=("tahoma", 15))
        self.modele.place(x=200, y=150)
        self.ppk = Entry(self.frameleft, text="durée", font=("tahoma", 15))
        self.ppk.place(x=200, y=210)
        self.pj = Entry(self.frameleft, text="date_finr", font=("tahoma", 15))
        self.pj.place(x=200, y=270)
        ##################BUTTONS############################
        self.ajouter = Button(self.frameleft, text="supprimer", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clicksupprimerres)
        self.ajouter.place(x=200, y=380)
        ###########################
        self.frameright = Frame(self.master, width=700)
        self.frameright.pack(side=RIGHT, fill=BOTH)
        self.topframeright = Frame(self.frameright, height=150, padx=5, pady=5, width=700)
        self.topframeright.pack(fill=X)
        self.rechercherres = Entry(self.topframeright, font=("tahoma", 15), width=50)
        self.rechercherres.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.rechercher = Button(self.topframeright, text="rechercher", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickrechercheres)
        self.rechercher.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.topframeright.grid_columnconfigure(0, weight=1)
        self.topframeright.grid_columnconfigure(1, weight=1)
        ########################frame tree view#######
        self.frameview = Frame(self.frameright)
        self.frameview.pack(fill=BOTH)
        self.table = ttk.Treeview(self.frameview, columns=("code_res", "matricule", "date_deb", "durée", "date_fin"),show="headings")
        self.table.pack(fill=BOTH)
        self.table.heading("code_res", text="code_res")
        self.table.heading("matricule", text="matricule")
        self.table.heading("date_deb", text="date_deb")
        self.table.heading("durée", text="durée")
        self.table.heading("date_fin", text="date_fin")
        self.table.column("code_res", anchor=W, width=15)
        self.table.column("matricule", anchor=W, width=15)
        self.table.column("date_deb", anchor=W, width=15)
        self.table.column("durée", anchor=W, width=15)
        self.table.column("date_fin", anchor=W, width=15)
