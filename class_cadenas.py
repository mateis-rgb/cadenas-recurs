# -*- coding: utf-8 -*-

from random import choice;

class Cadena():
    """ Cette classe permet de creer une liste de combinainsons en fonction
        du nombre de joueurs au jeu.
        
        Cette classe prend un nombre de joueurs en paramètre.
    """
    
    def __init__(self, nbj):
        self.nbj = nbj;
            
    def generer_cadenas(self):
        """ Cette méthode génère un liste de combinaisons en fonctrion du
            nombre de joueurs
        """
    
        self.cadenas = dict();
        cars=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
              "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
              "1", "2", "3", "4", "5", "6", "7", "8", "9"];
        
        # On creer un couple clé valeurs pour chaque joueurs, cela va donner,
        # => id_du_joueur: combinaison
        for k in range(self.nbj):
            combinaison = list();
           
            for i in range(4):
                # On tire aléatoirement dans les caractères disponibles.
                combinaison.append(choice(cars));
           
            self.cadenas[k] = combinaison;
      
   
   
   
class ListeCarCombinaison():
    """ Cette classe permet de faire toutes les vérifications ainsi que 
        le déroulement du jeu.
        
        Cette classe prend en paramètre un nombre de joueurs ainsi qu'un
        dictionnaire Python contenant les combinaisons.
    """
      
    def __init__(self, nbJ, cadenas):
         self.nbJ = nbJ;
         self.cadenas = cadenas;
         
         if (nbJ != 1): self.aFini = {i: False for i in range(nbJ)}
         
    def estSeul(self):
        """ Cette méthode controlle si le joueur est seul au quel cas il
            retourne True sinon False.
        """
        return self.nbJ == 1;
      
    def defNbEssai(self):
        """ Cette méthode défini un attribut de classe ListeCarCombinaison, 
            cet attribut est le nombre d'essaie que possède le joueur pour
            trouvé la combinaison. L'attribut nbEssai n'est définit que s'il
            y à qu'un seul joueur.
        """
        if (self.estSeul()):
            self.nbEssai = 10;
         
    def verification(self, combinaison, joueur):
        """ Cette méthode procède à la comparaison de la chaine de caractère
            entré par le joueur ainsi que celle qu'il doit trouver.
        """
        
        cpt=0 # mal positionné
        cpi=0 # bien positionné
         
        code = self.cadenas.get(joueur);
        combi = self.transformerCombinaison(combinaison);
         
        for i in range(self.cadenas -1):
            for x in range(len(combi)):
                if (x == i):
                    cpt += 1;
                
                if (combi[x] == code[x]):
                    cpi += 1;
            
        
        if (code != combi):
            return (f"{cpt} mal poitioné et {cpi} bien positionné");
        
        return True;
            
    def transformerCombinaison(self, combiUser):
          """ Cette méthode permet de passer d'une chaine de caractère
              (combiUser) à une tableau contenant chaque caractère.
          """          
          code = list();
          
          for caractere in combiUser:
              code.append(caractere.upper());
              
          return code;

    def recompense(self):
        return 0;
                        
                         
      
         
