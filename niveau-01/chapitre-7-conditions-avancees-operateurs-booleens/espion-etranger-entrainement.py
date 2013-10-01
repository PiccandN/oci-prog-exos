##################################
# fichier espion-etranger-entrainement.py
# nom de l'exercice :  Espion étranger
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=1
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

date_debut=int(input())
date_fin=int(input())
nbEntrees=int(input())
nbSuspects=0

for loop in range(nbEntrees):
   date_entree=int(input())
   
   if (date_entree >= date_debut) and (date_entree <= date_fin):
      nbSuspects=nbSuspects+1
print(nbSuspects)
