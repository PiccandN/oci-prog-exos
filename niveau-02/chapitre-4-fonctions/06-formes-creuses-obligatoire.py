##################################
# fichier 06-formes-creuses-obligatoire.py
# nom de l'exercice : Formes creuses
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=13
# type : obligatoire
#
# Chapitre : chapitre-4-fonctions
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nbX = int(input())
nbLignesRectangle = int(input())
nbColonnesRectangle = int(input())
nbLignesTriangle = int(input())


def ligneX(nbX):
   for loop in range(nbX):
      print("X", end = "")
   print("")
   

def rectangle(nbLignesRectangle, nbColonnesRectangle):
   if nbLignesRectangle == 1:
      for loop in range(nbColonnesRectangle):
         print("#", end = "")
      print("")
      
   elif nbColonnesRectangle == 1:
      for loop in range(nbLignesRectangle):
         print("#")
   
   else:
      for loop in range(nbColonnesRectangle):
        print("#", end = "")
      print("")   
   
      for loop in range(nbLignesRectangle - 2):
         print("#", end = "")
         for loop in range(nbColonnesRectangle - 2):
            print(" ", end = "")
         print("#")
   
      for loop in range(nbColonnesRectangle):
         print("#", end = "")
      print("")
   

def triangle(nbLignesTriangle):
   if nbLignesTriangle == 1:
      print("@")
   
   else:
      print("@")
   
      for i in range(nbLignesTriangle - 2):
         print("@", end = "")
         for loop in range(i):
            print(" ", end = "")
         print("@", end = "")
         print("")
   
      for loop in range(nbLignesTriangle):
         print("@", end = "")
   
   
ligneX(nbX)
print("")
rectangle(nbLignesRectangle, nbColonnesRectangle)
print("")
triangle(nbLignesTriangle)
