class Client:
    def __init__(self, name, npermi):
        self.npermi = npermi
        self.name = name


class Vehicule:
    def __init__(self, mat, marque, prix_journalier, prix_kilometre):
        self.mat = mat
        self.marque = marque
        self.prix_journalier = prix_journalier
        self.prix_kilometre = prix_kilometre

