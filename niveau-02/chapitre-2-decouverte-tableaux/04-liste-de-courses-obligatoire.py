##################################
# fichier 04-liste-de-courses-obligatoire.py
# nom de l'exercice : Liste de courses
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=5
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

prix_kg = [9, 5, 12, 15, 7, 42, 13, 10, 1, 20]
total = 0

for nIngredient in range(10):
   poids = int(input())
   total += poids * prix_kg[nIngredient]
   nIngredient += 1

print(total)
