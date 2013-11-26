##################################
# fichier 13-choix-des-emplacements-obligatoire.py
# nom de l'exercice : Choix des emplacements
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=18
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

nbEmplacements = int(input())
numeroEmplacement = [0] * nbEmplacements
 
for idEmplacement in range(nbEmplacements):
   marchand = int(input())
   numeroEmplacement[marchand] = idEmplacement
 
for marchand in range(nbEmplacements):
   print(numeroEmplacement[marchand])
