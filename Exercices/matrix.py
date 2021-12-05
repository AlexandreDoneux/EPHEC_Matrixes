# Alexandre Doneux
# Python 3.10
# Début: 4/12/2021

import numpy as np

class Matrix:
    def __init__(self, dim_x, dim_y):
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.determinant = False
        self.inverted = False  # Une matrice peut ne pas avoir de matrice inverse
        self.transposed = np.ones((dim_y, dim_x))   # Attention: transposée -> dimensions inversée, ex: 2x3 -> 3x2
        self.values = np.ones((dim_x, dim_y))   # .ones(utilise un tuple pour avoir les dimensions de la matrice

    def __str__(self):
        return(str(self.values))  # Transformation en string car self. values est de type numpy.ndarray


    def __add__(self, matrix2):
        """
        Méthode additionnant deux matrices, les attributs "values" de l'objet et d'un autre.
        :param matrix2: Objet de type Matrix
        :return: result - numpy.ndarray, représente la somme des matrices
        """
        result = np.add( self.values, matrix2.values)
        return(result)

    def __sub__(self, matrix2):
        """
        Méthode soustrait une matrice à la notre.
        :param matrix2: Objet de type Matrix
        :return: result - numpy.ndarray, représente la différence des matrices
        """
        result = np.subtract( self.values, matrix2.values)
        return(result)

    def __mul__(self, mult_factor):
        """
        Calcules la multiplication d'un matrices par un nombre entier
        :param mult_factor: int - nombre par lequel on va multiplier toutes les valeurs de la matrice
        :return: result - numpy.ndarray, matrice finale suite à la mutiplication de ses valeurs
        """
        result = np.multiply(self.values, mult_factor)
        return(result)

    def __truediv__(self, div_factor):
        """
        Calcules la division d'un matrices par un nombre entier
        :param div_factor: int - nombre par lequel on va diviser toutes les valeurs de la matrice
        :return: result - numpy.ndarray, matrice finale suite à la division de ses valeurs
        """
        result = np.true_divide(self.values, div_factor)

    def inverse(self):
        """
        Méthode calculant l'inverse de la matrice
        :param: None
        :return: None
        Mets dans l'attrribut "inverted" de l'objet l'inverse de la matrice(sous la forme d'un numpy.ndarray.
        """
        if np.linalg.det(self.values) != 0:
            self.inverted = np.around(np.linalg.inv(self.values), 2)  # numpy.around() -> arrondit les valeurs
        else:
            self.inverted = False  # Mets la-'inverse à False

    def transpose(self):
        """
        Matrice calculant la transposée de la matrice
        :param: None
        :return: None
        Mets dans l'attribut "transposed" de l'objet la transposée de la matrice (sous forme de numpy.ndarray).
        """
        self.transposed = np.transpose(self.values)


    def dot_product(self, matrix2):
        """
        Produit matriciel entre deux matrices. Le dim_y de la première doit être égale à dim_x de la deuxième
        :param matrix2: Objet de type Matrix
        :return: result - umpy.ndarray, solution du produit matriciel
        """
        if self.dim_y != matrix2.dim_x:
            return(False)   # si produit matriciel pas possible à cause des dimensions -> renvoit False

        result = np.dot(self.values, matrix2.values)
        return(result)

    def get_determinant(self):
        """
        Calcule le déterminant de la matrice
        :param: None
        :return: None
        Mets dans l'attribut "determinant" le déterminant de la matrice.
        """
        self.determinant = np.linalg.det(self.values)

    def get_random_values(self, low, high=0):
        """
        Génère des valeurs aléatoires pour la matrice
        :param low: int - valeur minimale que peuvent avoir lescomposants de la matrice
        :param high: int - valeur maximale que peuvent avoir lescomposants de la matrice
        :return: None
        Mets dans l'attribut "values" la matrice avec toutes ses valeurs nouvellement générées. self.values à la forme
        d'un numpy.ndarray.
        """
        self.values = np.random.randint(low, high, (self.dim_x, self.dim_y))

if __name__ == "__main__":

    matr1 = Matrix(3,3)
    matr1.get_random_values(2, 7)
    print(matr1)
    print(matr1*2)
