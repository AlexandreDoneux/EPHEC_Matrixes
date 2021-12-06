# Alexandre Doneux
# Python 3.10

from exercices.matrix import Matrix  # techniquement je n'utilise pas la classe Matrix. J'utilise des objets mais pas besoin d'import
import numpy as np

class DotProduct:
    def __init__(self, matrix1, matrix2):
        """
        initialisation des attributs de la classe et calculera la somme et la différence des deux matrices
        :param matrix1: Première matrice pour le produit matriciel
        :param matrix2: Deuxième matrice pour le produit matriciel
        """
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        self.result = self.matrix1.dot_product(self.matrix2)
        self.text = ""

    def __str__(self):
        self.text = "".join(("Soit les matrices A et B suivantes: \n\n", str(self.matrix1), "\n\n", str(self.matrix2),
                             "\n\nDonnez le produit matriciel AxB\n: "))
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
