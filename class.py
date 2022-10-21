from random import *

class Cadena():
   
   def __init__(self,nbj ):
      self.nbj = nbj;
            
   def generer_cadenas(self):
      self.cadenas=[];
      cars=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9"];
      
      for k in range (self.nbj-1):
         combi = list();
         for i in range(4):
            combi.append(random.choice(cars));
         self.cadenas[k] = combi;
      
   
   
   
class ListeCarCombinaison():
      
      def __init__(self, nbJ, cadenas):
         self.nbJ = nbJ;
         self.cadenas = cadenas
         
      def estSeul(self):
         return self.nbJ == 1;
      
      def nbEssai(self):
         self.nbEssai = 10;
         
      def verification(self, combi):
         for x ion range(combi):
            if 
      
         
