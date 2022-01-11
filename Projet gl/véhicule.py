import sqlite3
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from locdb import Databse
from reservation_management import *
from tkinter import messagebox

class vehicule :
    def __init__(self,cf):
        self.framegestionvehicule = Frame(cf, bg="white", pady=10, padx=10)
        self.framegestionvehicule.grid(row=0, column=0)
        self.img = Image.open("images/vehicule.jpg")
        self.img.thumbnail((250, 250))
        self.new_img = ImageTk.PhotoImage(self.img)
        self.imgvehicule = Label(self.framegestionvehicule, image=self.new_img, padx=10, pady=10)
        self.imgvehicule.pack()
        self.btngestvehicule = Button(self.framegestionvehicule, text="gestion véhicule", bg="#1b9ea4", fg="white", padx=10,pady=10, font=("tahoma", 15), command=self.openGestionVehicule)
        self.btngestvehicule.pack()


    def openGestionVehicule(self):
        self.master=Toplevel()
        self.master.title("Gestion de véhicules")
        self.master.geometry("1200x500+150+150")
        ###top frame start here ###
        self.frametop2 = Frame(self.master, bg="#1b9ea4", height=150)
        self.frametop2.pack(fill=X)
        self.ldz = Label(self.frametop2, text="Gestion de véhicules", bg="#1b9ea4", fg="white", font=("tahoma", 50), pady=50)
        self.ldz.pack()
        ###top frame end here ###
        ###centre frame start here ###
        self.centreframe2 = Frame(self.master, bg="white")
        self.centreframe2.pack(fill=X)

        ###frame ajouter véhicule ###
        self.frameajoutvehicule = Frame(self.centreframe2, bg="white", pady=50, padx=30)
        self.frameajoutvehicule.grid(row=0, column=0)
        self.btnajoutvehicule = Button(self.frameajoutvehicule, text="Ajouter véhicule", bg="#1b9ea4", fg="white", padx=10,pady=10, font=("tahoma", 15), command=self.openajouter)
        self.btnajoutvehicule.pack()
        ###frame modifier véhicule ###
        self.framemodifvehicule = Frame(self.centreframe2, bg="white", pady=50, padx=30)
        self.framemodifvehicule.grid(row=0, column=1)
        self.btnmodifvehicule2 = Button(self.framemodifvehicule, text="Modifier véhicule", bg="#1b9ea4", fg="white", padx=10,pady=10, font=("tahoma", 15),command=self.openmodifier)
        self.btnmodifvehicule2.pack()
        self.centreframe2.grid_columnconfigure(0, weight=1)
        self.centreframe2.grid_columnconfigure(1, weight=1)
        self.centreframe2.grid_columnconfigure(2, weight=1)

        ###frame supprimer véhicule ###
        self.framesupvehicule = Frame(self.centreframe2, bg="white", pady=50, padx=30)
        self.framesupvehicule.grid(row=0, column=2)
        self.btnsupvehicule = Button(self.framesupvehicule, text="Supprimer véhicule", bg="#1b9ea4", fg="white", padx=10, pady=10, font=("tahoma", 15),command=self.opensupprimer)
        self.btnsupvehicule.pack()




    def clickajouter(self):
       db = Databse()
       mat1 = self.matricule.get()
       ma1= self.marque.get()
       pj1=self.pj.get()
       pk1=self.ppk.get()
       v1=Vehicule(mat1,ma1,pj1,pk1)
       try :
          db.ajouter_vehicule(v1)
          messagebox.showinfo("Confirmation", "Véhicule ajouté")
       except sqlite3.IntegrityError :
           messagebox.showerror("Erreur","Véhicule existant")

    def clickrecherchevhc(self):
        db=Databse()
        mat2=self.recherchervhc.get()
        resultats=db.afficher_vehicules(mat2)
        for res in resultats :
            self.table.insert('','end',values=res)

    def clicksupprimervhc(self):
        db=Databse()
        mat3 = self.suppmatricle.get()
        try:
            db.supprimer_vehicule(mat3)
            messagebox.showinfo("Confirmation", "Véhicule supprimé")
        except sqlite3.IntegrityError:
            messagebox.showerror("Erreur", "Véhicule existant")

    def clickmodifier(self):
        db=Databse()
        mat4 = self.modifmatricle.get()
        ma4 = self.modifmarque.get()
        pj4 = self.modifpj.get()
        pk4 = self.modifppk.get()
        v4 = Vehicule(mat4, ma4, pj4, pk4)
        db.modifier_vehicule(v4)


    def clickconsulter(self):
        db = Databse()
        mat2 = self.modifmatricle.get()
        resultats2 = db.afficher_vehicules(mat2)
        self.modifmarque.insert(0,''+resultats2[0][1])
        self.modifpj.insert(0, ''+str(resultats2[0][2]))
        self.modifppk.insert(0, ''+str(resultats2[0][3]))

    def openajouter(self):
        self.master=Toplevel()
        self.master.title("Ajouter un véhicule")
        self.master.geometry("1200x500+150+150")
        ##############################################
        self.frameleft=Frame(self.master,width=500)
        self.frameleft.pack(side=LEFT,fill=Y)
        ##################LABELS############################
        self.lblmatricule=Label(self.frameleft,text="matricle", font=("tahoma", 15))
        self.lblmatricule.place(x=20,y=30)
        self.lblmarque = Label(self.frameleft, text="marque", font=("tahoma", 15))
        self.lblmarque.place(x=20, y=90)
        self.lblppk = Label(self.frameleft, text="prix par kilomètre", font=("tahoma", 15))
        self.lblppk.place(x=20, y=150)
        self.lblpj = Label(self.frameleft, text="prix journalier", font=("tahoma", 15))
        self.lblpj.place(x=20, y=210)
        ##################ENTRIES############################
        self.matricule = Entry(self.frameleft, font=("tahoma", 15))
        self.matricule.place(x=200, y=30)
        self.marque = Entry(self.frameleft, font=("tahoma", 15))
        self.marque.place(x=200, y=90)
        self.ppk = Entry(self.frameleft,font=("tahoma", 15))
        self.ppk.place(x=200, y=150)
        self.pj = Entry(self.frameleft, font=("tahoma", 15))
        self.pj.place(x=200, y=210)
        ##################BUTTONS############################
        self.ajouter = Button(self.frameleft, text="ajouter", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickajouter)
        self.ajouter.place(x=200, y=380)
        ###########################
        self.frameright = Frame(self.master, width=700)
        self.frameright.pack(side=RIGHT, fill=BOTH)
        self.topframeright = Frame(self.frameright, height=150, padx=5, pady=5, width=700)
        self.topframeright.pack(fill=X)
        self.recherchervhc = Entry(self.topframeright, font=("tahoma", 15), width=50)
        self.recherchervhc.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.rechercher = Button(self.topframeright, text="rechercher", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickrecherchevhc)
        self.rechercher.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.topframeright.grid_columnconfigure(0, weight=1)
        self.topframeright.grid_columnconfigure(1, weight=1)
        ########################frame tree view#######
        self.frameview=Frame(self.frameright)
        self.frameview.pack(fill=BOTH)
        self.table=ttk.Treeview(self.frameview,columns=("matricle","marque","prix par kilomètre","prix journalier"),show="headings")
        self.table.pack(fill=BOTH)
        self.table.heading("matricle",text="matricle")
        self.table.heading("marque", text="marque")
        self.table.heading("prix par kilomètre", text="prix par kilomètre")
        self.table.heading("prix journalier", text="prix journalier")
        self.table.column("matricle",anchor=W,width=15)
        self.table.column("marque",anchor=W,width=15)
        self.table.column("prix par kilomètre",anchor=W,width=15)
        self.table.column("prix journalier",anchor=W,width=15)









    def openmodifier(self):
            self.master = Toplevel()
            self.master.title("Modifier véhicules")
            self.master.geometry("1200x500+150+150")
            ##############################################
            self.frameleft = Frame(self.master, width=500)
            self.frameleft.pack(side=LEFT, fill=Y)
            ##################LABELS############################
            self.lbl2matricule = Label(self.frameleft, text="matricle", font=("tahoma", 15))
            self.lbl2matricule.place(x=20, y=30)
            self.lbl2marque = Label(self.frameleft, text="marque", font=("tahoma", 15))
            self.lbl2marque.place(x=20, y=90)
            self.lbl2ppk = Label(self.frameleft, text="prix par kilomètre", font=("tahoma", 15))
            self.lbl2ppk.place(x=20, y=150)
            self.lbl2pj = Label(self.frameleft, text="prix journalier", font=("tahoma", 15))
            self.lbl2pj.place(x=20, y=210)
            ##################ENTRIES############################
            self.modifmatricle = Entry(self.frameleft, text="matricle", font=("tahoma", 15))
            self.modifmatricle.place(x=200, y=30)
            self.modifmarque = Entry(self.frameleft, text="marque", font=("tahoma", 15))
            self.modifmarque.place(x=200, y=90)
            self.modifppk = Entry(self.frameleft, text="prix par kilomètre", font=("tahoma", 15))
            self.modifppk.place(x=200, y=150)
            self.modifpj = Entry(self.frameleft, text="prix journalier", font=("tahoma", 15))
            self.modifpj.place(x=200, y=210)
            ##################BUTTONS############################
            self.modifier = Button(self.frameleft, text="Modifier", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickmodifier)
            self.modifier.place(x=300, y=380)
            self.consulter = Button(self.frameleft, text="Consulter", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickconsulter)
            self.consulter.place(x=100, y=380)
            ################
            self.frameright = Frame(self.master, width=700)
            self.frameright.pack(side=RIGHT, fill=BOTH)
            self.topframeright=Frame(self.frameright,height=150,padx=5,pady=5,width=700)
            self.topframeright.pack(fill=X)
            self.recherchervhc = Entry(self.topframeright, font=("tahoma", 15),width=50)
            self.recherchervhc.grid(row=0,column=0,sticky="nsew",padx=10,pady=10)
            self.rechercher = Button(self.topframeright, text="rechercher", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickrecherchevhc)
            self.rechercher.grid(row=0,column=1,sticky="nsew",padx=10,pady=10)
            self.topframeright.grid_columnconfigure(0,weight=1)
            self.topframeright.grid_columnconfigure(1, weight=1)
            ########################frame tree view#######
            self.frameview = Frame(self.frameright)
            self.frameview.pack(fill=BOTH)
            self.table = ttk.Treeview(self.frameview,columns=("matricle", "marque", "prix par kilomètre", "prix journalier"),show="headings")
            self.table.pack(fill=BOTH)
            self.table.heading("matricle", text="matricle")
            self.table.heading("marque", text="marque")
            self.table.heading("prix par kilomètre", text="prix par kilomètre")
            self.table.heading("prix journalier", text="prix journalier")
            self.table.column("matricle", anchor=W, width=15)
            self.table.column("marque", anchor=W, width=15)
            self.table.column("prix par kilomètre", anchor=W, width=15)
            self.table.column("prix journalier", anchor=W, width=15)

    def opensupprimer(self):
            self.master = Toplevel()
            self.master.title("Supprimer véhicules")
            self.master.geometry("1200x500+150+150")
            ##############################################
            self.frameleft = Frame(self.master, width=500)
            self.frameleft.pack(side=LEFT, fill=Y)
            ##################LABELS############################
            self.lbl3matricule = Label(self.frameleft, text="matricle", font=("tahoma", 15))
            self.lbl3matricule.place(x=20, y=30)
            self.lbl3marque = Label(self.frameleft, text="marque", font=("tahoma", 15))
            self.lbl3marque.place(x=20, y=90)
            self.lbl3ppk = Label(self.frameleft, text="prix par kilomètre", font=("tahoma", 15))
            self.lbl3ppk.place(x=20, y=150)
            self.lbl3pj = Label(self.frameleft, text="prix journalier", font=("tahoma", 15))
            self.lbl3pj.place(x=20, y=210)
            ##################ENTRIES############################
            self.suppmatricle = Entry(self.frameleft, text="matricle", font=("tahoma", 15))
            self.suppmatricle.place(x=200, y=30)
            self.marque = Entry(self.frameleft, text="marque", font=("tahoma", 15))
            self.marque.place(x=200, y=90)
            self.ppk = Entry(self.frameleft, text="prix par kilomètre", font=("tahoma", 15))
            self.ppk.place(x=200, y=150)
            self.pj = Entry(self.frameleft, text="prix journalier", font=("tahoma", 15))
            self.pj.place(x=200, y=210)
            ##################BUTTONS############################
            self.supprimer = Button(self.frameleft, text="Supprimer", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clicksupprimervhc)
            self.supprimer.place(x=200, y=380)
            ################
            self.frameright = Frame(self.master, width=700)
            self.frameright.pack(side=RIGHT, fill=BOTH)
            self.topframeright=Frame(self.frameright,height=150,padx=5,pady=5,width=700)
            self.topframeright.pack(fill=X)
            self.recherchervhc = Entry(self.topframeright, font=("tahoma", 15),width=50)
            self.recherchervhc.grid(row=0,column=0,sticky="nsew",padx=10,pady=10)
            self.rechercher = Button(self.topframeright, text="rechercher", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickrecherchevhc)
            self.rechercher.grid(row=0,column=1,sticky="nsew",padx=10,pady=10)
            self.topframeright.grid_columnconfigure(0,weight=1)
            self.topframeright.grid_columnconfigure(1, weight=1)
            ########################frame tree view#######
            self.frameview = Frame(self.frameright)
            self.frameview.pack(fill=BOTH)
            self.table = ttk.Treeview(self.frameview,columns=("matricle", "marque", "prix par kilomètre", "prix journalier"),show="headings")
            self.table.pack(fill=BOTH)
            self.table.heading("matricle", text="matricle")
            self.table.heading("marque", text="marque")
            self.table.heading("prix par kilomètre", text="prix par kilomètre")
            self.table.heading("prix journalier", text="prix journalier")
            self.table.column("matricle", anchor=W, width=15)
            self.table.column("marque", anchor=W, width=15)
            self.table.column("prix par kilomètre", anchor=W, width=15)
            self.table.column("prix journalier", anchor=W, width=15)
