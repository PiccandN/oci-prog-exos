##################################
# fichier 04-fonction-min-obligatoire.py
# nom de l'exercice : Fonction min
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=7
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

def min(a, b):
   if a < b:
      return a
   else:
      return b
   
def main():
   a = int(input())
   for loop in range(9):
      b = int(input())
      a = min(a, b)
   print(a)
      
main()
