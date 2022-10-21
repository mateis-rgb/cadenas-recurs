# cadenas-recurs
Projet de NSI
## Arboressance :
Fichier qui contient les deux classes.
-> class.py

Fichier qui contient le code principale de la résolution du problème.
-> main.py

Fichier source du pdf (fichier latex)
-> projet.tex

## Consigne
Un coffre-fort rempli de pièces d’or est fermé par autant de cadenas qu’il y a de joueurs.
S’il n’y a qu’un seul joueur, celui-ci devra réussir à l’ouvrir avec un nombre d’essais
limité (ou dans un laps de temps limité) sans quoi le coffre explose et le trésor est perdu
! S’il y a plusieurs joueurs le butin sera distribué en parts inégales, de la plus grosse
pour celui qui ouvre le cadenas en premier à la plus petite pour le dernier à ouvrir le
cadenas (ex : pour 4 joueurs : 50%, 30%, 15% et 5%).

Pour ouvrir un cadenas il faut en trouver la combinaison. Celle-ci est constituée de 5
caractères (chiffres et/ou lettres). La combinaison est déterminée de manière aléatoire :
chaque caractère de la combinaison est choisi dans une liste de six valeurs possibles qui
est portée à la connaissance du ou des joueurs. Chaque cadenas possède sa propre
combinaison.

A tour de rôle chaque joueur propose une combinaison : quand celle-ci est incorrecte, il
reçoit en retour une indication : nombre de caractères corrects et bien positionnés (mais
sans indication de position !), et nombre de caractères corrects mais mal positionnés. Par
exemple si les code est “A F D G *” et que le joueur propose “A C A * A” il lui est donné
l’indication suivante : “1 bien positionné et 1 mal positionné”.


Écrire un programme en Python qui permet de jouer “au trésor à partager” et qui s’appuie sur
deux classes dont vous définirez les attributs et les méthodes : la classe “Cadenas” et la
classe “ListeCarCombinaison” (chacune des instances de cette classe définit une liste de 6
caractères à partir de laquelle est constituée la combinaison d’un cadenas).

Se rappeler qu’un attribut d’une classe peut prendre comme valeur une instance d’une autre
classe. Pour éviter la ‘triche’ les deux classes seront sauvegardées dans un module qui sera
importé dans le programme principal du jeu.

class ListeCarCOmbinaison(): <br>
  methode __init__(self nbJ, cadenas): <br>
    self.cadenas= cadenas <br>
    self.nbJ= nbj <br>

  methode estSeule(self): <br>
    retourner self.nbj = 1 <br>

  methode nbEssai(self): <br>
    si self.cadenas[J]= cobinaison faire <br>
      pop(J) <br>
      ajouter dans une liste J qui ont finit <br>
