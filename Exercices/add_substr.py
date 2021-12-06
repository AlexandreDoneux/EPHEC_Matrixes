# Alexandre Doneux
# Python 3.10

from exercices.matrix import Matrix  # techniquement je n'utilise pas la classe Matrix. J'utilise des objets mais pas besoin d'import
import numpy as np

class ExerciceAddSubstr:
    def __init__(self, matrix1, matrix2, type_ex):
        """
        initialisation des attributs de la classe et calculera la somme et la différence des deux matrices
        :param matrix1: Première matrice pour l'addition ou soustraction
        :param matrix2: Deuxième matrice pour l'addition ou soustraction
        :param: type: int, si égal à 0, on fait une addition, si égale à 1 une soustraction
        """
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        self.type_ex = type_ex

        self.ex_name = [" l'addition A + B", " la soustraction A - B"]
        if type_ex == 0:
            self.result = self.matrix1.values + self.matrix2.values
        elif type_ex == 1:
            self.result = self.matrix1.values - self.matrix2.values

        self.text = ""

    def __str__(self):
        self.text = "".join(("Soit les matrices A et B suivantes: \n\n", str(self.matrix1), "\n\n", str(self.matrix2),
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


    if np.array_equal(np.ones((3,3)), [[1, 1, 1], [1, 1, 1], [1, 1, 1]]):
        print("marche")

    result = np.array_equal(np.ones((2, 2)), [[1, 1], [1, 1]])
    print(result)

    matrix3 = [[1, 2], [3, 4]]
    print(matrix3)
    print(np.array(matrix3))
    print(np.array_equal(matrix3, np.array(matrix3)))