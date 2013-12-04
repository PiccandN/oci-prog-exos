##################################
# fichier 04f-ngms-sns-vlls-obligatoire.py
# nom de l'exercice : ngms sns vlls
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=23
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

for loop in range(2):
   titre = input()
   for i in range(len(titre)):
      if titre[i] != "A" and titre[i] != "E" and titre[i] != "I" and titre[i] != "O" and titre[i] != "U" and titre[i] != "Y" and titre[i] != " ":
         print(titre[i], end = "")
   print("")
