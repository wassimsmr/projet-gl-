class Client:
    def __init__(self, npermi, name , surname , birthday , birthplace ):
        self.npermi = npermi
        self.name = name
        self.surname = surname
        self.birthday= birthday
        self.birthplace = birthplace


class Vehicule:
    def __init__(self, mat, marque, prix_journalier, prix_kilometre):
        self.mat = mat
        self.marque = marque
        self.prix_journalier = prix_journalier
        self.prix_kilometre = prix_kilometre

class Reservation:
    def __init__(self,coderes,matricule,datedeb,duree,datefin):
        self.coderes=coderes
        self.matricule=matricule
        self.datedeb=datedeb
        self.duree=duree
        self.datefin=datefin

class Contrat :
    def __init__(self,coderes,npermi,matricule):
        self.coderes = coderes
        self.npermi = npermi
        self.matricule = matricule

class Utilisateur :
    def __init__(self,username,password,nom,prenom,adminflag):
        self.username=username
        self.password = password
        self.nom = nom
        self.prenom=prenom
        self.adminflag=adminflag

