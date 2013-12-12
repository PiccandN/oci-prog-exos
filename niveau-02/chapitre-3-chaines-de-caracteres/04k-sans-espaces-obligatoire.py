##################################
# fichier 04k-sans-espaces-obligatoire.py
# nom de l'exercice : Sans espaces
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=28
# type : obligatoire
#
# Chapitre : chapitre-3-chaines-de-caracteres
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

ligne = input()
caracteres = list(ligne)

for i in range(len(ligne)):
   if caracteres[i] == " ":
      caracteres[i] = "_"

ligne = "".join(caracteres)
print(ligne)
