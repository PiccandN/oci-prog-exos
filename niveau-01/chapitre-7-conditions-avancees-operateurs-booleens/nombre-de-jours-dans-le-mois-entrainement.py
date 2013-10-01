##################################
# fichier nombre-de-jours-dans-le-mois-entrainement.py
# nom de l'exercice :  Nombre de jours dans le mois
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=4
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

numero = int(input())
if numero == 11:
   print(29)
else:
   if ( (4 <= numero) and (numero <= 6) ) or (numero == 10):
      print(31)
   else:
      print(30)
