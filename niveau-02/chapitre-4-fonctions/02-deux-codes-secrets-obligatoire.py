##################################
# fichier 02-deux-codes-secrets-obligatoire.py
# nom de l'exercice : Deux codes secrets
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=3
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

def test1():
   code = 4242
   trouve = False
   while trouve == False:
      print("Entrez le code :")
      if int(input()) == code:
         trouve = True
         
def test2():
   code = 2121
   trouve = False
   while trouve == False:
      print("Entrez le code :")
      if int(input()) == code:
         trouve = True
      
test1()
print("Premier code bon.")
test2()
print("Bravo.")
