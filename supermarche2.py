"""

"""
print("Bienvenu, veillez remplire le panier")

run = True
montant_total = 0
while run:
    print("Ajouter un article au panier")
    designation = str(input("Entrer la designation: "))
    quantite = int(input("Quantité: "))
    prix_u = int(input("Prix unitaire: "))
    montant_total += prix_u*quantite
    continuer = int(input("Taper 1 pour ajouter et 0 pour terminer: "))
    if(continuer == 0):
        run = False

print("Montant total :", montant_total)
montant_client = int(input('Combien le client verse ? : '))
monaie = montant_client - montant_total
print('La monaie du client: ', monaie)