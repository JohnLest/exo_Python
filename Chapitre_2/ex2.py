# Écrire un script avec la liste de nombres nb=[15, 89, 5, 99, 23, 78, 12, 33, 68, 16].
# Trouver et afficher le maximum de la liste, 
# calculer la moyenne global, 
# afficher les cotes supérieures à 30 et dire combien il y en a. 
# Ensuite, trier la liste par ordre croissant.

nb=[15, 89, 5, 99, 23, 78, 12, 33, 68, 16] # on initialise notre liste, 
plus_grand = 0 # une variable pour notre plus grand nombre, 
moyenne = 0 # une autre pour calculer la moyenne, 
plus30 = 0 # et une dernière pour verifier les nombres plus grands que 30.

for elem in nb: # Pour chaque élément dans la liste nb : 
    if (elem > plus_grand): # Si l'élément est plus grand que la valeur de plus_grand, 
        plus_grand = elem  # alors plus_grand prend la valeur de notre élément.
    moyenne += elem # On additionne notre élément à la valeur total de moyenne.
    if (elem > 30): # Si l'élément est plus grand que 30, 
        print(f"Cette cote : {elem} est plus grande que 30") # alors on l'affiche, 
        plus30 +=1 # et on ajoute un au compteur.

print(f"La cote maximum obtenue est : {plus_grand}") # on affiche la valeur de plus_grand.
print(f"La moyenne des cotes est de : {moyenne / len(nb)}") # On calcule la moyenne des cotes avec la somme total des éléments divisés par leur nombres.
print(f"Il y a un total de {plus30} cotes plus grandes que 30") # On précise combien de nombre sont plus grand que 30.
nb.sort() # On trie le tableau.
print(nb) # On affiche le tableau trié.
