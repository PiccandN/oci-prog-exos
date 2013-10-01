##################################
# fichier force-algoreenne-validation.py
# nom de l'exercice :  Force algoréenne
# url : http://www.france-ioi.org/algo/task.php?idChapter=646&idTask=0&sTab=task&iOrder=1
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

nbPersonnes=int(input())
if nbPersonnes > 0:
   poids1=0
   poids2=0
   for loop in range(nbPersonnes):
      poids1=poids1+int(input())
      poids2=poids2+int(input())
      
if poids1-poids2 > 0:
         print("L'équipe 1 a un avantage")
if poids2-poids1 > 0:
         print("L'équipe 2 a un avantage")
print("Poids total pour l'équipe 1 : " + str(poids1))
print("Poids total pour l'équipe 2 : " + str(poids2))
