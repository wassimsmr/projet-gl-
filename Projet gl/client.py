import sqlite3
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from locdb import Database
from reservation_management import *
from tkinter import messagebox

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

    def clickajouterclient(self):
        db = Database()
        num1 = self.num.get()
        name1 = self.name.get()
        surname1 = self.surname.get()
        birthday1 = self.birthday.get()
        birthplace1 = self.birthplace.get()
        c1 = Client(num1, name1, surname1, birthday1,birthplace1)
        try:
            db.add_client(c1)
            messagebox.showinfo("Confirmation", "Véhicule ajouté")
        except sqlite3.IntegrityError:
            messagebox.showerror("Erreur", "Véhicule existant")

    def clickrechercheclient(self):
            db = Database()
            rechcl = self.rechercherclient.get()
            resultats = db.afficher_clients(rechcl)
            for res in resultats:
                self.table.insert('', 'end', values=res)

    def clicksupprimerclient(self):
        db=Database()
        num3 = self.num.get()
        try:
            db.supprimer_client(num3)
            messagebox.showinfo("Confirmation", "Véhicule supprimé")
        except sqlite3.IntegrityError:
            messagebox.showerror("Erreur", "Véhicule existant")

    def clickmodifierclient(self):
        db=Database()
        num2 = self.num.get()
        name2 = self.name.get()
        surname2 = self.surname.get()
        birthday2 = self.birthday.get()
        birthplace2 = self.birthplace.get()
        c2 = Client(num2, name2, surname2, birthday2, birthplace2)
        db.modifier_client(c2)
        messagebox.showinfo("Confirmation", "Donnee modifiés")

    def clickconsulterclient(self):
        db = Database()
        num2 = self.num.get()
        resultats2 = db.afficher_clients(num2)
        # delete pour vider la zone d'ecriture, insert pour inserer les nouvelles données
        self.name.delete(0, END)
        self.name.insert(0, ''+resultats2[0][1])

        self.surname.delete(0, END)
        self.surname.insert(0, ''+str(resultats2[0][2]))

        self.birthday.delete(0, END)
        self.birthday.insert(0, ''+str(resultats2[0][3]))

        self.birthplace.delete(0, END)
        self.birthplace.insert(0, '' + str(resultats2[0][4]))



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

        ###frame ajouter véhicule ###
        self.gestionclients2 = Frame(self.centreframe2, bg="white", pady=50, padx=30)
        self.gestionclients2.grid(row=0, column=0)
        self.btnclient2 = Button(self.gestionclients2, text="Ajouter client", bg="#1b9ea4", fg="white", padx=10,pady=10, font=("tahoma", 15), command=self.openajouter)
        self.btnclient2.pack()
        ###frame modifier véhicule ###
        self.gestionclients2 = Frame(self.centreframe2, bg="white", pady=50, padx=30)
        self.gestionclients2.grid(row=0, column=1)
        self.btnclient2 = Button(self.gestionclients2, text="Modifier client", bg="#1b9ea4", fg="white", padx=10, pady=10, font=("tahoma", 15), command=self.openmodifier)
        self.btnclient2.pack()
        self.centreframe2.grid_columnconfigure(0, weight=1)
        self.centreframe2.grid_columnconfigure(1, weight=1)
        self.centreframe2.grid_columnconfigure(2, weight=1)

        ###frame supprimer véhicule ###
        self.gestionclients2 = Frame(self.centreframe2, bg="white", pady=50, padx=30)
        self.gestionclients2.grid(row=0, column=2)
        self.btnclient2 = Button(self.gestionclients2, text="Supprimer client", bg="#1b9ea4", fg="white", padx=10,pady=10, font=("tahoma", 15), command=self.opensupprimer)
        self.btnclient2.pack()


    def openajouter(self):
        self.master = Toplevel()
        self.master.title("Ajouter un client")
        self.master.geometry("1200x500+150+150")
        ##############################################
        self.frameleft = Frame(self.master, width=500)
        self.frameleft.pack(side=LEFT, fill=Y)
        ##################LABELS############################
        self.lblNum = Label(self.frameleft, text="Num permis", font=("tahoma", 15))
        self.lblNum.place(x=20, y=30)
        self.lblname = Label(self.frameleft, text="Nom", font=("tahoma", 15))
        self.lblname.place(x=20, y=90)
        self.lblsurname = Label(self.frameleft, text="Prénom", font=("tahoma", 15))
        self.lblsurname.place(x=20, y=150)
        self.lblbirthday = Label(self.frameleft, text="Date de naissance", font=("tahoma", 15))
        self.lblbirthday.place(x=20, y=210)
        self.lblbirthplace = Label(self.frameleft, text="Lieu de naissance", font=("tahoma", 15))
        self.lblbirthplace.place(x=20, y=270)
        ##################ENTRIES############################
        self.num = Entry(self.frameleft, font=("tahoma", 15))
        self.num.place(x=200, y=30)
        self.name = Entry(self.frameleft,font=("tahoma", 15))
        self.name.place(x=200, y=90)
        self.surname = Entry(self.frameleft, font=("tahoma", 15))
        self.surname.place(x=200, y=150)
        self.birthday = Entry(self.frameleft,  font=("tahoma", 15))
        self.birthday.place(x=200, y=210)
        self.birthplace = Entry(self.frameleft,  font=("tahoma", 15))
        self.birthplace.place(x=200, y=270)
        ##################BUTTONS############################
        self.ajouter = Button(self.frameleft, text="ajouter", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickajouterclient)
        self.ajouter.place(x=200, y=380)
        ###########################
        self.frameright = Frame(self.master, width=700)
        self.frameright.pack(side=RIGHT, fill=BOTH)
        self.topframeright = Frame(self.frameright, height=150, padx=5, pady=5, width=700)
        self.topframeright.pack(fill=X)
        self.rechercherclient = Entry(self.topframeright, font=("tahoma", 15), width=50)
        self.rechercherclient.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.rechercher = Button(self.topframeright, text="rechercher", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickrechercheclient)
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
        self.num = Entry(self.frameleft, text="matricle", font=("tahoma", 15))
        self.num.place(x=200, y=30)
        self.name = Entry(self.frameleft, text="marque", font=("tahoma", 15))
        self.name.place(x=200, y=90)
        self.surname = Entry(self.frameleft, text="modele", font=("tahoma", 15))
        self.surname.place(x=200, y=150)
        self.birthday = Entry(self.frameleft, text="prix par kilomètre", font=("tahoma", 15))
        self.birthday.place(x=200, y=210)
        self.birthplace = Entry(self.frameleft, text="prix journalier", font=("tahoma", 15))
        self.birthplace.place(x=200, y=270)
        ##################BUTTONS############################
        self.modifier = Button(self.frameleft, text="Modifier", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickmodifierclient)
        self.modifier.place(x=300, y=380)
        self.consulter = Button(self.frameleft, text="Consulter", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickconsulterclient)
        self.consulter.place(x=100, y=380)
        ################
        self.frameright = Frame(self.master, width=700)
        self.frameright.pack(side=RIGHT, fill=BOTH)
        self.topframeright = Frame(self.frameright, height=150, padx=5, pady=5, width=700)
        self.topframeright.pack(fill=X)
        self.recherchervhc = Entry(self.topframeright, font=("tahoma", 15), width=50)
        self.recherchervhc.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.rechercher = Button(self.topframeright, text="rechercher", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickrechercheclient)
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
        self.num = Entry(self.frameleft, text="matricle", font=("tahoma", 15))
        self.num.place(x=200, y=30)
        self.marque = Entry(self.frameleft, text="marque", font=("tahoma", 15))
        self.marque.place(x=200, y=90)
        self.modele = Entry(self.frameleft, text="modele", font=("tahoma", 15))
        self.modele.place(x=200, y=150)
        self.ppk = Entry(self.frameleft, text="prix par kilomètre", font=("tahoma", 15))
        self.ppk.place(x=200, y=210)
        self.pj = Entry(self.frameleft, text="prix journalier", font=("tahoma", 15))
        self.pj.place(x=200, y=270)
        ##################BUTTONS############################
        self.supprimer = Button(self.frameleft, text="Supprimer", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clicksupprimerclient)
        self.supprimer.place(x=200, y=380)
        ################
        self.frameright = Frame(self.master, width=700)
        self.frameright.pack(side=RIGHT, fill=BOTH)
        self.topframeright = Frame(self.frameright, height=150, padx=5, pady=5, width=700)
        self.topframeright.pack(fill=X)
        self.rechercherclient = Entry(self.topframeright, font=("tahoma", 15), width=50)
        self.rechercherclient.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.rechercher = Button(self.topframeright, text="rechercher", bg="#1b9ea4", fg="white", font=("tahoma", 15),command=self.clickrechercheclient)
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

