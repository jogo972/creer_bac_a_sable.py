import os

DOSSIER = "/home/jogo/Python/bac-a-sable"

def taille(n):
    for i, u in enumerate(("o", "Ko", "Mo", "Go")):
        if n < 1024 ** (i + 1):
            return f"{n / 1024 ** i:.1f} {u}"
    return f"{n / 1024 ** 3:.1f} Go"

total = 0
plus_gros = 0
plus_gros_nom = ""

for nom in os.listdir(DOSSIER):
    chemin = os.path.join(DOSSIER, nom)
    if os.path.isfile(chemin):
        octets = os.path.getsize(chemin)

        total += octets

        if octets > plus_gros:
            plus_gros = octets
            plus_gros_nom = nom

print(f"Total : {total} octets ({total / 1024**2:.2f} Mo)")
print(f"Plus gros : {plus_gros_nom} ({taille(plus_gros)})")   
import os

DOSSIER = "/home/jogo/Python/bac-a-sable"

compteur = {}

for nom in os.listdir(DOSSIER):
    if os.path.isfile(chemin) and nom.endswith(".txt"):   
    if os.path.isfile(chemin):
        ext = os.path.splitext(nom)[1]
        compteur[ext] = compteur.get(ext, 0) + 1

for ext, nb in sorted(compteur.items()):
    print(f"{ext:10} {nb}")   
