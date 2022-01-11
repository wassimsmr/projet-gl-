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
        self.cr.execute("INSERT INTO clients(mat,name) VALUES(?,?)", (client.mat, client.name))
        self.connection.commit()

    def afficher_clients(self, npermi=0):
        """Aficher tout les clients"""
        if npermi == 0:
            self.cr.execute("SELECT * FROM clients")
        else:
            self.cr.execute("SELECT * FROM clients WHERE matricule = ?", (npermi,))
        return self.cr.fetchall()

    def supprimer_client(self, matricule):
        """supprimer le client"""
        self.cr.execute("DELETE FROM clients WHERE mat = ?", (matricule,))

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
