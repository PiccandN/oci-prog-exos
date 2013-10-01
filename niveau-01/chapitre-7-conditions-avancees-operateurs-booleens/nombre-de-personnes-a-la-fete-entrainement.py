##################################
# fichier nombre-de-personnes-a-la-fete-entrainement.py
# nom de l'exercice :  Nombre de personnes à la fête
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=6
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

nbPersonnes=int(input())
nbMax=0
nbActuel=0

for loop in range(2*nbPersonnes):
   situation_personne=int(input())
   
   if situation_personne>0:
      nbActuel=nbActuel+1
   else:
      nbActuel=nbActuel-1
   if nbActuel>nbMax:
      nbMax=nbActuel
print(nbMax)
