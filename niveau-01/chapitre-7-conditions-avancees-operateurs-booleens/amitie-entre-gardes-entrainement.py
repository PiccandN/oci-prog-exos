##################################
# fichier amitie-entre-gardes-entrainement.py
# nom de l'exercice :  Amitié entre gardes
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=5
# type : entrainement
#
# Nom du chapitre : 
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

debutsoldat1=int(input())
finsoldat1=int(input())
debutsoldat2=int(input())
finsoldat2=int(input())

if (finsoldat2<debutsoldat1) or (finsoldat1<debutsoldat2):
   print("Pas amis")
else:
   print("Amis")
