import os
from datetime import datetime

DOSSIER = "/home/jogo/Python/bac-a-sable"
limite = datetime(2026, 10, 1)

for chemin, sous_dossiers, fichiers in os.walk(DOSSIER):
    sous_dossiers.sort()
    for nom in fichiers:
        f = os.path.join(chemin, nom)
        mtime = os.path.getmtime(f)
        date = datetime.fromtimestamp(mtime)
        if date >= limite:
            print(f"{f}  {date.strftime('%d/%m/%Y %H:%M')}")   
