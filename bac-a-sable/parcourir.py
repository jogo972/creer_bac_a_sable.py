import os

DOSSIER = "/home/jogo/Python/bac-a-sable"

nb_fichiers = 0
nb_dossiers = 0
total = 0

for chemin, sous_dossiers, fichiers in os.walk(DOSSIER):
    sous_dossiers.sort()

    print(chemin)
    nb_dossiers += 1

    for nom in fichiers:
        f = os.path.join(chemin, nom)
        octets = os.path.getsize(f)
        total += octets
        nb_fichiers += 1
        print(f"  {nom:15} {octets:>10}")

print(f"\nFichiers : {nb_fichiers}")
print(f"Dossiers : {nb_dossiers}")
print(f"Total    : {total / 1024**2:.2f} Mo")   
