##################################
# fichier la-grande-fete-entrainement.py
# nom de l'exercice :  La grande fête
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=11
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

dateDebut=int(input())
dateFin=int(input())
nbInvites=int(input())
nbSuspects=0

for loop in range(nbInvites):
   dateArrivee=int(input())
   dateDepart=int(input())
   
   if (dateArrivee>dateFin) or (dateDepart<dateDebut):
      nbSuspects=nbSuspects
   else:
      nbSuspects=nbSuspects+1

print(nbSuspects)
