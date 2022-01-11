

from tkinter import *

import véhicule as v
import client as cli
import reservation as res
import facture as fac
import utilisateur as u
import contrat as con



class mainmenu:
    def __init__(self,window):
        self.master=window
        self.master.title("LocDz")
        self.width=self.master.winfo_screenwidth()
        self.height=self.master.winfo_screenheight()
        self.master.geometry("{w}x{h}+0+0".format(w=self.width,h=self.height))
        self.master.state("zoomed")
        ###top frame start here ###
        self.frametop=Frame(self.master,bg="#1b9ea4",height=150)
        self.frametop.pack(fill=X)
        self.ldz=Label(self.frametop,text="LocDz",bg="#1b9ea4",fg="white",font=("tahoma",50),pady=50)
        self.ldz.pack()
        ###top frame end here ###
        ###centre frame start here ###
        self.centreframe=Frame(self.master,bg="white")
        self.centreframe.pack(fill=X)
        ###frame gestion véhicule ###
        vhc = v.vehicule(self.centreframe)
        ###frame gestion clients ###
        clie = cli.client(self.centreframe)
        ####frame gestion réservation ###
        reserv = res.reservation(self.centreframe)
        self.centreframe.grid_columnconfigure(0, weight=1)
        self.centreframe.grid_columnconfigure(1, weight=1)
        self.centreframe.grid_columnconfigure(2, weight=1)
        # centre frame end here #

        # bottom frame start here
        self.bottomframe = Frame(self.master, bg="white", height=200)
        self.bottomframe.pack(fill=X)
        ###frame gestion facture ###
        fct = fac.facture(self.bottomframe)
        ###frame gestion contrat ###
        cntr = con.contrat(self.bottomframe)
        ############frame gestion utilisateur ###########
        utili = u.utilisateur(self.bottomframe)
        self.bottomframe.grid_columnconfigure(0, weight=1)
        self.bottomframe.grid_columnconfigure(1, weight=1)
        self.bottomframe.grid_columnconfigure(2, weight=1)
        ###bottom frame end here ###






























if (__name__ == '__main__'):
    window = Tk()
    std = mainmenu(window)

    mainloop()