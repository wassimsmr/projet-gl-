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
    def __init__(self, matricule, kilo_init, date_init):
        self.matricule = matricule
        self.kilo_init = kilo_init
        self.date_init = date_init
        self.etat = 0
        self.kilo_fin = 0.0
        self.date_fin = ''

    def finaliser_facture(self, code_fact, kilo_fin, date_fin):
        self.kilo_fin = kilo_fin
        self.date_fin = date_fin

    def total(self, prix_j, prix_k):
        date_deb = datetime.strptime(self.date_init, '%Y-%m-%d')
        date_end = datetime.strptime(self.date_fin, '%Y-%m-%d')

        date_dif = abs(date_deb-date_end).days
        print(date_dif)
        kilo_dif = self.kilo_fin-self.kilo_init
        print(kilo_dif)
        return prix_j * date_dif + prix_k * kilo_dif
