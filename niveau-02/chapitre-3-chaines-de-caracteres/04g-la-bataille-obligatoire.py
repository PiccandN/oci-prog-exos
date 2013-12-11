##################################
# fichier 04g-la-bataille-obligatoire.py
# nom de l'exercice : La bataille
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=24
# type : obligatoire
#
# Chapitre : chapitre-3-chaines-de-caracteres
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

cartes1 = input()
cartes2 = input()
victoire = False
nbTours = 0

if cartes1 < cartes2:
   longueur = len(cartes1)
else:
   longueur = len(cartes2)

while victoire == False and longueur > nbTours:
   if cartes1[nbTours] == cartes2[nbTours]:
      nbTours += 1
   elif cartes1[nbTours] < cartes2[nbTours]:
      print(1)
      victoire = True
   elif cartes1[nbTours] > cartes2[nbTours]:
      print(2)
      victoire = True

if victoire == False:
   if len(cartes1) < len(cartes2):
      print(2)
   elif len(cartes1) > len(cartes2):
      print(1)
   elif len(cartes1) == len(cartes2):
      print("=")

print(nbTours)
