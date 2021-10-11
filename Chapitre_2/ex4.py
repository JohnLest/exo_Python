# Écrire un script qui permet à l'utilisateur de créer une liste avec autant de prénom qu'il le souhaite, 
#     pour ensuite afficher les élément avec leur index.
#     Une fois cette liste créé, permettre à l'utilisateur de, au choix : 
#         Supprimer un élément à partir de l'index ou du prénom, 
#         ajouter un autre prénom, 
#         trier la liste par ordre alphabétique.
#     Afficher ensuite la liste modifiée soit totalement soit une partie en spécifiant la range d'index.

nbr = int(input("Combien d'éléments contient la liste? ")) # On demande combien d'éléments enregistre notre utilisateur.
liste = [] # on crée une liste vide
for i in range(nbr): # Dans une boucle for,  
    nom = input(f"Prénom {i +1}: ") # on demande le prénom à enregistrer
    liste.append(nom) # qu'on ajoute dans notre liste

for index in range(len(liste)): # une boucle for pour aller chercher les index et afficher les prénoms.
    print(f"l'index {index} contient {liste[index]} ")

choix = int(input("Que voulez vous faire? \n\t 1 - Supprimer un élément de la liste \n\t 2 - Supprimer un index de la liste \n\t 3 - Ajouter un nom \n\t 4 - Trier la liste par ordre alphabétique\n"))
# On laisse 4 choix à l'utilisateur : 
if(choix == 1): # Supprimer un élément par sa valeur, 
    delete = input("Quel élément faut il supprimer? ")
    liste.remove(delete)
elif(choix == 2): # supprimer un élément par son index
    delete = int(input("Quel index faut il supprimer? "))
    del(liste[delete])
elif(choix == 3): # Ajouter un prénom à la liste
    ajout = input("Prenom : ")
    liste.append(ajout)
elif(choix == 4): # ou trier la liste 
    liste.sort()
else : # bien sur on pense à ajouter une condition au cas ou l'utilisateur ne choisi aucun des 4 choix.
    print("Erreur dans les choix")

range_ = input("Quel range d'index faut il afficher (Merci de séparer les index par une virgule ou laisser vide pour la liste entière). ")
# On demande si l'utilisateur veut afficher toute la liste ou une partie. Si c'est une partie on lui demande de séparer les index par  une virgule
if(range_ != ""): # Si la réponse n'est pas vide :  
    rangeLst = range_.split(',') # on divise la chaine dans un tableau avec la virgule comme séparateur
    for index in rangeLst:
        index = index.strip() # on enlève les éventuelles espaces
    print(liste[int(rangeLst[0]): int(rangeLst[1])]) # on affiche le tableau avec la range d'index obtenu.
else : 
    print(liste) # Sinon on affiche tout le tableau.


