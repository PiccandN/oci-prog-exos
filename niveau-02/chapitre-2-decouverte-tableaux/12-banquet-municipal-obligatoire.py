##################################
# fichier 12-banquet-municipal-obligatoire.py
# nom de l'exercice : Banquet municipal
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=17
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

nbPositions = int(input())
nbChangements = int(input())
personne = [0] * nbPositions
changement = [0] * nbPositions

for idPersonne in range(nbPositions):
   personne[idPersonne] = int(input())

for loop in range(nbChangements):
   position1 = int(input())
   position2 = int(input())
   changement[position1] = personne[position2]
   changement[position2] = personne[position1]
   personne[position1] = changement[position1]
   personne[position2] = changement[position2]

for resultat in range(nbPositions):
   print(personne[resultat])
