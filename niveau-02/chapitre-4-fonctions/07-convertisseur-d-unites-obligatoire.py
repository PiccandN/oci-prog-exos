##################################
# fichier 07-convertisseur-d-unites-obligatoire.py
# nom de l'exercice : Convertisseur d'unités
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=14
# type : obligatoire
#
# Chapitre : chapitre-4-fonctions
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nbValeurs = int(input())
quantite = [0] * nbValeurs
unites = [0] * nbValeurs

for idValeur in range(nbValeurs):
   quantite[idValeur], unites[idValeur] = input().split(" ")
   quantite[idValeur] = float(quantite[idValeur])


for idValeur in range(nbValeurs):
   if unites[idValeur] == "m":
      quantite[idValeur] /= 0.3048
      print("{} p".format(quantite[idValeur]))
   
   elif unites[idValeur] == "g":
      quantite[idValeur] *= 0.002205
      print("{} l".format(quantite[idValeur]))
   
   elif unites[idValeur] == "c":
      quantite[idValeur] = (quantite[idValeur] * 1.8) + 32
      print("{} f".format(quantite[idValeur]))
