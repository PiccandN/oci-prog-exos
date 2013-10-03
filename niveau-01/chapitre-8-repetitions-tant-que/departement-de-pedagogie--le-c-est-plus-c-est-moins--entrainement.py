##################################
# fichier departement-de-pedagogie--le-c-est-plus-c-est-moins--entrainement.py
# nom de l'exercice :  Département de pédagogie : le c'est plus, c'est moins !
# url : http://www.france-ioi.org/algo/task.php?idChapter=649&idTask=0&sTab=task&iOrder=5
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

nbCible=int(input())
nbEssais=0
trouve=False

while not trouve:
   
   nbEssais=nbEssais+1
  
   nbEnfant=int(input())
   
   if nbCible==nbEnfant:
      trouve=True
   if nbCible>nbEnfant:
      print("c'est plus")
   if nbCible<nbEnfant:
      print("c'est moins")
      
print("Nombre d'essais nécessaires : ")
print(nbEssais)
