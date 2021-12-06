# Alexandre Doneux
# Python 3.10

from exercices.matrix import Matrix # techniquement je n'utilise pas la classe Matrix. J'utilise des objets mais pas besoin d'import
import numpy as np


class ExerciceMultDiv:
    def __init__(self, matrix, factor, type_ex):
        """
        initialisation des attributs de la classe et calculera la somme et la différence des deux matrices
        :param matrix1: Première matrice pour l'addition ou soustraction
        :param matrix2: Deuxième matrice pour l'addition ou soustraction
        :param: type: int, si égal à 0, on fait une addition, si égale à 1 une soustraction
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
                             "\n\nDonnez", self.ex_name[self.type_ex], "\n "))
        return(self.text)

    def check_result(self, awnser):
        """
        Vérifiera la réponse de l'utilisateur et le résultat généré par le code pour le calcul
        :param awnser: solution fournie par l'utilisateur, on utilisera un input dans main_matrix.py
        :return: result - boolean, si  la réponse est bonne renvoie True, sinon renvoie False
        """
        result = np.array_equal(self.result, awnser)
        return(result)


if __name__ == "__main__":
    print("Fin")