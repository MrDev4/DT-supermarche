"""

"""

liste_articles = []
run = True

while run:
    print("Ajouter un article au panier")
    designation = str(input("Entrer la designation: "))
    quantite = int(input("Quantité: "))
    prix_u = int(input("Prix unitaire: "))
    article = {"designation": designation, "quantite": quantite, "prix_u": prix_u, "prix_t":prix_u*quantite}
    liste_articles.append(article)
    continuer = int(input("Taper 1 pour ajouter et 0 pour terminer: "))
    if(continuer == 0):
        run = False

#Calcul du montant total
montant_total = 0
for article in liste_articles:
    montant_total += article['prix_t']

print("Montant total :", montant_total)
montant_client = int(input('Combien le client verse ? : '))
monaie = montant_client - montant_total
print('La monaie du client: ', monaie)