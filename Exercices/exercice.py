# Alexandre Doneux
# Python 3.10
# UTF-8

import numpy as np

class Exercice:
    def __init__(self):
        self.result

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
        return (result)

if __name__ == "__main__":
    pass