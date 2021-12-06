# Alexandre Doneux
# Python 3.10

from exercices.matrix import Matrix  # techniquement je n'utilise pas la classe Matrix. J'utilise des objets mais pas besoin d'import
import numpy as np
from ast import literal_eval

class Inverse:
    def __init__(self, matrix):
        """
        initialisation des attributs de la classe et calculera l'inverse de la matrice
        :param matrix: matrice dont on calculera la matrice inverse
        """
        self.matrix = matrix
        matrix.inverse() # Calcule l'inverse de la matrice

        matrix.get_determinant()
        if matrix.determinant == 0:
            self.result == literal_eval("[[0]]") # J'aurais pu juste mettre [[0]]
            #self.result == [[0]]
        else:
            self.result = self.matrix.inverted
        self.text = ""

    def __str__(self):
        self.text = "".join(("Soit la matrice suivante: \n\n", str(self.matrix),
                             "\n\nDonnez la matrice inverse de cette matrice\. Si elle n'en a pas, écrivez '[[0]]'.\n"
                             "Attention! arrondir les valeurs au millième près. Arrondi vers le haut à 5.\n: "))
        # Une matrice inverse ne peut jamais être nulle
        return(self.text)

    def check_result(self, awnser):
        """
        Vérifiera la réponse de l'utilisateur et le résultat généré par le code pour le calcul
        :param awnser: solution fournie par l'utilisateur, on utilisera un input dans main_matrix.py
        :return: result - boolean, si  la réponse est bonne renvoie True, sinon renvoie False
        """
        #result = np.array_equal(self.result, awnser)
        result = np.allclose(self.result, awnser, 0.01, 0.01)   # vérifie si égale avec une certaine précision (les valeurs de tolérance de base sont OK
        # Dans certains calculs de numpy on a pas le nombre exacte, exemple: 3 != 3.0000000000004
        return(result)


if __name__ == "__main__":

    matrix = Matrix(2, 2)
    matrix.values = [[-1, 3], [-2, 0]]
    matrix.inverse()
    print(matrix)
    print(matrix.inverted)
    print(np.allclose(literal_eval("[[0, -0.5], [0.33, -0.17]]"), matrix.inverted))