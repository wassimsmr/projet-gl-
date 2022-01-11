from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

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

    def openinitialiser(self):
        self.master = Toplevel()
        self.master.title("Initialiser une facture")
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
        self.pj = Label(self.frameleft, text="date_init", font=("tahoma", 15))
        self.pj.place(x=20, y=210)
        ##################ENTRIES############################
        self.matricle = Entry(self.frameleft, text="code_res", font=("tahoma", 15))
        self.matricle.place(x=200, y=30)
        self.marque = Entry(self.frameleft, text="matricule", font=("tahoma", 15))
        self.marque.place(x=200, y=90)
        self.modele = Entry(self.frameleft, text="km_init", font=("tahoma", 15))
        self.modele.place(x=200, y=150)
        self.pj = Entry(self.frameleft, text="date_init", font=("tahoma", 15))
        self.pj.place(x=200, y=210)
        ##################BUTTONS############################
        self.ajouter = Button(self.frameleft, text="ajouter", bg="#1b9ea4", fg="white", font=("tahoma", 15))
        self.ajouter.place(x=200, y=350)
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
        self.table = ttk.Treeview(self.frameview, columns=("code_res", "matricule", "km_init","date_init"),show="headings")
        self.table.pack(fill=BOTH)
        self.table.heading("code_res", text="code_res")
        self.table.heading("matricule", text="matricule")
        self.table.heading("km_init", text="km_init")
        self.table.heading("date_init", text="date_init")
        self.table.column("code_res", anchor=W, width=15)
        self.table.column("matricule", anchor=W, width=15)
        self.table.column("km_init", anchor=W, width=15)
        self.table.column("date_init", anchor=W, width=15)

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
        self.ajouter = Button(self.frameleft, text="modifier", bg="#1b9ea4", fg="white", font=("tahoma", 15))
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
        self.table = ttk.Treeview(self.frameview, columns=("code_res", "matricule", "km_init", "km_fin", "date_init", "date_fin", "etat"), show="headings")
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
        self.ajouter = Button(self.frameleft, text="supprimer", bg="#1b9ea4", fg="white", font=("tahoma", 15))
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
        self.table = ttk.Treeview(self.frameview, columns=("code_res", "matricule", "km_init", "km_fin", "date_init", "date_fin", "etat"), show="headings")
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

    def openfinaliser(self):
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
            self.ppk = Label(self.frameleft, text="km_fin", font=("tahoma", 15))
            self.ppk.place(x=20, y=150)
            self.ppk = Label(self.frameleft, text="date_fin", font=("tahoma", 15))
            self.ppk.place(x=20, y=210)
            self.pj = Label(self.frameleft, text="etat", font=("tahoma", 15))
            self.pj.place(x=20, y=270)
            ##################ENTRIES############################
            self.matricle = Entry(self.frameleft, text="code_res", font=("tahoma", 15))
            self.matricle.place(x=200, y=30)
            self.marque = Entry(self.frameleft, text="matricule", font=("tahoma", 15))
            self.marque.place(x=200, y=90)
            self.ppk = Entry(self.frameleft, text="km_fin", font=("tahoma", 15))
            self.ppk.place(x=200, y=150)
            self.ppk = Entry(self.frameleft, text="date_fin", font=("tahoma", 15))
            self.ppk.place(x=200, y=210)
            self.pj = Entry(self.frameleft, text="etat", font=("tahoma", 15))
            self.pj.place(x=200, y=270)
            ##################BUTTONS############################
            self.ajouter = Button(self.frameleft, text="finaliser", bg="#1b9ea4", fg="white", font=("tahoma", 15))
            self.ajouter.place(x=200, y=350)
            ###########################
            self.frameright = Frame(self.master, width=700)
            self.frameright.pack(side=RIGHT, fill=BOTH)
            self.topframeright = Frame(self.frameright, height=150, padx=5, pady=5, width=700)
            self.topframeright.pack(fill=X)
            self.recherchervhc = Entry(self.topframeright, font=("tahoma", 15), width=50)
            self.recherchervhc.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
            self.rechercher = Button(self.topframeright, text="rechercher", bg="#1b9ea4", fg="white",
                                     font=("tahoma", 15))
            self.rechercher.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
            self.topframeright.grid_columnconfigure(0, weight=1)
            self.topframeright.grid_columnconfigure(1, weight=1)
            ########################frame tree view#######
            self.frameview = Frame(self.frameright)
            self.frameview.pack(fill=BOTH)
            self.table = ttk.Treeview(self.frameview, columns=("code_res", "matricule", "km_fin", "date_fin", "etat"), show="headings")
            self.table.pack(fill=BOTH)
            self.table.heading("code_res", text="code_res")
            self.table.heading("matricule", text="matricule")
            self.table.heading("km_fin", text="km_fin")
            self.table.heading("date_fin", text="date_fin")
            self.table.heading("etat", text="etat")
            self.table.column("code_res", anchor=W, width=15)
            self.table.column("matricule", anchor=W, width=15)
            self.table.column("km_fin", anchor=W, width=15)
            self.table.column("date_fin", anchor=W, width=15)
            self.table.column("etat", anchor=W, width=15)


