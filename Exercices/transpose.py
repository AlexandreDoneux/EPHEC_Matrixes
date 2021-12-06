# Alexandre Doneux
# Python 3.10

from exercices.matrix import Matrix  # techniquement je n'utilise pas la classe Matrix. J'utilise des objets mais pas besoin d'import
import numpy as np

class Transpos:
    def __init__(self, matrix):
        """
        initialisation des attributs de la classe et calculera la transposée de la matrice
        :param matrix: matrice dont on calculera le déterminant
        """
        self.matrix = matrix
        matrix.transpose()  # Calcule la transposée de la matrice
        self.result = self.matrix.transposed
        self.text = ""

    def __str__(self):
        self.text = "".join(("Soit la matrice suivante: \n\n", str(self.matrix),
                             "\n\nDonnez la transposée de cette matrice\n"
                             "Attention! arrondir les valeurs au millième près. Arrondi vers le haut à 5.\n: "))
        return(self.text)

    def check_result(self, awnser):
        """
        Vérifiera la réponse de l'utilisateur et le résultat généré par le code pour le calcul
        :param awnser: solution fournie par l'utilisateur, on utilisera un input dans main_matrix.py
        :return: result - boolean, si  la réponse est bonne renvoie True, sinon renvoie False
        """
        #result = np.array_equal(self.result, awnser)
        result = np.allclose(self.result, awnser)   # vérifie si égale avec une certaine précision (les valeurs de tolérance de base sont OK
        # Dans certains calculs de numpy on a pas le nombre exacte, exemple: 3 != 3.0000000000004
        return(result)


if __name__ == "__main__":
    print("Fin")