##################################
# fichier 05-distance-obligatoire.py
# nom de l'exercice : Distance
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=9
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

from math import *

def distanceEuclidienne(x1, y1, x2, y2):
   distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
   return distance

distance = distanceEuclidienne(float(input()), float(input()), float(input()), float(input()))
print(distance)
