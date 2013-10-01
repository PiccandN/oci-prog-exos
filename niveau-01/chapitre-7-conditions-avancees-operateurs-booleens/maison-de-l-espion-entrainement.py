##################################
# fichier maison-de-l-espion-entrainement.py
# nom de l'exercice :  Maison de l'espion
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=2
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

abcissemin=int(input())
abcissemax=int(input())
ordonneemin=int(input())
ordonneemax=int(input())
nbMaisonstot=int(input())
nbMaisons=0


for loop in range(nbMaisonstot):
   abcisseMaison=int(input())
   ordonneeMaison=int(input())
   
   if abcisseMaison >=abcissemin and abcisseMaison <= abcissemax and ordonneeMaison >=ordonneemin and ordonneeMaison <= ordonneemax:
      nbMaisons=nbMaisons+1
      
print(nbMaisons)
