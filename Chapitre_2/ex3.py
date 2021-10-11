# Écrire un script qui permet à l'utilisateur d'introduire le nombre d'ordinateurs qu'il
#    désire dans son réseau ainsi que le numéro d'ordre du premier ordinateur. 
#    Le programme constitue alors deux listes. 
#    Celle des noms des ordinateurs et celle des adresses Ip. 
#    Exemple avec 5 ordinateurs et que le numéro d'ordre du premier est égal à 14 : 
#        liste_ordi=['ordi14','ordi15','ordi16',...,'ordi18'] 
#        liste_ip=['192.168.0.14', '192.168.0.15', '192.168.0.16',...,'192.168.0.18'] 
#    /!\ l'adresse 192.168.0.0 ainsi 192.168.0.255 ne peuvent être utilisée, 
#    et bien entendu on ne peut aller au delà de 192.168.0.254 adresse ip maximale dans un réseau de classe C.

nbrOrdi = int(input("Combien d'ordinateur y a t'il a initialiser? ")) # On demande combien de machine on veut sur notre réseau
demarrage = int(input("À partir de quel numéro faut-il démarrer? ")) # et quel numéro porte la première machine.

if(demarrage + nbrOrdi >= 255): # Si le nombre de machine plus le numéro de démmarage dépasse les 255 c'est qu'on va trop loins.
    print("Il y a une erreur car on dépasse le range autorisé (254)")
elif(demarrage <= 0) : # Et bien sur  on vérifie qu'on part bien de 1 ou plus 
    print("La valeur de de démarrage doit être min 1")
else : # si tout est bon, 
    liste_ordi = [] # on initialise la liste des ordinateurs
    liste_ip = [] # et des addresses IP.

    for ordi in range(nbrOrdi): # Pour chaque ordinateur, 
        liste_ordi.append(f"ordi{demarrage + ordi}") # on ajoute le nom de l'ordinateur, 
        liste_ip.append(f"192.168.0.{demarrage + ordi}") # et l'addresse IP. 

    print(liste_ordi) # On affiche ensuite 
    print(liste_ip) # les deux listes
