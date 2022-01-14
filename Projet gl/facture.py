import sqlite3
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from locdb import Database
from reservation_management import *
from tkinter import messagebox


class facture :
    def __init__(self,bf):
        self.gestionfacture = Frame(bf, bg="white", pady=10, padx=10)
        self.gestionfacture.grid(row=1, column=0)
        self.img4 = Image.open("images/facture.jpg")
        self.img4.thumbnail((220, 220))
        self.new_img4 = ImageTk.PhotoImage(self.img4)
        self.imgfacture = Label(self.gestionfacture, image=self.new_img4, padx=10, pady=10)
        self.imgfacture.pack()
        self.btnfacture = Button(self.gestionfacture, text="gestion factures", bg="#1b9ea4", fg="white", padx=10,pady=10, font=("tahoma", 15), command=self.openGestionFacture)
        self.btnfacture.pack()

    def openGestionFacture(self):
        self.master = Toplevel()
        self.master.title("Gestion de factures")
        self.master.geometry("1200x500+150+150")
        ###top frame start here ###
        self.frametop2 = Frame(self.master, bg="#1b9ea4", height=150)
        self.frametop2.pack(fill=X)
        self.ldz = Label(self.frametop2, text="Gestion de factures", bg="#1b9ea4", fg="white", font=("tahoma", 50),pady=50)
        self.ldz.pack()
        ###top frame end here ###
        ###centre frame start here ###
        self.centreframe2 = Frame(self.master, bg="white")
        self.centreframe2.pack(fill=X)
        ###frame consulter véhicule ###
        self.gestionvehicule2 = Frame(self.centreframe2, bg="white", pady=50, padx=30)
        self.gestionvehicule2.grid(row=0, column=0)
        self.btnvehicule2 = Button(self.gestionvehicule2, text="Consulter les factures", bg="#1b9ea4", fg="white",padx=10, pady=10, font=("tahoma", 15), command=self.openconsulter)
        self.btnvehicule2.pack()
        ###frame ajouter véhicule ###
        self.gestionvehicule2 = Frame(self.centreframe2, bg="white", pady=50, padx=30)
        self.gestionvehicule2.grid(row=0, column=1)
        self.btnvehicule2 = Button(self.gestionvehicule2, text="Initialiser facture", bg="#1b9ea4", fg="white", padx=10,pady=10, font=("tahoma", 15), command=self.openinitialiser)
        self.btnvehicule2.pack()
        ###frame modifier véhicule ###
        self.gestionvehicule2 = Frame(self.centreframe2, bg="white", pady=50, padx=30)
        self.gestionvehicule2.grid(row=0, column=2)
        self.btnvehicule2 = Button(self.gestionvehicule2, text="Modifier facture", bg="#1b9ea4", fg="white",padx=10, pady=10, font=("tahoma", 15), command=self.openmodifier)
        self.btnvehicule2.pack()
        self.centreframe2.grid_columnconfigure(0, weight=1)
        self.centreframe2.grid_columnconfigure(1, weight=1)
        self.centreframe2.grid_columnconfigure(2, weight=1)
        ###bottom frame start here ###
        self.bottomframe2 = Frame(self.master, bg="white", height=200)
        self.bottomframe2.pack(fill=X)
        ###frame supprimer véhicule ###
        self.gestionvehicule2 = Frame(self.bottomframe2, bg="white", pady=50, padx=30)
        self.gestionvehicule2.grid(row=0, column=0)
        self.btnvehicule2 = Button(self.gestionvehicule2, text="Supprimer facture", bg="#1b9ea4", fg="white",padx=10, pady=10, font=("tahoma", 15), command=self.opensupprimer)
        self.btnvehicule2.pack()
        ###frame supprimer véhicule ###
        self.gestionvehicule2 = Frame(self.bottomframe2, bg="white", pady=50, padx=30)
        self.gestionvehicule2.grid(row=0, column=1)
        self.btnvehicule2 = Button(self.gestionvehicule2, text="Finaliser facture", bg="#1b9ea4", fg="white", padx=10,pady=10, font=("tahoma", 15), command=self.openfinaliser)
        self.btnvehicule2.pack()
        self.bottomframe2.grid_columnconfigure(0, weight=1)
        self.bottomframe2.grid_columnconfigure(1, weight=1)

    def clicker_initialiser_fac(self):
        with Database() as db:
            mat = self.matricule.get()
            kmi = self.km_init.get()
            datei = self.date_init.get()
            try:
                v1 = db.get_vehicule(mat)
                f1 = Facture(v1, kmi, datei)
                db.ajouter_facture(f1)
                x = db.cr.lastrowid

                messagebox.showinfo(title='Confirmation', message=f'Facture ajouté avec le code {x}')
            except TypeError:
                messagebox.showerror(title='Erreur', message='Aucune vehicule existant avec ce matricule')

    def clicker_rechercher(self):
        with Database() as db:
            rch = self.recherchervhc.get()
            resultat = db.afficher_factures(rch)
            self.table.delete(*self.table.get_children())
            for r in resultat:
                self.table.insert('', 'end', values=r)

    def openinitialiser(self):
        self.master = Toplevel()
        self.master.title("Initialiser une facture")
        self.master.geometry("1200x500+150+150")
        ##############################################
        self.frameleft = Frame(self.master, width=500)
        self.frameleft.pack(side=LEFT, fill=Y)
        ##################LABELS############################
        self.marque = Label(self.frameleft, text="Matricule", font=("tahoma", 15))
        self.marque.place(x=20, y=30)
        self.modele = Label(self.frameleft, text="Kilometrage initiale", font=("tahoma", 15))
        self.modele.place(x=20, y=90)
        self.pj = Label(self.frameleft, text="Date initiale", font=("tahoma", 15))
        self.pj.place(x=20, y=150)
        self.date_hint = Label(self.frameleft, text = 'Format de date : (AAAA-MM-JJ)', font =('Tahoma', 12))
        self.date_hint.place(x=100, y=210)
        #   ------------Entries---------------
        self.matricule = Entry(self.frameleft, text="matricule", font=("tahoma", 15))

        self.matricule.place(x=200, y=30)
        self.km_init = Entry(self.frameleft, text="km_init", font=("tahoma", 15))
        self.km_init.place(x=200, y=90)
        self.date_init = Entry(self.frameleft, text="date_init", font=("tahoma", 15))
        self.date_init.place(x=200, y=150)
        #  -------------BUTTONS-----------
        self.ajouter = Button(self.frameleft, text="Ajouter", bg="#1b9ea4", fg="white", font=("tahoma", 15),
                              command=self.clicker_initialiser_fac)
        self.ajouter.place(x=200, y=350)
        # ----------------
        self.frameright = Frame(self.master, width=700)
        self.frameright.pack(side=RIGHT, fill=BOTH)
        self.topframeright = Frame(self.frameright, height=150, padx=5, pady=5, width=700)
        self.topframeright.pack(fill=X)
        self.recherchervhc = Entry(self.topframeright, font=("tahoma", 15), width=50)
        self.recherchervhc.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.rechercher = Button(self.topframeright, text="rechercher", bg="#1b9ea4", fg="white", font=("tahoma", 15),
                                 command=self.clicker_rechercher)
        self.rechercher.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.topframeright.grid_columnconfigure(0, weight=1)
        self.topframeright.grid_columnconfigure(1, weight=1)
        ########################frame tree view#######
        self.frameview = Frame(self.frameright)
        self.frameview.pack(fill=BOTH)
        self.table = ttk.Treeview(self.frameview, columns=("code_res", "date_init", "date_fin", "kilo_init","kilo_fin",
                                                           "etat", "matricule", "total"),
                                  show="headings")
        self.table.pack(fill=BOTH)
        self.table.heading("code_res", text="Code de Facture")
        self.table.heading("date_init", text="Date initiale")
        self.table.heading("date_fin", text="Date Finale")
        self.table.heading("kilo_init", text="KM Initiale")
        self.table.heading("kilo_fin", text="KM Finale")
        self.table.heading("etat", text="Etat")
        self.table.heading("matricule", text="Matricule")
        self.table.heading("total", text="Prix totale")
        self.table.column("code_res", anchor=W, width=5)
        self.table.column("date_init", anchor=W, width=5)
        self.table.column("date_fin", anchor=W, width=5)
        self.table.column("kilo_init", anchor=W, width=5)
        self.table.column("kilo_fin", anchor=W, width=5)
        self.table.column("etat", anchor=W, width=5)
        self.table.column("matricule", anchor=W, width=5)
        self.table.column("total", anchor=W, width=5)

    def clicker_finaliser(self):
        cf = self.code_fac.get()
        kmf = self.km_fin.get()
        dtf = self.dt_fin.get()
        with Database() as db:
            try:
                f1 = db.get_facture(cf)
                f1.finaliser_facture(float(kmf), dtf)
                db.final_facture(f1)
                self.total_price.config(state='normal')
                self.total_price.delete(0, END)
                self.total_price.insert(0, f1.somme)
                messagebox.showinfo(title='Confirmation', message=f'Facture N{f1.code_fact} : total = {f1.somme}')
            except TypeError:
                messagebox.showerror('Erreur', 'Aucune facture avec ce code existe')

    def openfinaliser(self):
            self.master = Toplevel()
            self.master.title("Supprimer client")
            self.master.geometry("1200x500+150+150")
            ##############################################
            self.frameleft = Frame(self.master, width=500)
            self.frameleft.pack(side=LEFT, fill=Y)
            ##################LABELS############################
            self.code_fac_label = Label(self.frameleft, text="Code de Facture", font=("tahoma", 15))
            self.code_fac_label.place(x=20, y=30)
            self.kilo_fin_label = Label(self.frameleft, text="Kilometrage Finale", font=("tahoma", 15))
            self.kilo_fin_label.place(x=20, y=90)
            self.date_final_label = Label(self.frameleft, text="Date finale", font=("tahoma", 15))
            self.date_final_label.place(x=20, y=150)
            self.date_hint = Label(self.frameleft, text='Format de date : (AAAA-MM-JJ)', font=('Tahoma', 12))
            self.date_hint.place(x=100, y=210)
            ##################ENTRIES############################
            self.code_fac = Entry(self.frameleft, text="Code de facture", font=("tahoma", 15))
            self.code_fac.place(x=200, y=30)
            self.km_fin = Entry(self.frameleft, text="kmfin", font=("tahoma", 15))
            self.km_fin.place(x=200, y=90)
            self.dt_fin = Entry(self.frameleft, text="dt_fin", font=("tahoma", 15))
            self.dt_fin.place(x=200, y=150)
            today = datetime.today()
            d1 = today.strftime('%Y-%m-%d')
            self.dt_fin.delete(0, END)
            self.dt_fin.insert(0, d1)
            self.total_price = Entry(self.frameleft, font=("tahoma", 15), state='disabled')
            self.total_price.place(x=200, y=410)
            ##################BUTTONS############################
            self.finaliser = Button(self.frameleft, text="Finaliser", bg="#1b9ea4", fg="white", font=("tahoma", 15),
                                    command=self.clicker_finaliser)
            self.finaliser.place(x=200, y=350)
            self.frameright = Frame(self.master, width=700)
            self.frameright.pack(side=RIGHT, fill=BOTH)
            self.topframeright = Frame(self.frameright, height=150, padx=5, pady=5, width=700)
            self.topframeright.pack(fill=X)
            self.recherchervhc = Entry(self.topframeright, font=("tahoma", 15), width=50)
            self.recherchervhc.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
            self.rechercher = Button(self.topframeright, text="rechercher", bg="#1b9ea4", fg="white",
                                     font=("tahoma", 15),
                                     command=self.clicker_rechercher)
            self.rechercher.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
            self.topframeright.grid_columnconfigure(0, weight=1)
            self.topframeright.grid_columnconfigure(1, weight=1)
            ########################frame tree view#######
            self.frameview = Frame(self.frameright)
            self.frameview.pack(fill=BOTH)
            self.table = ttk.Treeview(self.frameview,
                                      columns=("code_res", "date_init", "date_fin", "kilo_init", "kilo_fin",
                                               "etat", "matricule", "total"),
                                      show="headings")
            self.table.pack(fill=BOTH)
            self.table.heading("code_res", text="Code de Facture")
            self.table.heading("date_init", text="Date initiale")
            self.table.heading("date_fin", text="Date Finale")
            self.table.heading("kilo_init", text="KM Initiale")
            self.table.heading("kilo_fin", text="KM Finale")
            self.table.heading("etat", text="Etat")
            self.table.heading("matricule", text="Matricule")
            self.table.heading("total", text="Prix totale")
            self.table.column("code_res", anchor=W, width=5)
            self.table.column("date_init", anchor=W, width=5)
            self.table.column("date_fin", anchor=W, width=5)
            self.table.column("kilo_init", anchor=W, width=5)
            self.table.column("kilo_fin", anchor=W, width=5)
            self.table.column("etat", anchor=W, width=5)
            self.table.column("matricule", anchor=W, width=5)
            self.table.column("total", anchor=W, width=5)

    def openconsulter(self):
        self.master = Toplevel()
        self.master.title("Consulter clients")
        self.master.geometry("1200x500+150+150")
        ##############################################
        self.frameleft = Frame(self.master, width=500)
        self.frameleft.pack(side=LEFT, fill=Y)
        ##################LABELS############################
        self.matricle = Label(self.frameleft, text="code_res", font=("tahoma", 15))
        self.matricle.place(x=20, y=30)
        self.marque = Label(self.frameleft, text="matricule", font=("tahoma", 15))
        self.marque.place(x=20, y=90)
        self.modele = Label(self.frameleft, text="km_init", font=("tahoma", 15))
        self.modele.place(x=20, y=150)
        self.ppk = Label(self.frameleft, text="km_fin", font=("tahoma", 15))
        self.ppk.place(x=20, y=210)
        self.pj = Label(self.frameleft, text="date_init", font=("tahoma", 15))
        self.pj.place(x=20, y=270)
        self.ppk = Label(self.frameleft, text="date_fin", font=("tahoma", 15))
        self.ppk.place(x=20, y=330)
        self.pj = Label(self.frameleft, text="etat", font=("tahoma", 15))
        self.pj.place(x=20, y=390)
        ##################ENTRIES############################
        self.matricle = Entry(self.frameleft, text="code_res", font=("tahoma", 15))
        self.matricle.place(x=200, y=30)
        self.marque = Entry(self.frameleft, text="matricule", font=("tahoma", 15))
        self.marque.place(x=200, y=90)
        self.modele = Entry(self.frameleft, text="km_init", font=("tahoma", 15))
        self.modele.place(x=200, y=150)
        self.ppk = Entry(self.frameleft, text="km_fin", font=("tahoma", 15))
        self.ppk.place(x=200, y=210)
        self.pj = Entry(self.frameleft, text="date_init", font=("tahoma", 15))
        self.pj.place(x=200, y=270)
        self.ppk = Entry(self.frameleft, text="date_fin", font=("tahoma", 15))
        self.ppk.place(x=200, y=330)
        self.pj = Entry(self.frameleft, text="etat", font=("tahoma", 15))
        self.pj.place(x=200, y=390)
        ##################BUTTONS############################
        self.ajouter = Button(self.frameleft, text="consulter", bg="#1b9ea4", fg="white", font=("tahoma", 15))
        self.ajouter.place(x=200, y=450)
        ###########################
        self.frameright = Frame(self.master, width=700)
        self.frameright.pack(side=RIGHT, fill=BOTH)
        self.topframeright = Frame(self.frameright, height=150, padx=5, pady=5, width=700)
        self.topframeright.pack(fill=X)
        self.recherchervhc = Entry(self.topframeright, font=("tahoma", 15), width=50)
        self.recherchervhc.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.rechercher = Button(self.topframeright, text="rechercher", bg="#1b9ea4", fg="white", font=("tahoma", 15))
        self.rechercher.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.topframeright.grid_columnconfigure(0, weight=1)
        self.topframeright.grid_columnconfigure(1, weight=1)
        ########################frame tree view#######
        self.frameview = Frame(self.frameright)
        self.frameview.pack(fill=BOTH)
        self.table = ttk.Treeview(self.frameview, columns=(
        "code_res", "matricule", "km_init", "km_fin", "date_init", "date_fin", "etat"), show="headings")
        self.table.pack(fill=BOTH)
        self.table.heading("code_res", text="code_res")
        self.table.heading("matricule", text="matricule")
        self.table.heading("km_init", text="km_init")
        self.table.heading("km_fin", text="km_fin")
        self.table.heading("date_init", text="date_init")
        self.table.heading("date_fin", text="date_fin")
        self.table.heading("etat", text="etat")
        self.table.column("code_res", anchor=W, width=15)
        self.table.column("matricule", anchor=W, width=15)
        self.table.column("km_init", anchor=W, width=15)
        self.table.column("km_fin", anchor=W, width=15)
        self.table.column("date_init", anchor=W, width=15)
        self.table.column("date_fin", anchor=W, width=15)
        self.table.column("etat", anchor=W, width=15)

    def clicker_consulter(self):
        db = Database()
        num2 = self.code_fac.get()
        resultats2 = db.afficher_factures(num2)
        # delete pour vider la zone d'ecriture, insert pour inserer les nouvelles données
        self.datei.delete(0, END)
        self.datei.insert(0, '' + resultats2[0][1])

        self.datef.delete(0, END)
        self.datef.insert(0, '' + str(resultats2[0][2]))

        self.kminit.delete(0, END)
        self.kminit.insert(0, '' + str(resultats2[0][3]))

        self.kmfin.delete(0, END)
        self.kmfin.insert(0, '' + str(resultats2[0][4]))

        self.etat.delete(0, END)
        self.etat.insert(0, '' + str(resultats2[0][5]))

        self.matricule.delete(0, END)
        self.matricule.insert(0, '' + str(resultats2[0][6]))

    def clicker_modifer(self):
        db = Database()
        code = self.code_fac.get()
        datei2 = self.datei.get()
        datef2 = self.datef.get()
        kmi2 = float(self.kminit.get())
        kmf2 = float(self.kmfin.get())
        etat2 = self.etat.get()
        mat2 = self.matricule.get()
        try:
            v2 = db.get_vehicule(matricule=mat2)
        except TypeError:
            messagebox.showerror('Erreur', 'Aucun vehicule existe avec ce matricule')

        f2 = Facture(v2, kmi2, datei2, code, etat2, kmf2, datef2)
        db.modifier_facture(f2)
        messagebox.showinfo("Confirmation", "Donnee modifiés")

    def openmodifier(self):
        self.master = Toplevel()
        self.master.title("Modifier client")
        self.master.geometry("1200x500+150+150")
        ##############################################
        self.frameleft = Frame(self.master, width=500)
        self.frameleft.pack(side=LEFT, fill=Y)
        # ------------LABELS----------
        self.matricle = Label(self.frameleft, text="Code Facture", font=("tahoma", 15))
        self.matricle.place(x=20, y=30)
        self.marque = Label(self.frameleft, text="Date initiale", font=("tahoma", 15))
        self.marque.place(x=20, y=90)
        self.modele = Label(self.frameleft, text="Date finale", font=("tahoma", 15))
        self.modele.place(x=20, y=150)
        self.ppk = Label(self.frameleft, text="KM initiale", font=("tahoma", 15))
        self.ppk.place(x=20, y=210)
        self.pj = Label(self.frameleft, text="KM finale", font=("tahoma", 15))
        self.pj.place(x=20, y=270)
        self.ppk = Label(self.frameleft, text="Etat", font=("tahoma", 15))
        self.ppk.place(x=20, y=330)
        self.pj = Label(self.frameleft, text="Matricule", font=("tahoma", 15))
        self.pj.place(x=20, y=390)
        ##################ENTRIES############################
        self.code_fac = Entry(self.frameleft, text="code_res", font=("tahoma", 15))
        self.code_fac.place(x=200, y=30)
        self.datei = Entry(self.frameleft, text="date_init", font=("tahoma", 15))
        self.datei.place(x=200, y=90)
        self.datef = Entry(self.frameleft, text="datef", font=("tahoma", 15))
        self.datef.place(x=200, y=150)
        self.kminit = Entry(self.frameleft, text="kminit", font=("tahoma", 15))
        self.kminit.place(x=200, y=210)
        self.kmfin = Entry(self.frameleft, text="kmfin", font=("tahoma", 15))
        self.kmfin.place(x=200, y=270)
        self.etat = Entry(self.frameleft, text="date_fin", font=("tahoma", 15))
        self.etat.place(x=200, y=330)
        self.matricule = Entry(self.frameleft, text="etat", font=("tahoma", 15))
        self.matricule.place(x=200, y=390)
        ##################BUTTONS############################
        self.ajouter = Button(self.frameleft, text="Modifier", bg="#1b9ea4", fg="white", font=("tahoma", 15),
                              command=self.clicker_modifer)
        self.ajouter.place(x=200, y=450)
        self.consulter = Button(self.frameleft, text='Consulter', bg="#1b9ea4", fg="white", font=("tahoma", 15),
                                command=self.clicker_consulter)
        self.consulter.place(x=50, y=450)
        ###########################
        self.frameright = Frame(self.master, width=700)
        self.frameright.pack(side=RIGHT, fill=BOTH)
        self.topframeright = Frame(self.frameright, height=150, padx=5, pady=5, width=700)
        self.topframeright.pack(fill=X)
        self.recherchervhc = Entry(self.topframeright, font=("tahoma", 15), width=50)
        self.recherchervhc.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.rechercher = Button(self.topframeright, text="rechercher", bg="#1b9ea4", fg="white", font=("tahoma", 15),
                                 command=self.clicker_rechercher)
        self.rechercher.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.topframeright.grid_columnconfigure(0, weight=1)
        self.topframeright.grid_columnconfigure(1, weight=1)
        ########################frame tree view#######
        self.frameview = Frame(self.frameright)
        self.frameview.pack(fill=BOTH)
        self.table = ttk.Treeview(self.frameview,
                                  columns=("code_res", "date_init", "date_fin", "kilo_init", "kilo_fin",
                                           "etat", "matricule", "total"),
                                  show="headings")
        self.table.pack(fill=BOTH)
        self.table.heading("code_res", text="Code de Facture")
        self.table.heading("date_init", text="Date initiale")
        self.table.heading("date_fin", text="Date Finale")
        self.table.heading("kilo_init", text="KM Initiale")
        self.table.heading("kilo_fin", text="KM Finale")
        self.table.heading("etat", text="Etat")
        self.table.heading("matricule", text="Matricule")
        self.table.heading("total", text="Prix totale")
        self.table.column("code_res", anchor=W, width=5)
        self.table.column("date_init", anchor=W, width=5)
        self.table.column("date_fin", anchor=W, width=5)
        self.table.column("kilo_init", anchor=W, width=5)
        self.table.column("kilo_fin", anchor=W, width=5)
        self.table.column("etat", anchor=W, width=5)
        self.table.column("matricule", anchor=W, width=5)
        self.table.column("total", anchor=W, width=5)

    def clicker_supprimer(self):
        with Database() as db:
            cf = self.code_fac.get()
            answ = messagebox.askyesno('Confirmation', f'Vous êtes entrain de supprimer la facture N {cf}. Continuer?')
            if answ:
                try:
                    db.supprimer_facture(cf)
                    messagebox.showinfo('Succés', 'Facture suprrimé')
                except sqlite3.Error:
                    messagebox.showerror('Erreur', "Facture avec ce code n'existe pas")

    def opensupprimer(self):
        self.master = Toplevel()
        self.master.title("Supprimer client")
        self.master.geometry("1200x500+150+150")
        ##############################################
        self.frameleft = Frame(self.master, width=500)
        self.frameleft.pack(side=LEFT, fill=Y)
        ##################LABELS############################
        self.code_fac_label = Label(self.frameleft, text="Code Facture", font=("tahoma", 15))
        self.code_fac_label.place(x=20, y=30)

        ##################ENTRIES############################
        self.code_fac = Entry(self.frameleft, text="code_fac", font=("tahoma", 15))
        self.code_fac.place(x=200, y=30)
        ##################BUTTONS############################
        self.supprimer = Button(self.frameleft, text="supprimer", bg="#1b9ea4", fg="white", font=("tahoma", 15),
                                command=self.clicker_supprimer)
        self.supprimer.place(x=200, y=450)
        ###########################
        self.frameright = Frame(self.master, width=700)
        self.frameright.pack(side=RIGHT, fill=BOTH)
        self.topframeright = Frame(self.frameright, height=150, padx=5, pady=5, width=700)
        self.topframeright.pack(fill=X)
        self.recherchervhc = Entry(self.topframeright, font=("tahoma", 15), width=50)
        self.recherchervhc.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.rechercher = Button(self.topframeright, text="rechercher", bg="#1b9ea4", fg="white", font=("tahoma", 15),
                                 command=self.clicker_rechercher)
        self.rechercher.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.topframeright.grid_columnconfigure(0, weight=1)
        self.topframeright.grid_columnconfigure(1, weight=1)
        # --------- frame tree view -----
        self.frameview = Frame(self.frameright)
        self.frameview.pack(fill=BOTH)
        self.table = ttk.Treeview(self.frameview,
                                  columns=("code_res", "date_init", "date_fin", "kilo_init", "kilo_fin",
                                           "etat", "matricule", "total"),
                                  show="headings")
        self.table.pack(fill=BOTH)
        self.table.heading("code_res", text="Code de Facture")
        self.table.heading("date_init", text="Date initiale")
        self.table.heading("date_fin", text="Date Finale")
        self.table.heading("kilo_init", text="KM Initiale")
        self.table.heading("kilo_fin", text="KM Finale")
        self.table.heading("etat", text="Etat")
        self.table.heading("matricule", text="Matricule")
        self.table.heading("total", text="Prix totale")
        self.table.column("code_res", anchor=W, width=5)
        self.table.column("date_init", anchor=W, width=5)
        self.table.column("date_fin", anchor=W, width=5)
        self.table.column("kilo_init", anchor=W, width=5)
        self.table.column("kilo_fin", anchor=W, width=5)
        self.table.column("etat", anchor=W, width=5)
        self.table.column("matricule", anchor=W, width=5)
        self.table.column("total", anchor=W, width=5)