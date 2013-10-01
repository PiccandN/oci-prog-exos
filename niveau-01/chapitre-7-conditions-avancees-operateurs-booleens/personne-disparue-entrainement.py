##################################
# fichier personne-disparue-entrainement.py
# nom de l'exercice :  Personne disparue
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=9
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

numeroPers=int(input())
tailleListe=int(input())
reponse=0

for loop in range(tailleListe):
   if numeroPers==int(input()):
      reponse=1
      
if reponse==1:
   print("Sorti de la ville")
else:
   print("Encore dans la ville")
