# Alexandre Doneux
# Python 3.10

from exercices.exercice import Exercice


class ExerciceAddSubstr(Exercice):
    def __init__(self, matrix1, matrix2, type_ex):
        """
        initialisation des attributs de la classe et calculera la somme et la différence des deux matrices
        :param matrix1: Première matrice pour l'addition ou soustraction
        :param matrix2: Deuxième matrice pour l'addition ou soustraction
        :param: type_ex: int, si égal à 0, on fait une addition, si égale à 1 une soustraction
        """
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        self.type_ex = type_ex

        self.ex_name = [" l'addition A + B", " la soustraction A - B"]

        """
        if type_ex == 0:
            self.result = self.matrix1.values + self.matrix2.values
        elif type_ex == 1:
            self.result = self.matrix1.values - self.matrix2.values
        """

        self.result = self.matrix1.values + self.matrix2.values if type_ex == 0 else \
            self.matrix1.values - self.matrix2.values

        self.text = ""

    def __str__(self):
        self.text = "".join(("Soit les matrices A et B suivantes: \n\n", str(self.matrix1), "\n\n", str(self.matrix2),
                             "\n\nDonnez", self.ex_name[self.type_ex], "\n"
                             "Attention! arrondir les valeurs au millième près. Arrondi vers le haut à 5.\n: "))
        return self.text


if __name__ == "__main__":
    pass
