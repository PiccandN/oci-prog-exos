##################################
# fichier 08-visite-de-la-mine-obligatoire.py
# nom de l'exercice : Visite de la mine
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=11
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

nbDeplacements = int(input())
aller = [0] * nbDeplacements
retour = [0] * nbDeplacements
valeurRetour = 0

for tDeplacement in range(nbDeplacements):
   tDeplacement = int(input())
   if tDeplacement == 1:
      retour[valeurRetour] = 2
   elif tDeplacement == 2:
      retour[valeurRetour] = 1 
   elif tDeplacement == 4:
      retour[valeurRetour] = 5
   elif tDeplacement == 5:
      retour[valeurRetour] = 4
   else:
      retour[valeurRetour] = 3
   valeurRetour += 1
   
valeurRetour -= 1
for loop in range(nbDeplacements):
   print(retour[valeurRetour])
   valeurRetour -= 1
