# Alexandre Doneux
# Python 3.10

from exercices.matrix import Matrix  # techniquement je n'utilise pas la classe Matrix. J'utilise des objets mais pas besoin d'import

from ast import literal_eval
from exercices.exercice import Exercice

class Inverse(Exercice):
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



if __name__ == "__main__":
    pass