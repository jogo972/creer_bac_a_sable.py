montant = int(input("Montant à payer : "))
billet = 50

if montant > billet:
    print("Le billet de 50 € ne suffit pas !")
else:
    monnaie = billet - montant
    print(f"Rendu : {monnaie} €")

    for valeur in [20, 10, 5, 2, 1]:
        nb = monnaie // valeur
        if nb > 0:
            if valeur >= 5:
                print(f"{nb} billet(s) de {valeur} €")
            else:
                print(f"{nb} pièce(s) de {valeur} €")
        monnaie = monnaie % valeur   