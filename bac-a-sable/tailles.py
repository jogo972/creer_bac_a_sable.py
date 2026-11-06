import os

dossier = "."   
elements = sorted(os.listdir("."))

print(f"{'Nom':15} {'Taille (octets)':>10}")
print("-" * 27)

for e in elements:
    chemin = os.path.join(dossier, e)
    if os.path.isfile(chemin):
        taille = os.path.getsize(chemin)
        print(f"{e:15} {taille:>10}")   