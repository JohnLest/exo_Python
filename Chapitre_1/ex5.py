# Trouver sur internet la légende de Sissa, 
# écrire un scripte qui donne le nombre total de grains de riz 
# ainsi que sa masse total.

# La légende : En Inde, le roi Belkib (ou Bathait), qui s'ennuie à la cour, 
# demande qu'on lui invente un jeu pour le distraire. 
# Le sage Sissa invente alors un jeu d'échecs, ce qui ravit le roi. 
# Pour remercier Sissa, le roi lui demande de choisir sa récompense, 
# aussi fastueuse qu'elle puisse être. Sissa choisit de demander au roi de prendre le plateau du jeu et, 
# sur la première case, poser un grain de riz, ensuite deux sur la deuxième, 
# puis quatre sur la troisième, et ainsi de suite, en doublant à chaque fois le nombre de grains de riz que l’on met. 
# Le roi et la cour sont amusés par la modestie de cette demande. Mais lorsqu'on la met en œuvre, 
# on s'aperçoit qu'il n'y a pas assez de grains de riz dans tout le royaume pour la satisfaire (Source : Wikipédia)


case = 0 # on initialise la case (-1) sur la quelle on ce trouve (ce sera l'exposant)
riz = 2 # on initialise le nombre de riz de dépard (2 car sur la seconde case on a deux grains de riz (2^1 = 2))
riz_total = 0 # on initialise le mombre total de grains de riz

while (case < 64): # Temps que le nombre de case est strictement plus petit que 64
    print(f"Sur la case {case} on dispose {riz ** case} grains de riz") # On indique combien de grains de riz est posé sur cette case
    riz_total = riz_total + (riz ** case) # On ajoute le nombre de grains de riz de la case au total des grains de riz
    case += 1 # on incrémente la case de 1

print(f"Il y a donc un total de {riz_total} de grains de riz") # On affiche le total de grains de riz
riz_kilo = 25000 # On initialise le nombre de grains de riz dans un kilo

print(f"Si dans un Kg de riz il y a {riz_kilo} grains, alors le sage à demandé un total de {riz_total / riz_kilo / 1000} tonnes de riz")
# On calcule et affiche le nombre total de tonnes que le vieux sage demande.