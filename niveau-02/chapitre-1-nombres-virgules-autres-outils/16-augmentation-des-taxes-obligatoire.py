##################################
# fichier 16-augmentation-des-taxes-obligatoire.py
# nom de l'exercice : Augmentation des taxes
# url : http://www.france-ioi.org/algo/task.php?idChapter=650&idTask=0&sTab=task&iOrder=20
# type : obligatoire
#
# Chapitre : chapitre-1-nombres-virgules-autres-outils
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

from math import *

taxeActuelle = float(input())
taxeNouvelle = float(input())
prixActuel = float(input())

prixNouveau = ((prixActuel / (1 + taxeActuelle/100)) * (1 + taxeNouvelle/100))

print(round(prixNouveau*100)/100)
