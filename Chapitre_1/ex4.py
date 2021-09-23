# Écrire un script qui convertit 1.827.499.540 secondes 
# en nombre d’années – mois – jours – heures - minutes - secondes

secondes = 1827499540
rest = secondes
sec_min = 60
sec_heure = 3600
sec_jour = 3600*24
sec_mois = sec_jour*30
sec_an = sec_jour*365

annees = rest // sec_an
rest = rest % sec_an

mois = rest // sec_mois
rest = rest % sec_mois

jours = rest // sec_jour
rest = rest % sec_jour

heures = rest // sec_heure
rest = rest % sec_heure

min = rest // sec_min
rest = rest % sec_min

print (f"Dans {secondes} secondes, il y à {annees} ans, {mois} mois, {jours} jours, {heures} heures, {min} minutes et {rest} secondes")
