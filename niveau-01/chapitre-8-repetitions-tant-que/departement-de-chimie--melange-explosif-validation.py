##################################
# fichier departement-de-chimie--melange-explosif-validation.py
# nom de l'exercice :  Département de chimie : mélange explosif
# url : http://www.france-ioi.org/algo/task.php?idChapter=649&idTask=0&sTab=task&iOrder=7
# type : validation
#
# Nom du chapitre : 
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nbMesuresTotal=int(input())
tMin=int(input())
tMax=int(input())
temperature=int(input())
nbMesures=0

while temperature>=tMin and temperature<=tMax and nbMesures<nbMesuresTotal:
   print("Rien à signaler")
   nbMesures=nbMesures+1
   if nbMesures<nbMesuresTotal:
      temperature=int(input())

if temperature<tMin or temperature>tMax:
   print("Alerte !!")
