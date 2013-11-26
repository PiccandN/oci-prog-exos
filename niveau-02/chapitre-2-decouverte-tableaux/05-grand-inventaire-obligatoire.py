##################################
# fichier 05-grand-inventaire-obligatoire.py
# nom de l'exercice : Grand inventaire
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=7
# type : obligatoire
#
# Chapitre : chapitre-2-decouverte-tableaux
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nbOperations = int(input())
produit = [0] * 10

for loop in range(nbOperations):
    nIngredient = int(input())-1
    quantite = int(input())
    produit[nIngredient] += quantite

for nProduit in range(10):
    print(produit[nProduit])
