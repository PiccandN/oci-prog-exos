##################################
# fichier bonus--casernes-de-pompiers-validation.py
# nom de l'exercice :  Bonus : Casernes de pompiers
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=7
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

nbPaires=int(input())

for loop in range(nbPaires):
   abcissemin1=int(input())
   abcissemax1=int(input())
   ordonneemin1=int(input())
   ordonneemax1=int(input())
   
   abcissemin2=int(input())
   abcissemax2=int(input())
   ordonneemin2=int(input())
   ordonneemax2=int(input())
   
   if (abcissemax1<=abcissemin2 or abcissemax2<=abcissemin1)or(ordonneemax1<=ordonneemin2 or ordonneemax2<=ordonneemin1):
      print("NON")
   else:
      print("OUI")
