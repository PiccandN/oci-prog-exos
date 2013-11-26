##################################
# fichier 07-repartition-du-poids-obligatoire.py
# nom de l'exercice : Répartition du poids
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=10
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

from math import *

nbCharrettes = int(input())
poidsCharrette = [0] * nbCharrettes
somme = 0

for numCharrette in range(nbCharrettes):
    poids = float(input())
    poidsCharrette[numCharrette] = poids
    somme += poids

moyenne = somme / nbCharrettes

for numCharrette in range(nbCharrettes):
    print(moyenne - poidsCharrette[numCharrette])
