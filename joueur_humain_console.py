"""
Contient la classe JoueurHumainConsole, qui hérite de Joueur. Permet l'interaction avec l'utilisateur.

Pour cette classe, vous êtes encouragé à créer vos propres méthodes afin de réutiliser du code.
"""

from afficheur import afficher, demander
from joueur import Joueur


class JoueurHumainConsole(Joueur):
    def __init__(self, couleur):
        """
        Constructeur de la classe JoueurHumainConsole
        Args:
            couleur: la couleur du joueur
        """
        super().__init__(couleur, "Humain")

    def strategie_selection_attaquant(self, cases_disponibles):
        """
        Cette méthode permet à l'utilisateur de choisir une case attaquante parmi
        les cases disponibles à l'aide de la console.

          - Si le joueur entre des coordonnées au format x,y correspondant à une
          case disponible, on retourne cette case.
          - Si le joueur entre des coordonnées au format x,y ne correspondant pas à une
          case disponible (ou si les coordonnées sont en dehors du plateau), on lui indique
          d'entrer une case disponible et on redemande une case.
          - Si le joueur entre le mauvais format (ou toute autre chaîne de caractères non vide),
          on lui indique que l'entrée est invalide et on redemande une case.
          - Si le joueur n'entre rien, on retourne None.
          - Facultatif: vous pouvez afficher les coordonnées des cases disponibles.

        Exemple: Entrez les coordonnées de la case que vous souhaitez
                 sélectionner pour attaque (ou rien pour terminer le tour): salut
                 Entrée invalide. Entrez les coordonnées de la case que vous souhaitez
                 sélectionner pour attaque (ou rien pour terminer le tour): 3,4
                 Cette case n'est pas disponible pour attaque. Entrez les coordonnées de la case que vous souhaitez
                 sélectionner (ou rien pour terminer le tour): 5,6

        Args:
            cases_disponibles (dict): Les cases disponibles pour l'attaque

        Returns:
            Case: La case sélectionnée pour attaque. None si on choisit de passer notre tour.

        """
        # VOTRE CODE ICI
        case_dispo_key = ""
        for key in cases_disponibles.__iter__():
            case_dispo_key = case_dispo_key + str(key)
        debut = True
        cordonnees = demander("Entrez les coordonnées de la case que vous souhaitez sélectionner pour attaque (ou rien "
                              "pour terminer le tour)")
        while (debut):
            if cordonnees=="":
                debut = False
                return None
            else:

                mes_cordonnees = cordonnees.split(",")
                if len(mes_cordonnees) == 1 or len(mes_cordonnees) > 2:
                    chaine_selection_attaque_liste = 'Entrée invalide. Entrez les coordonnées de la case en attaque parmis:' +\
                                               case_dispo_key
                    chaine_selection_attaque = "".join(chaine_selection_attaque_liste)
                    afficher(chaine_selection_attaque)
                    cordonnees = demander("Entrez les coordonnées de la case que vous souhaitez sélectionner (ou rien "
                                          "pour terminer le tour): \n")

                if len(mes_cordonnees) == 2 and mes_cordonnees[0].isdigit() == False and mes_cordonnees[1].isdigit() == False:
                    chaine_selection_attaque_liste = 'Entrée invalide. Entrez les coordonnées de la case en attaque parmis:' + \
                                                     case_dispo_key
                    chaine_selection_attaque = "".join(chaine_selection_attaque_liste)
                    afficher(chaine_selection_attaque)
                    cordonnees = demander("Entrez les coordonnées de la case que vous souhaitez sélectionner (ou rien "
                                          "pour terminer le tour): ")

                if len(mes_cordonnees) == 2 and mes_cordonnees[0].isdigit() == True and mes_cordonnees[1].isdigit() == \
                        True and mes_cordonnees != "":
                    coor1, coor2 = int(mes_cordonnees[0]), int(mes_cordonnees[1])

                    point = (coor1,coor2)
                    if point in cases_disponibles:
                        debut = False
                        return cases_disponibles[point]
                    else:
                        chaine_selection_attaque_liste = 'Case non disponible. Entrez les coordonnées de la case en attaque parmis:' + \
                                                             case_dispo_key
                        chaine_selection_attaque = "".join(chaine_selection_attaque_liste)
                        afficher(chaine_selection_attaque)
                        cordonnees = demander(
                                "Entrez les coordonnées de la case que vous souhaitez sélectionner (ou rien "
                                "pour terminer le tour): ")

    def strategie_selection_defenseur(self, cases_disponibles, case_attaquante):
        """
        Cette méthode permet à l'utilisateur de choisir une case défenseur parmi
        les cases disponibles à l'aide de la console.

          - Si le joueur entre des coordonnées au format x,y correspondant à une
          case disponible, on retourne cette case.
          - Si le joueur entre des coordonnées au format x,y ne correspondant pas à une
          case disponible (ou si les coordonnées sont en dehors du plateau), on lui indique
          d'entrer une case disponible et on redemande une case.
          - Si le joueur entre le mauvais format (ou toute autre chaîne de caractères non vide),
          on lui indique que l'entrée est invalide et on redemande une case.
          - Si le joueur n'entre rien, on retourne None.
          - Facultatif: vous pouvez afficher les coordonnées des cases disponibles.

        Exemple: Entrez les coordonnées de la case que vous souhaitez
                 sélectionner pour défense (ou rien pour terminer le tour): salut
                 Entrée invalide. Entrez les coordonnées de la case que vous souhaitez
                 sélectionner pour défense (ou rien pour terminer le tour): 5,6
                 Cette case n'est pas disponible pour défense. Entrez les coordonnées de la case
                 que vous souhaitez sélectionner pour défense (ou rien pour terminer le tour): 5,5

        Args:
            cases_disponibles (dict): Les cases disponibles pour la défense.
            case_attaquante (Case): La case en mode attaque.
                IMPORTANT: cet argument n'est pas forcément utile. On le passe car on doit le passer
                à JoueurOrdinateur pour sa méthode du même nom. Vous pouvez donc l'ignorer ici.

        Returns:
            Case: La case sélectionnée pour attaque. None si on choisit de passer notre tour.

        """
        # VOTRE CODE ICI
        debut = True
        case_dispo_key = ""
        for key in cases_disponibles.__iter__():
            case_dispo_key = case_dispo_key + str(key)
        cordonnees = demander("Entrez les coordonnées de la case que vous souhaitez"\
                 "sélectionner pour défense (ou rien pour terminer le tour):")
        while (debut):
            if cordonnees == "":
                debut = False
                return None
            else:

                mes_cordonnees = cordonnees.split(",")
                if len(mes_cordonnees) == 1 or len(mes_cordonnees) > 2:
                    chaine_selection_defense_liste = 'Entrée invalide. Entrez les coordonnées de la case en defense parmis:' + \
                                                     case_dispo_key
                    chaine_selection_defense = "".join(chaine_selection_defense_liste)
                    afficher(chaine_selection_defense)
                    cordonnees = demander(
                        "Entrez les coordonnées de la case que vous souhaitez sélectionner (ou rien "
                        "pour terminer le tour): ")

                if len(mes_cordonnees) == 2 and mes_cordonnees[0].isdigit() == False and mes_cordonnees[
                    1].isdigit() == False:
                    chaine_selection_defense_liste = 'Entrée invalide. Entrez les coordonnées de la case en defense parmis:' + \
                                                     case_dispo_key
                    chaine_selection_defense = "".join(chaine_selection_defense_liste)
                    afficher(chaine_selection_defense)
                    cordonnees = demander("Entrez les coordonnées de la case que vous souhaitez sélectionner (ou rien "
                        "pour terminer le tour): ")
                if len(mes_cordonnees) == 2 and mes_cordonnees[0].isdigit() == True and mes_cordonnees[
                    1].isdigit() == True and mes_cordonnees != "":
                    coor1, coor2 = int(mes_cordonnees[0]), int(mes_cordonnees[1])
                    point = (coor1, coor2)
                    if point in cases_disponibles:
                        debut = False
                        return cases_disponibles[point]
                    else:
                        chaine_selection_defense_liste = 'Case non disponible. Entrez les coordonnées de la case en defense parmis:' + \
                                                         case_dispo_key
                        chaine_selection_defense = "".join(chaine_selection_defense_liste)
                        afficher(chaine_selection_defense)
                        cordonnees = demander(
                            "Entrez les coordonnées de la case que vous souhaitez sélectionner (ou rien "
                            "pour terminer le tour): ")

