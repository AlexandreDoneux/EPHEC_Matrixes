# Alexandre Doneux
# Python 3.10

from exercices.matrix import Matrix # techniquement je n'utilise pas la classe Matrix. J'utilise des objets mais pas besoin d'import
import numpy as np


class ExerciceMultDiv:
    def __init__(self, matrix, factor, type_ex):
        """
        initialisation des attributs de la classe et calculera la multiplication ou la division d'une matrice par un facteur
        :param matrix: matrice dont les termes seront multipliés/divisés
        :param factor: facteur de multiplication/division
        :param: type_ex: int, si égal à 0, on fait une multiplication, si égale à 1 une division
        """
        self.matrix = matrix
        self.factor = factor
        self.type_ex = type_ex

        self.ex_name = [" la multiplication A . b", " la division A / b"]
        if type_ex == 0:
            self.result = self.matrix.values * self.factor
        elif type_ex == 1:
            self.result = self.matrix.values / self.factor

        self.text = ""

    def __str__(self):
        self.text = "".join(("Soit la matrices A et le nombre b: \n\n", str(self.matrix), "\n\n", str(self.factor),
                             "\n\nDonnez", self.ex_name[self.type_ex], "\n"
                             "Attention! arrondir les valeurs au millième près. Arrondi vers le haut à 5.\n: "))
        return(self.text)

    def check_result(self, awnser):
        """
        Vérifiera la réponse de l'utilisateur et le résultat généré par le code pour le calcul
        :param awnser: solution fournie par l'utilisateur, on utilisera un input dans main_matrix.py
        :return: result - boolean, si  la réponse est bonne renvoie True, sinon renvoie False
        """
        # result = np.array_equal(self.result, awnser)
        result = np.allclose(self.result,
                             awnser)  # vérifie si égale avec une certaine précision (les valeurs de tolérance de base sont OK
        # Dans certains calculs de numpy on a pas le nombre exacte, exemple: 3 != 3.0000000000004
        return(result)


if __name__ == "__main__":
    print("Fin")