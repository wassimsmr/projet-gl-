import sqlite3

from locdb import Database
from reservation_management import *

c1 = Client('Fathi', 1353)
db = Database()
# # db.add_client(c1)
# db.afficher_clients()
#
# rch = db.rechererch_client(1234)
# print(rch)
#
# db.supprimer_client(1234)
# db.afficher_clients()

v1 = Vehicule(3123, 'Toyota', 200.0, 100.0)
try:
    db.ajouter_vehicule(v1)
    print("ajoute")
except sqlite3.IntegrityError:
    print("vehicule exist")


resultat = db.afficher_vehicules(3123)

print(resultat if resultat else "Aucune resultat")

for r in resultat:
   print(f'')

