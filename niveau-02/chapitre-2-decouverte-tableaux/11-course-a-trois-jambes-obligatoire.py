##################################
# fichier 11-course-a-trois-jambes-obligatoire.py
# nom de l'exercice : Course à trois jambes
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=16
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

nbParticipants = int(input())
entier = [0] * nbParticipants
numParticipant = 0

for loop in range(nbParticipants):
   entier[numParticipant] = int(input())
   numParticipant += 1
entier.sort()

petit = 0
grand = nbParticipants -1

while petit < grand:
   print(entier[petit], entier[grand])
   petit += 1
   grand -= 1
