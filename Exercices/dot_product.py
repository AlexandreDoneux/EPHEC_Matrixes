# Alexandre Doneux
# Python 3.10

from exercices.matrix import Matrix  # techniquement je n'utilise pas la classe Matrix. J'utilise des objets mais pas besoin d'import
from exercices.exercice import Exercice

class DotProduct(Exercice):
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
                             "\n\nDonnez le produit matriciel AxB\n"
                             "Attention! arrondir les valeurs au millième près. Arrondi vers le haut à 5.\n: "))
        return(self.text)




if __name__ == "__main__":
    pass
