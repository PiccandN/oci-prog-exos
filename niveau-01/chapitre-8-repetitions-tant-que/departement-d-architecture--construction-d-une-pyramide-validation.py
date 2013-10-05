##################################
# fichier departement-d-architecture--construction-d-une-pyramide-validation.py
# nom de l'exercice :  Département d'architecture : construction d'une pyramide
# url : http://www.france-ioi.org/algo/task.php?idChapter=649&idTask=0&sTab=task&iOrder=6
# type : validation
#
# Nom du chapitre : 
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nbDispo=15
nbUtilises=0
hauteur=0

while nbDispo-nbUtilises >= (hauteur+1)**2:
    hauteur=hauteur+1
    nbUtilises=nbUtilises+hauteur**2

print(hauteur)
print(nbUtilises)
