##################################
# fichier 03b-fiches-d-inscription-obligatoire.py
# nom de l'exercice : Fiches d’inscription
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=14
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

nbPersonnes = int(input())

for loop in range(nbPersonnes):
   nom = input()
   decoupe = nom.split(" ")
   print(decoupe[1], end = " ")
   print(decoupe[0])
