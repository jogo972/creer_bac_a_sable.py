import os

DOSSIER = "/home/jogo/Python/bac-a-sable"

compteur = {}

for nom in os.listdir(DOSSIER):
    chemin = os.path.join(DOSSIER, nom)
    if os.path.isfile(chemin):
        ext = os.path.splitext(nom)[1]
        compteur[ext] = compteur.get(ext, 0) + 1

for ext, nb in sorted(compteur.items()):
    print(f"{ext:10} {nb}")   
