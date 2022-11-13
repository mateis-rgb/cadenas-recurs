# -*- coding: utf-8 -*-

from class_cadenas import Cadena, ListeCarCombinaison;

combi = Cadena(int(input("Entrez le nombre de joueur : ")));
combi.generer_cadenas();

joueurs = ListeCarCombinaison(combi.nbj, combi.cadenas);

if (joueurs.estSeul()):
    while (joueurs.nbEssai > 0):
        essai = str(input("Entrez une combinaison à 4 caractères (A-Z & 0-9)"));
        
        verif = joueurs.verification(essai, 0);
        
        # Syntaxe d'un opérateur ternaire en Python
        # valeur_si_vrai if condition else valeur_si_faux
        print("Vous avez gagné, vous remportez tout le trésor." if verif else verif);  
    
elif (joueurs.nbJ == 2):
    while True:
        # Si aucun des joueurs n'a fini
        if (joueurs.aFini.get(0) == False and joueurs.aFini.get(1) == False):
            essai1 = str(input("Joueur 1, entrez une combinaison à 4 caractères (A-Z & 0-9)"));
            verif1 = joueurs.verification(essai1, 0);
            
            if (verif1):
                joueurs.aFini[0] = 1;
            else:
                print(verif1);
                
                
            essai2 = str(input("Joueur 2, entrez une combinaison à 4 caractères (A-Z & 0-9)"));
            verif2 = joueurs.verification(essai2, 0);
            
            if (verif2):
                joueurs.aFini[1] = 1;
            else:
                print(verif2);
        
        # Si le joueur 1 à fini mais pas le joueur 2
        elif (joueurs.aFini.get(0) != False and joueurs.aFini.get(1) == False):
            print("Joueur 1, vous remportez 75% du trésor, attendez que le joueur 2 finisse");
            
        
        
        # Si le joueur 2 à fini mais pas le joueur 1
        elif (joueurs.aFini.get(1) != False and joueurs.aFini.get(0) == False):
            print("Joueur 2, vous remportez 75% du trésor, attendez que le joueur 2 finisse");
            
            
            
        # Les deux joueurs ont fini.
        else:
            print("Joueur 1, joueur 2, vous avez fini. Bravo à vous.");
            break;
            

else:
    






























