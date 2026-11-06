import os

DOSSIER = "/home/jogo/Python/bac-a-sable"

for chemin, sous_dossiers, fichiers in os.walk(DOSSIER):
    sous_dossiers.sort()

    for nom in fichiers:
        f = os.path.join(chemin, nom)
        if os.path.getsize(f) == 0:
            print(f"FICHIER VIDE : {f}")

    if not sous_dossiers and not fichiers:
        print(f"DOSSIER VIDE   : {chemin}")   
