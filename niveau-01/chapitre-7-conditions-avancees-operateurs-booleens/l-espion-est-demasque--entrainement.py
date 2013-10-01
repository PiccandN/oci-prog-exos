##################################
# fichier l-espion-est-demasque--entrainement.py
# nom de l'exercice :  L'espion est démasqué !
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=14
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

nbPersonnes=int(input())

for loop in range(nbPersonnes):
   nbCaracteristiques=0
   
   taille=int(input())
   if taille>=178 and taille<=182:
      nbCaracteristiques=nbCaracteristiques+1
   
   age=int(input())
   if age >=34:
      nbCaracteristiques=nbCaracteristiques+1
   
   poids=int(input())
   if poids<70:
      nbCaracteristiques=nbCaracteristiques+1
      
   cheval=int(input())
   if cheval==0:
      nbCaracteristiques=nbCaracteristiques+1
      
   cheveux=int(input())
   if cheveux==1:
      nbCaracteristiques=nbCaracteristiques+1
      
   if (nbCaracteristiques==5):
      print("Très probable")
   if (nbCaracteristiques==4) or (nbCaracteristiques==3):
      print("Probable")
   if (nbCaracteristiques==0):
      print("Impossible")
   if (nbCaracteristiques==2) or (nbCaracteristiques==1):
      print("Peu probable")
