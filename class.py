import random;

class Cadena():
   
   def __init__(self, nbj):
      self.nbj = nbj;
            
   def generer_cadenas(self):
      self.cadenas={};
      cars=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9"];
      
      for k in range(self.nbj):
         combinaison = list();
         for i in range(4):
            combinaison.append(random.choice(cars));
         self.cadenas[k] = combinaison;
      
   
   
   
class ListeCarCombinaison():
      
    def __init__(self, nbJ, cadenas):
         self.nbJ = nbJ;
         self.cadenas = cadenas;
         
    def estSeul(self):
         return self.nbJ == 1;
      
    def nbEssai(self):
         self.nbEssai == 10;
         
    def verification(self, combi, code):
         cpt=0 # mal positionné
         cpi=0 # bien positionné
         
         for i in range(self.cadenas -1):
            for x in range(len(combi)):
               if x == i:
                  cpt += 1;
            for k in range(len(combi)):
               if combi[k] == code[k]:
                  cpi += 1;
         return f"{cpt} mal poitioné et {cpi} bien positionné";
                           
    def transformerCombinaison(self, combiUser, code):
          """ TransfromerCombinaison() est une fonction qui permet de passer
          d'une chaine de caractère (combiUser) à une tableau contenant chaque
          caractère.
          """
          combiUser = combiUser.upper();
          
          for caractere in combiUser:
              code.append(caractere);
              
          return code;
                        
                         
      
         
