from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class client :
    def __init__(self,cf):
        self.gestionclients = Frame(cf, bg="white", pady=10, padx=10)
        self.gestionclients.grid(row=0, column=1)
        self.img2 = Image.open("images/utilisateurs et client.jpg")
        self.img2.thumbnail((140, 140))
        self.new_img2 = ImageTk.PhotoImage(self.img2)
        self.imgclient = Label(self.gestionclients, image=self.new_img2, padx=10, pady=10)
        self.imgclient.pack()
        self.btnclient = Button(self.gestionclients, text="gestion clients", bg="#1b9ea4", fg="white", padx=10, pady=10,font=("tahoma", 15), command=self.openGestionClient)
        self.btnclient.pack()

    def openGestionClient(self):
        self.master = Toplevel()
        self.master.title("Gestion de clients")
        self.master.geometry("1200x500+150+150")
        ###top frame start here ###
        self.frametop2 = Frame(self.master, bg="#1b9ea4", height=150)
        self.frametop2.pack(fill=X)
        self.gdc = Label(self.frametop2, text="Gestion de clients", bg="#1b9ea4", fg="white", font=("tahoma", 50),pady=50)
        self.gdc.pack()
        ###top frame end here ###
        ###centre frame start here ###
        self.centreframe2 = Frame(self.master, bg="white")
        self.centreframe2.pack(fill=X)
        ###frame consulter véhicule ###
        self.gestionclients2 = Frame(self.centreframe2, bg="white", pady=50, padx=30)
        self.gestionclients2.grid(row=0, column=0)
        self.btnclient2 = Button(self.gestionclients2, text="Consulter client", bg="#1b9ea4", fg="white", padx=10,pady=10, font=("tahoma", 15), command=self.openconsulter)
        self.btnclient2.pack()
        ###frame ajouter véhicule ###
        self.gestionclients2 = Frame(self.centreframe2, bg="white", pady=50, padx=30)
        self.gestionclients2.grid(row=0, column=1)
        self.btnclient2 = Button(self.gestionclients2, text="Ajouter client", bg="#1b9ea4", fg="white", padx=10,pady=10, font=("tahoma", 15), command=self.openajouter)
        self.btnclient2.pack()
        ###frame modifier véhicule ###
        self.gestionclients2 = Frame(self.centreframe2, bg="white", pady=50, padx=30)
        self.gestionclients2.grid(row=0, column=2)
        self.btnclient2 = Button(self.gestionclients2, text="Modifier client", bg="#1b9ea4", fg="white", padx=10, pady=10, font=("tahoma", 15), command=self.openmodifier)
        self.btnclient2.pack()
        self.centreframe2.grid_columnconfigure(0, weight=1)
        self.centreframe2.grid_columnconfigure(1, weight=1)
        self.centreframe2.grid_columnconfigure(2, weight=1)
        ###bottom frame start here ###
        self.bottomframe2 = Frame(self.master, bg="white", height=200)
        self.bottomframe2.pack(fill=X)
        ###frame supprimer véhicule ###
        self.gestionclients2 = Frame(self.bottomframe2, bg="white", pady=50, padx=30)
        self.gestionclients2.grid(row=0, column=0)
        self.btnclient2 = Button(self.gestionclients2, text="Supprimer client", bg="#1b9ea4", fg="white", padx=10,pady=10, font=("tahoma", 15), command=self.opensupprimer)
        self.btnclient2.pack()
        self.bottomframe2.grid_columnconfigure(0, weight=1)

    def openajouter(self):
        self.master = Toplevel()
        self.master.title("Ajouter un client")
        self.master.geometry("1200x500+150+150")
        ##############################################
        self.frameleft = Frame(self.master, width=500)
        self.frameleft.pack(side=LEFT, fill=Y)
        ##################LABELS############################
        self.Num = Label(self.frameleft, text="Num", font=("tahoma", 15))
        self.Num.place(x=20, y=30)
        self.marque = Label(self.frameleft, text="Nom", font=("tahoma", 15))
        self.marque.place(x=20, y=90)
        self.modele = Label(self.frameleft, text="Prénom", font=("tahoma", 15))
        self.modele.place(x=20, y=150)
        self.ppk = Label(self.frameleft, text="Date de naissance", font=("tahoma", 15))
        self.ppk.place(x=20, y=210)
        self.pj = Label(self.frameleft, text="Lieu de naissance", font=("tahoma", 15))
        self.pj.place(x=20, y=270)
        ##################ENTRIES############################
        self.matricle = Entry(self.frameleft, text="matricle", font=("tahoma", 15))
        self.matricle.place(x=200, y=30)
        self.marque = Entry(self.frameleft, text="marque", font=("tahoma", 15))
        self.marque.place(x=200, y=90)
        self.modele = Entry(self.frameleft, text="modele", font=("tahoma", 15))
        self.modele.place(x=200, y=150)
        self.ppk = Entry(self.frameleft, text="prix par kilomètre", font=("tahoma", 15))
        self.ppk.place(x=200, y=210)
        self.pj = Entry(self.frameleft, text="prix journalier", font=("tahoma", 15))
        self.pj.place(x=200, y=270)
        ##################BUTTONS############################
        self.ajouter = Button(self.frameleft, text="ajouter", bg="#1b9ea4", fg="white", font=("tahoma", 15))
        self.ajouter.place(x=200, y=380)
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
        self.table = ttk.Treeview(self.frameview,columns=("Num", "Nom", "Prénom", "date de naissance", "Lieu de naissance"),show="headings")
        self.table.pack(fill=BOTH)
        self.table.heading("Num", text="Num")
        self.table.heading("Nom", text="Nom")
        self.table.heading("Prénom", text="Prénom")
        self.table.heading("date de naissance", text="date de naissance")
        self.table.heading("Lieu de naissance", text="Lieu de naissance")
        self.table.column("Num", anchor=W, width=15)
        self.table.column("Nom", anchor=W, width=15)
        self.table.column("Prénom", anchor=W, width=15)
        self.table.column("date de naissance", anchor=W, width=15)
        self.table.column("Lieu de naissance", anchor=W, width=15)

    def openconsulter(self):
        self.master = Toplevel()
        self.master.title("Consulter clients")
        self.master.geometry("1200x500+150+150")
        ##############################################
        self.frameleft = Frame(self.master, width=500)
        self.frameleft.pack(side=LEFT, fill=Y)
        ##################LABELS############################
        self.matricle = Label(self.frameleft, text="Num", font=("tahoma", 15))
        self.matricle.place(x=20, y=30)
        self.marque = Label(self.frameleft, text="Nom", font=("tahoma", 15))
        self.marque.place(x=20, y=90)
        self.modele = Label(self.frameleft, text="Prénom", font=("tahoma", 15))
        self.modele.place(x=20, y=150)
        self.ppk = Label(self.frameleft, text="Date de naissance", font=("tahoma", 15))
        self.ppk.place(x=20, y=210)
        self.pj = Label(self.frameleft, text="Lieu de naissance", font=("tahoma", 15))
        self.pj.place(x=20, y=270)
        ##################ENTRIES############################
        self.matricle = Entry(self.frameleft, text="Num", font=("tahoma", 15))
        self.matricle.place(x=200, y=30)
        self.marque = Entry(self.frameleft, text="Nom", font=("tahoma", 15))
        self.marque.place(x=200, y=90)
        self.modele = Entry(self.frameleft, text="Prénom", font=("tahoma", 15))
        self.modele.place(x=200, y=150)
        self.ppk = Entry(self.frameleft, text="Date de naissance", font=("tahoma", 15))
        self.ppk.place(x=200, y=210)
        self.pj = Entry(self.frameleft, text="Lieu de naissance", font=("tahoma", 15))
        self.pj.place(x=200, y=270)
        ##################BUTTONS############################
        self.consulter = Button(self.frameleft, text="Consulter", bg="#1b9ea4", fg="white", font=("tahoma", 15))
        self.consulter.place(x=200, y=380)
        ################
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
        self.table = ttk.Treeview(self.frameview,columns=("Num", "Nom", "Prénom", "date de naissance", "Lieu de naissance"),show="headings")
        self.table.pack(fill=BOTH)
        self.table.heading("Num", text="Num")
        self.table.heading("Nom", text="Nom")
        self.table.heading("Prénom", text="Prénom")
        self.table.heading("date de naissance", text="date de naissance")
        self.table.heading("Lieu de naissance", text="Lieu de naissance")
        self.table.column("Num", anchor=W, width=15)
        self.table.column("Nom", anchor=W, width=15)
        self.table.column("Prénom", anchor=W, width=15)
        self.table.column("date de naissance", anchor=W, width=15)
        self.table.column("Lieu de naissance", anchor=W, width=15)


    def openmodifier(self):
        self.master = Toplevel()
        self.master.title("Modifier client")
        self.master.geometry("1200x500+150+150")
        ##############################################
        self.frameleft = Frame(self.master, width=500)
        self.frameleft.pack(side=LEFT, fill=Y)
        ##################LABELS############################
        self.matricle = Label(self.frameleft, text="Num", font=("tahoma", 15))
        self.matricle.place(x=20, y=30)
        self.marque = Label(self.frameleft, text="Nom", font=("tahoma", 15))
        self.marque.place(x=20, y=90)
        self.modele = Label(self.frameleft, text="Prénom", font=("tahoma", 15))
        self.modele.place(x=20, y=150)
        self.ppk = Label(self.frameleft, text="Date de naissance", font=("tahoma", 15))
        self.ppk.place(x=20, y=210)
        self.pj = Label(self.frameleft, text="Lieu de naissance", font=("tahoma", 15))
        self.pj.place(x=20, y=270)
        ##################ENTRIES############################
        self.matricle = Entry(self.frameleft, text="matricle", font=("tahoma", 15))
        self.matricle.place(x=200, y=30)
        self.marque = Entry(self.frameleft, text="marque", font=("tahoma", 15))
        self.marque.place(x=200, y=90)
        self.modele = Entry(self.frameleft, text="modele", font=("tahoma", 15))
        self.modele.place(x=200, y=150)
        self.ppk = Entry(self.frameleft, text="prix par kilomètre", font=("tahoma", 15))
        self.ppk.place(x=200, y=210)
        self.pj = Entry(self.frameleft, text="prix journalier", font=("tahoma", 15))
        self.pj.place(x=200, y=270)
        ##################BUTTONS############################
        self.modifier = Button(self.frameleft, text="Modifier", bg="#1b9ea4", fg="white", font=("tahoma", 15))
        self.modifier.place(x=200, y=380)
        ################
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
        self.table = ttk.Treeview(self.frameview,
                                  columns=("Num", "Nom", "Prénom", "date de naissance", "Lieu de naissance"),
                                  show="headings")
        self.table.pack(fill=BOTH)
        self.table.heading("Num", text="Num")
        self.table.heading("Nom", text="Nom")
        self.table.heading("Prénom", text="Prénom")
        self.table.heading("date de naissance", text="date de naissance")
        self.table.heading("Lieu de naissance", text="Lieu de naissance")
        self.table.column("Num", anchor=W, width=15)
        self.table.column("Nom", anchor=W, width=15)
        self.table.column("Prénom", anchor=W, width=15)
        self.table.column("date de naissance", anchor=W, width=15)
        self.table.column("Lieu de naissance", anchor=W, width=15)


    def opensupprimer(self):
        self.master = Toplevel()
        self.master.title("Supprimer client")
        self.master.geometry("1200x500+150+150")
        ##############################################
        self.frameleft = Frame(self.master, width=500)
        self.frameleft.pack(side=LEFT, fill=Y)
        ##################LABELS############################
        self.matricle = Label(self.frameleft, text="Num", font=("tahoma", 15))
        self.matricle.place(x=20, y=30)
        self.marque = Label(self.frameleft, text="Nom", font=("tahoma", 15))
        self.marque.place(x=20, y=90)
        self.modele = Label(self.frameleft, text="Prénom", font=("tahoma", 15))
        self.modele.place(x=20, y=150)
        self.ppk = Label(self.frameleft, text="Date de naissance", font=("tahoma", 15))
        self.ppk.place(x=20, y=210)
        self.pj = Label(self.frameleft, text="Lieu de naissance", font=("tahoma", 15))
        self.pj.place(x=20, y=270)
        ##################ENTRIES############################
        self.matricle = Entry(self.frameleft, text="matricle", font=("tahoma", 15))
        self.matricle.place(x=200, y=30)
        self.marque = Entry(self.frameleft, text="marque", font=("tahoma", 15))
        self.marque.place(x=200, y=90)
        self.modele = Entry(self.frameleft, text="modele", font=("tahoma", 15))
        self.modele.place(x=200, y=150)
        self.ppk = Entry(self.frameleft, text="prix par kilomètre", font=("tahoma", 15))
        self.ppk.place(x=200, y=210)
        self.pj = Entry(self.frameleft, text="prix journalier", font=("tahoma", 15))
        self.pj.place(x=200, y=270)
        ##################BUTTONS############################
        self.supprimer = Button(self.frameleft, text="Supprimer", bg="#1b9ea4", fg="white", font=("tahoma", 15))
        self.supprimer.place(x=200, y=380)
        ################
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
        self.table = ttk.Treeview(self.frameview,
                                  columns=("Num", "Nom", "Prénom", "date de naissance", "Lieu de naissance"),
                                  show="headings")
        self.table.pack(fill=BOTH)
        self.table.heading("Num", text="Num")
        self.table.heading("Nom", text="Nom")
        self.table.heading("Prénom", text="Prénom")
        self.table.heading("date de naissance", text="date de naissance")
        self.table.heading("Lieu de naissance", text="Lieu de naissance")
        self.table.column("Num", anchor=W, width=15)
        self.table.column("Nom", anchor=W, width=15)
        self.table.column("Prénom", anchor=W, width=15)
        self.table.column("date de naissance", anchor=W, width=15)
        self.table.column("Lieu de naissance", anchor=W, width=15)
