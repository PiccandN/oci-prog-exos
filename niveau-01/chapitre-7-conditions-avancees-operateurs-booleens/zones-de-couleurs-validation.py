##################################
# fichier zones-de-couleurs-validation.py
# nom de l'exercice :  Zones de couleurs
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=15
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

nbPers=int(input())

for loop in range(nbPers):
   x=int(input())
   y=int(input())
   
   if ((x>10 and x<50) and (y>10 and y<20)) or ((x>10 and x<50) and (y>45 and y<55)) or ((x>10 and x<25) and (y>20 and y<45)) or ((x>50 and x<85) and (y>10 and y<55)):
      print("Dans une zone bleue")
   
   elif ((x>15 and x<45) and (y>60 and y<70)) or ((x>60 and x<85) and (y>60 and y<70)):
      print("Dans une zone rouge")
      
   elif ((x>0 and x<90) and (y>0 and y<70)):
      print("Dans une zone jaune")
   
   else:
      print("En dehors de la feuille")
