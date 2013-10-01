##################################
# fichier departement-de-medecine--controle-d-une-epidemie-entrainement.py
# nom de l'exercice :  Département de médecine : contrôle d'une épidémie
# url : http://www.france-ioi.org/algo/task.php?idChapter=649&idTask=0&sTab=task&iOrder=1
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

popVille=int(input())
nbMalades=1
nbJours=1

while nbMalades < popVille:
   nbMalades=nbMalades*3
   nbJours=nbJours+1
   
print(nbJours)
