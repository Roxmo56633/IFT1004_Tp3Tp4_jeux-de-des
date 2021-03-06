"""
Contient la classe JoueurOrdinateur, qui hérite de Joueur. Cette classe implémente une intelligence
artificielle pour choisir l'attaquant et le défenseur.

La stratégie de l'intelligence artificielle est la suivante:
À chaque attaque elle a une chance sur 5 d'arrêter son tour
Si elle attaque:
    Elle sélectionne l'attaquant ayant le plus de dés
    Si des voisins ont 1 ou 2 dés de moins, elle attaque le plus fort d'entre eux
    Sinon, si un voisin a autant de dés qu'elle, elle l'attaque
    Sinon, si un voisin a au moins 3 dés de moins qu'elle, elle attaque le plus fort d'entre eux
    Sinon, elle a une chance sur deux d'attaquer le voisin le plus faible parmi ceux qui sont
        plus forts qu'elle, sinon elle retourne à la phase de choix de l'attaquant
Dans tous les cas, les égalités sont brisées arbitrairement.
"""

from joueur import Joueur
from random import randint
from case import Case

from random import choice


class JoueurOrdinateur(Joueur):
    def __init__(self, couleur):
        """
        Constructeur de la classe JoueurOrdinateur
        Args:
            couleur: la couleur du joueur
        """
        super().__init__(couleur, "Ordinateur")


    def filtrer_nb_des(self, cases, valeurs_acceptees):
        """
        Cette méthode retourne les cases dont le nombre de dés (Case.nombre_de_des)
        fait partie des valeurs de nombres de dés acceptés.

        Args:
            cases (dict): Les cases du jeu
            valeurs_acceptees (list): La liste des nombres de dés à conserver

        Returns:
            dict: Les cases du jeu dont le nombre de dés fait partie des valeurs acceptées

        """
        # VOTRE CODE ICI
        dico={}
        for cordonnees,case in cases.items():
            if case.nombre_de_des() in valeurs_acceptees:
                dico[cordonnees] = case
        return dico

    def trouver_nb_des_optimal(self, cases, minimum=False):
        """
        Cette méthode trouve la case ayant le maximum OU le minimum de dés.
        Si l'option minimum n'est pas cochée, on trouve la case ayant le plus grand nombre de dés.
        Si l'option minimum est cochée, on trouve la case ayant le plus petit nombre de dés.
        Vous pouvez utiliser des sous-méthodes si cela vous facilite le travail.

        Dans le cas d'une égalité (e.g. plusieurs cases ont le maximum de dés), vous pouvez
        sélectionner n'importe laquelle de ces cases (au hasard, toujours la dernière visitée par
        votre algorithme, ...).

        Args:
            cases (dict): Les cases parmi lesquelles chercher
            minimum (bool, optionnel): Si True, trouver le minimum, si False, trouver le maximum.
                Défaut: False

        Returns:
            Case: la case sélectionnée
        """
        # VOTRE CODE ICI
        def casse_maximum(cases):
            """
           Ajout trouve la case ayant le plus grand nombre de dés
            Args:
                cases: (dict) Les cases parmis lesquelles chercher

            Returns: la case maximum (dans le cas ou il y en a deux, c'est la 1re maximum)

            """
            case_maximale = None
            nombre_plus_grand = 0
            liste_case_objet = list(cases.values())
            for i in range(len(liste_case_objet)):
                nombre_des_case = Case.nombre_de_des(liste_case_objet[i])
                if nombre_des_case > nombre_plus_grand:
                    nombre_plus_grand = nombre_des_case
                    case_maximale = liste_case_objet[i]

                i = i + 1
            return case_maximale

        def casse_minimum(cases):
            """
            Trouve la case ayant le moins de dés
            Args:
                cases: (dict) Les cases parmis chercher

            Returns: la case ayant le moins de dés (si il y en a deux, on trouve le 1re minimum)

            """
            case_minimum = None
            nombre_plus_petit = 8
            liste_case_objet = list(cases.values())
            for i in range(len(liste_case_objet)):
                nombre_des_case = Case.nombre_de_des(liste_case_objet[i])
                if nombre_des_case < nombre_plus_petit:
                    nombre_plus_petit = nombre_des_case
                    case_minimum = liste_case_objet[i]

                i = i + 1
            return case_minimum

        if minimum == False:
            return casse_maximum(cases)
        else:
            return casse_minimum(cases)



    def strategie_selection_attaquant(self, cases_disponibles):
        """
        Cette méthode implémente l'intelligence artificielle (IA) permettant de sélectionner
        un attaquant.

        Args:
            cases_disponibles (dict): Les cases disponibles pour attaque

        Returns:
            Case: La case sélectionnée par l'IA. None si elle arrête son tour.
        """
        # L'IA a une chance sur 5 d'arrêter son tour
        if randint(1, 5) == 1:
            return None

        # L'IA sélectionne l'attaquant ayant le plus de dés
        return self.trouver_nb_des_optimal(cases_disponibles)

    def strategie_selection_defenseur(self, cases_disponibles, case_attaquante):
        """
        Cette méthode implémente l'intelligence artificielle (IA) permettant de sélectionner
        un défenseur.

        Args:
            cases_disponibles (dict): Les cases disponibles pour attaque
            case_attaquante (Case): La case qui attaque

        Returns:
            Case: La case sélectionnée par l'IA. None si elle retourne à la phase de
            sélection de l'attaquant.
        """

        # Si des voisins ont 1 ou 2 dés de moins, l'IA attaque le plus fort d'entre eux
        case_defense = self.trouver_nb_des_optimal(
            self.filtrer_nb_des(cases_disponibles,
                                [case_attaquante.nombre_de_des() - 1, case_attaquante.nombre_de_des() - 2])
        )
        if case_defense is not None:
            return case_defense

        # Sinon, si un voisin a autant de dés que l'IA, elle l'attaque
        case_defense = self.trouver_nb_des_optimal(
            self.filtrer_nb_des(cases_disponibles, [case_attaquante.nombre_de_des()])
        )
        if case_defense is not None:
            return case_defense

        # Sinon, si un voisin a au moins 3 dés de moins que l'IA, elle attaque le plus fort d'entre eux
        case_defense = self.trouver_nb_des_optimal(
            self.filtrer_nb_des(cases_disponibles,
                                [case_attaquante.nombre_de_des() - i for i in
                                 range(3, case_attaquante.nombre_de_des())])
        )
        if case_defense is not None:
            return case_defense

        # Sinon, l'IA attaque le voisin le plus faible parmi ceux qui sont plus forts qu'elle
        if randint(1, 2) == 1:
            return self.trouver_nb_des_optimal(cases_disponibles, minimum=True)
        else:
            return None
