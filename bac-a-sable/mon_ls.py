import os
import sys
from datetime import datetime

def taille(n):
    for i, u in enumerate(("o", "Ko", "Mo", "Go")):
        if n < 1024 ** (i + 1):
            return f"{n / 1024 ** i:.1f} {u}"
    return f"{n / 1024 ** 3:.1f} Go"

if len(sys.argv) < 2:
    print("Usage : python3 mon_ls.py <dossier>")
    sys.exit(1)

dossier = sys.argv[1]

if not os.path.isdir(dossier):
    print(f"Erreur : '{dossier}' n'est pas un dossier.")
    sys.exit(1)

for nom in sorted(os.listdir(dossier)):
    chemin = os.path.join(dossier, nom)
    est_dossier = os.path.isdir(chemin)

    if est_dossier:
        type_ = "d"
        taille_str = "-"
    else:
        type_ = "-"
        taille_str = taille(os.path.getsize(chemin))

    date = datetime.fromtimestamp(os.path.getmtime(chemin))
    date_str = date.strftime("%d/%m/%Y %H:%M")

    print(f"{type_} {taille_str:>10} {date_str}  {nom}")   
