from datetime import datetime


class Client:
    def __init__(self, npermi, name, surname, birthday, birthplace):
        self.npermi = npermi
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.birthplace = birthplace


class Vehicule:
    def __init__(self, mat, marque, prix_journalier, prix_kilometre):
        self.mat = mat
        self.marque = marque
        self.prix_journalier = prix_journalier
        self.prix_kilometre = prix_kilometre


class Reservation:
    def __init__(self, coderes, matricule, datedeb, duree, datefin):
        self.coderes = coderes
        self.matricule = matricule
        self.datedeb = datedeb
        self.duree = duree
        self.datefin = datefin


class Contrat:
    def __init__(self, coderes, npermi, matricule):
        self.coderes = coderes
        self.npermi = npermi
        self.matricule = matricule


class Facture:
    def __init__(self, vehicule, kilo_init, date_init, code_fact=0, etat=0, kilo_fin=0.0, date_fin='', somme=0):
        self.code_fact = code_fact
        self.vehicule = vehicule
        self.kilo_init = kilo_init
        self.date_init = date_init
        self.etat = etat
        self.kilo_fin = kilo_fin
        self.date_fin = date_fin
        self.somme = somme

    def finaliser_facture(self, kilo_fin, date_fin):
        self.kilo_fin = kilo_fin
        self.date_fin = date_fin
        self.somme = self.total()

    def total(self):
        date_deb = datetime.strptime(self.date_init, '%Y-%m-%d')
        date_end = datetime.strptime(self.date_fin, '%Y-%m-%d')

        date_dif = abs(date_deb-date_end).days
        print(date_dif)
        kilo_dif = self.kilo_fin-self.kilo_init
        print(kilo_dif)
        return self.vehicule.prix_journalier * date_dif + self.vehicule.prix_kilometre * kilo_dif


class Utilisateur:
    def __init__(self,username,password,nom,prenom,adminflag):
        self.username = username
        self.password = password
        self.nom = nom
        self.prenom=prenom
        self.adminflag=adminflag


