##################################
# fichier 04c-ecriture-en-miroir-obligatoire.py
# nom de l'exercice : Écriture en miroir
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=20
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

nbLignes = int(input())

for loop in range(nbLignes):

   ligne = input()
   longueur = len(ligne)

   for loop in range(len(ligne)):
      print(ligne[longueur - 1], end = "")
      longueur -= 1
   print("")
