import sqlite3
from reservation_management import *


class Database:
    def __init__(self):
        """Creates connection to db upon object instantiation"""
        self.connection = sqlite3.connect('locdz.db')
        self.cr = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

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

        self.cr.execute("UPDATE contrats set npermi = ?, matricule = ?  WHERE coderes = ? ",
            (contrat.npermi, contrat.matricule,contrat.coderes))
        self.connection.commit()

    def init_facture(self, facture):
        self.cr.execute("INSERT INTO factures VALUES ")

    def ajouter_utilisateur(self, utilisateur):
        self.cr.execute("INSERT INTO utilisateurs(username,password,nom,prenom,adminflag) VALUES (?,?,?,?,?)",
                    (utilisateur.username, utilisateur.password, utilisateur.nom,utilisateur.prenom,utilisateur.adminflag))
        self.connection.commit()

    def afficher_utilisateur(self, username=''):
        if username == '' or len(username) == 0:
            self.cr.execute("SELECT * FROM utilisateurs")
        else:
            self.cr.execute("SELECT * FROM utilisateurs WHERE username = ?", (username,))
        return self.cr.fetchall()

    def supprimer_utilisateur(self, username):
        self.cr.execute("DELETE FROM utilisateurs WHERE username = ?", (username,))
        self.connection.commit()

    def modifier_utilisateur(self, utilisateur):

        self.cr.execute("UPDATE utilisateurs set password = ?, nom = ? , prenom = ? , adminflag = ? WHERE username = ? ",
                        (utilisateur.password, utilisateur.nom,utilisateur.prenom,utilisateur.adminflag,utilisateur.username))
        self.connection.commit()

    def get_vehicule(self, matricule):
        self.cr.execute("SELECT * FROM vehicules WHERE matricule = ?", (matricule,))
        res = self.cr.fetchone()
        return Vehicule(res[0], res[1], res[2], res[3])

    def ajouter_facture(self,  facture):
        self.cr.execute("INSERT INTO factures (date_init,date_fin, kilo_init, kilo_fin, etat, matricule) "
                        "VALUES(?,?,?,?,?,?)",
                        (facture.date_init, facture.date_fin, facture.kilo_init, facture.kilo_fin, facture.etat,
                         facture.vehicule.mat))
        self.connection.commit()

    def afficher_factures(self, code_fac):
        if len(code_fac) == 0:
            self.cr.execute("SELECT * FROM factures")
        else:
            self.cr.execute("SELECT * FROM factures WHERE code_fac = ?", code_fac)
        return self.cr.fetchall()

    def get_facture(self, code_fac):
        self.cr.execute("SELECT * FROM factures WHERE code_fac = ?", (code_fac,))
        res = self.cr.fetchone()
        return Facture(self.get_vehicule(res[6]), float(res[3]), res[1], code_fac)

    def final_facture(self, facture):
        self.cr.execute("UPDATE factures SET date_fin = ?, kilo_fin = ?, etat = 1, total = ?  WHERE code_fac = ?",
                        (facture.date_fin, facture.kilo_fin, facture.somme, facture.code_fact))
        self.connection.commit()

    def modifier_facture(self, facture):
        self.cr.execute("UPDATE factures SET date_init = ?, date_fin = ?, kilo_init=?, kilo_fin=?, etat=?, matricule=?,"
                        "total = ? WHERE code_fac = ?",
                        (facture.date_init, facture.date_fin, facture.kilo_init, facture.kilo_fin, facture.etat,
                         facture.vehicule.mat, facture.total(), facture.code_fact))
        self.connection.commit()

    def supprimer_facture(self, code_fac):
        self.cr.execute("DELETE FROM factures WHERE code_fac=?", code_fac)
        self.connection.commit()