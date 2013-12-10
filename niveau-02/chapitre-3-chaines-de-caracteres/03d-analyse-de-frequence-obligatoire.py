##################################
# fichier 03d-analyse-de-frequence-obligatoire.py
# nom de l'exercice : Analyse de fréquence
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=16
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

nbLignes, nbMots = map(int, input().split())
ligne = [0] * nbLignes
mots = []

for idLigne in range(nbLignes):
   ligne[idLigne] = input()
   mots += ligne[idLigne].split() #création d'un tableau avec tous les mots dedans
   
taille = [0] * 101

for mot in mots:
   taille[len(mot)] += 1

for i in range(101):
   if taille[i] >= 1:
      print("{} : {}".format(i, taille[i]))
