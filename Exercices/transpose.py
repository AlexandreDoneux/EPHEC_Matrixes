# Alexandre Doneux
# Python 3.10

from exercices.matrix import Matrix  # techniquement je n'utilise pas la classe Matrix. J'utilise des objets mais pas besoin d'import
from exercices.exercice import Exercice

class Transpos(Exercice):
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



if __name__ == "__main__":
    pass