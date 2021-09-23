# Écrire un script qui convertit 1.827.499.540 secondes 
# en nombre d’années – mois – jours – heures - minutes - secondes

secondes = 1827499540 # On stock le nombre total de secondes
rest = secondes # On initialise le reste de seconde à calculer
sec_min = 60 # on calcule combien de secondes on a dans une minute
sec_heure = 3600 # dans une heure
sec_jour = 3600*24 # dans une journée 
sec_mois = sec_jour*30 # dans un mois (on prend des mois de 30 jours pour avoir plus facile)
sec_an = sec_jour*365 # dans un an (on ne compte pas les années bissextiles)

annees = rest // sec_an # On fait une division entière pour savoir le nombre d'années complètes qu'il y a
rest = rest % sec_an # On prend le reste de la division pour savoir le nombre de seconde qu'il nous reste.

mois = rest // sec_mois # On fait une division entière pour savoir le nombre de mois complets qu'il y a
rest = rest % sec_mois  # On prend le reste de la division pour savoir le nombre de seconde qu'il nous reste.

jours = rest // sec_jour # On fait une division entière pour savoir le nombre de jours complets qu'il y a
rest = rest % sec_jour # On prend le reste de la division pour savoir le nombre de seconde qu'il nous reste.

heures = rest // sec_heure # On fait une division entière pour savoir le nombre d'heures complètes qu'il y a
rest = rest % sec_heure # On prend le reste de la division pour savoir le nombre de seconde qu'il nous reste.

min = rest // sec_min # On fait une division entière pour savoir le nombre de minutes complètes qu'il y a
rest = rest % sec_min # On prend le reste de la division pour savoir le nombre de seconde qu'il nous reste.

print (f"Dans {secondes} secondes, il y à {annees} ans, {mois} mois, {jours} jours, {heures} heures, {min} minutes et {rest} secondes")
# On imprime le résultat
