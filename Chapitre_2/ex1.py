# Écrire un script qui permet à l'utilisateur d'introduire des nombres 
# et qui les additionne au fur et à mesure. Le script s'arrête lorsque 
# l'utilisateur introduit un nombre négatif (sans le calculer). A ce moment l'ordinateur affiche la somme.

calcul = 0 # On initialise une variable qui calculera les nombres
while (True): # On crèe une boucle infinie (la condition est toujour Vraie)
    nbr = int(input("Entrez un nombre ")) # On demande à l'utilisateur d'entrer un nombre qu'on convertit directement en int
    if (nbr >= 0): # Si le nombre est plus grand ou égal que 0,
        calcul += nbr # on ajoute à calcul la valeur de nbr.

    else : # Sinon, c'est que le nombre est négatif, 
        print(f"La somme total des nombres enregistrés est : {calcul}") # on affiche donc le résultat 
        break # et on casse la boucle pour en sortir. 

