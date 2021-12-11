# Alexandre Doneux
# Python 3.10

from exercices.matrix import Matrix  # techniquement je n'utilise pas la classe Matrix. J'utilise des objets mais pas besoin d'import
from exercices.exercice import Exercice

class Deter(Exercice):
    def __init__(self, matrix):
        """
        initialisation des attributs de la classe et calculera le déterminant de la matrice
        :param matrix: matrice dont on calculera le déterminant
        """
        self.matrix = matrix
        matrix.get_determinant() # Calcule le déterminant de la matrice
        self.result = self.matrix.determinant
        self.text = ""

    def __str__(self):
        self.text = "".join(("Soit la matrice suivante: \n\n", str(self.matrix),
                             "\n\nDonnez le déterminant de cette matrice\n: "))
        return(self.text)



if __name__ == "__main__":
    pass