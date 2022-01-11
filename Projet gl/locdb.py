import sqlite3
from reservation_management import Client, Vehicule


class Database:
    def __init__(self):
        """Creates connection to db upon object instantiation"""
        self.connection = sqlite3.connect('locdz.db')
        self.cr = self.connection.cursor()

    def close(self):
        """Closes connection to database"""
        self.connection.close()

    """ Gestion des clients"""
    def add_client(self, client):
        """Ajouter client a la table"""
        self.cr.execute("INSERT INTO clients(npermi,name,surname,birthday,birthplace) VALUES(?,?,?,?,?)", (client.npermi, client.name,client.surname,client.birthday,client.birthplace))
        self.connection.commit()

    def afficher_clients(self, npermi=0):
        """Aficher tout les clients"""
        if npermi == 0 or len(npermi) == 0 :
            self.cr.execute("SELECT * FROM clients")
        else:
            self.cr.execute("SELECT * FROM clients WHERE npermi = ?", (npermi,))
        return self.cr.fetchall()

    def supprimer_client(self, npermi):
        """supprimer le client"""
        self.cr.execute("DELETE FROM clients WHERE npermi = ?", (npermi,))
        self.connection.commit()
    def modifier_client(self, client):
        self.cr.execute("UPDATE clients set name = ?, surname = ?, birthday = ? , birthplace = ? WHERE npermi = ? ",
                        (client.name, client.surname, client.birthday, client.birthplace,client.npermi))
        self.connection.commit()


    """gestion vehicules"""
    def ajouter_vehicule(self, vehicule):
        self.cr.execute("INSERT INTO vehicules(matricule, marque, prix_journalier, prix_kilometre) VALUES (?,?,?,?)",
                        (vehicule.mat, vehicule.marque, vehicule.prix_journalier, vehicule.prix_kilometre))
        self.connection.commit()

    def afficher_vehicules(self, matricule=0):
        if matricule == 0 or len(matricule) == 0:
            self.cr.execute("SELECT * FROM vehicules")
        else:
            self.cr.execute("SELECT * FROM vehicules WHERE matricule = ?", (matricule,))
        return self.cr.fetchall()

    def supprimer_vehicule(self, matricule):
        self.cr.execute("DELETE FROM vehicules WHERE matricule = ?", (matricule,))
        self.connection.commit()

    def modifier_vehicule(self, vehicule):
        self.cr.execute("UPDATE vehicules set marque = ?, prix_journalier = ?, prix_kilometre = ? WHERE matricule = ? ",
                        (vehicule.marque, vehicule.prix_journalier, vehicule.prix_kilometre, vehicule.mat))
        self.connection.commit()


    def ajouter_reservation(self,reservation):
        self.cr.execute("INSERT INTO reservations(coderes, matricule, datedeb, duree , datefin) VALUES (?,?,?,?,?)",
                        (reservation.coderes, reservation.matricule, reservation.datedeb, reservation.duree,reservation.datefin))
        self.connection.commit()

    def afficher_reservation(self, coderes=0):
        if coderes == 0 or len(coderes) == 0:
            self.cr.execute("SELECT * FROM reservations")
        else:
            self.cr.execute("SELECT * FROM reservations WHERE coderes = ?", (coderes,))
        return self.cr.fetchall()

    def supprimer_reservation(self, coderes):
        self.cr.execute("DELETE FROM reservations WHERE coderes = ?", (coderes,))
        self.connection.commit()

    def modifier_reservation(self, reservation):

        self.cr.execute("UPDATE reservations set matricule = ?, datedeb = ?, duree = ? , datefin = ? WHERE coderes = ? ",
                        (reservation.matricule, reservation.datedeb, reservation.duree, reservation.datefin,reservation.coderes))
        self.connection.commit()

    def ajouter_contrat(self, contrat):
        self.cr.execute("INSERT INTO contrats(coderes,npermi, matricule) VALUES (?,?,?)",
                        ( contrat.coderes,contrat.npermi,contrat.matricule))
        self.connection.commit()

    def afficher_contrat(self, coderes=0):
        if coderes == 0 or len(coderes) == 0:
            self.cr.execute("SELECT * FROM contrats")
        else:
            self.cr.execute("SELECT * FROM contrats WHERE coderes = ?", (coderes,))
        return self.cr.fetchall()

    def supprimer_contrat(self, coderes):
        self.cr.execute("DELETE FROM contrats WHERE coderes = ?", (coderes,))
        self.connection.commit()

    def modifier_contrat(self, contrat):

        self.cr.execute(
            "UPDATE contrats set npermi = ?, matricule = ?  WHERE coderes = ? ",
            (contrat.npermi, contrat.matricule,contrat.coderes))
        self.connection.commit()
