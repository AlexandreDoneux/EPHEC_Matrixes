# Alexandre Doneux
# Python 3.10

from exercices.matrix import Matrix
import numpy as np

exercice_running = True
#dict_level_number = {1: [], 2: [], 3: []}

while exercice_running:
    dim_x = np.random.randint(1, 3)
    dim_y = np.random.randint(1, 3)
    matrix1 = Matrix(dim_x, dim_y)
    matrix2 = Matrix(dim_x, dim_y)

    # Générer nombre pour savoir si addition ou soustraction
    ex_num = np.random.randint(1, 3)

    if ex_num == 1:
        print("Quel est la somme ...")

    if ex_num == 2:
        print("Quel est la soustraction de ...")

    exercice_running = False

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