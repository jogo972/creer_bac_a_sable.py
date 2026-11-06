import os

DOSSIER = "/home/jogo/Python/bac-a-sable"

for nom in os.listdir(DOSSIER):
    chemin = os.path.join(DOSSIER, nom)
    if os.path.isfile(chemin) and nom.endswith(".txt"):
        octets = os.path.getsize(chemin)
        print(f"{nom:15} {octets:>10}")   
