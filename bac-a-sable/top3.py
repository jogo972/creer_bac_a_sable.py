import os

DOSSIER = "/home/jogo/Python/bac-a-sable"

fichiers = []

for nom in os.listdir(DOSSIER):
    chemin = os.path.join(DOSSIER, nom)
    if os.path.isfile(chemin):
        octets = os.path.getsize(chemin)
        fichiers.append((octets, nom))

for octets, nom in sorted(fichiers, reverse=True)[:3]:
    print(f"{nom:15} {octets:>10}")   
