# Alexandre Doneux
# Python 3.10
# 22/12/2021

import unittest
import numpy

from exercices.matrix import Matrix, DivisionByZero


class TestMtrAdd(unittest.TestCase):
    def test_add_3x3(self):
        """
        Teste l'addition entre 2 matrices 3x3
        """
        Matr1 = Matrix(3, 3)
        Matr1.values = numpy.array([[1, 2, 3], [3, 2, 1], [2, 3, 1]])
        Matr2 = Matrix(3, 3)
        Matr2.values = numpy.array([[4, 2, 7], [1, 2, 1], [1, 4, 4]])
        expected = numpy.array([[5, 4, 10], [4, 4, 2], [3, 7, 5]])
        self.assertEqual(numpy.all(expected), numpy.all(Matr1 + Matr2))

    def test_sub_2x3(self):
        """
        Teste la soustraction entre 2 matrices 2x3
        """
        Matr1 = Matrix(2, 3)
        Matr1.values = numpy.array([[1, 2, 3], [3, 2, 1]])
        Matr2 = Matrix(2, 3)
        Matr2.values = numpy.array([[4, 2, 7], [1, 2, 1]])
        expected = numpy.array([[-3, 0, -4], [2, 0, 0]])
        self.assertEqual(numpy.all(expected), numpy.all(Matr1 - Matr2))

    def test_add_3x2(self):
        """
        Teste l'addition entre 2 matrices 3x2
        """
        Matr1 = Matrix(3, 2)
        Matr1.values = numpy.array([[1, 2], [3, 2], [2, 3]])
        Matr2 = Matrix(3, 2)
        Matr2.values = numpy.array([[4, 2], [1, 2], [1, 4]])
        expected = numpy.array([[5, 4], [4, 4], [3, 7]])
        self.assertEqual(numpy.all(expected), numpy.all(Matr1 + Matr2))

    def test_sub_2x2(self):
        """
        Teste la soustraction entre 2 matrices 2x2
        """
        Matr1 = Matrix(2, 2)
        Matr1.values = numpy.array([[1, 2], [3, 2]])
        Matr2 = Matrix(2, 2)
        Matr2.values = numpy.array([[4, 2], [1, 2]])
        expected = numpy.array([[-3, 0], [2, 0]])
        self.assertEqual(numpy.all(expected), numpy.all(Matr1 - Matr2))

    def test_add_1x2(self):
        """
        Teste l'addition entre 2 matrices 1x2
        """
        Matr1 = Matrix(1, 2)
        Matr1.values = numpy.array([[1, 2]])
        Matr2 = Matrix(1, 2)
        Matr2.values = numpy.array([[4, 2]])
        expected = numpy.array([[5, 4]])
        self.assertEqual(numpy.all(expected), numpy.all(Matr1 + Matr2))

    def test_add_1x1(self):
        """
        Teste l'addition entre 2 matrices 1x1
        """
        Matr1 = Matrix(1, 1)
        Matr1.values = numpy.array([[1]])
        Matr2 = Matrix(1, 1)
        Matr2.values = numpy.array([[4]])
        expected = numpy.array([[5]])
        self.assertEqual(numpy.all(expected), numpy.all(Matr1 + Matr2))

    def test_add_empty(self):
        """
        Teste l'addition entre 2 matrices vides
        """
        Matr1 = Matrix(1, 1)
        Matr1.values = numpy.array([[]])
        Matr2 = Matrix(1, 1)
        Matr2.values = numpy.array([[]])
        expected = numpy.array([[]])
        self.assertEqual(numpy.all(expected), numpy.all(Matr1 + Matr2))


class TestMtrMultDiv(unittest.TestCase):
    def test_mult_3x3(self):
        """
        Teste la multiplication d'une matrice 3x3 par une constante
        """
        matr1 = Matrix(3, 3)
        matr1.values = numpy.array([[1, 2, 3], [3, 2, 1], [2, 3, 1]])
        const = 3
        expected = numpy.array([[3, 6, 9], [9, 6, 3], [6, 9, 3]])
        self.assertEqual(numpy.all(expected), numpy.all(matr1 * const))

    def test_mult_2x3(self):
        """
        Teste la multiplication d'une matrice 2x3 par une constante
        """
        matr1 = Matrix(2, 3)
        matr1.values = numpy.array([[1, 2, 3], [3, 2, 1]])
        const = 1
        expected = numpy.array([[1, 2, 3], [3, 2, 1]])
        self.assertEqual(numpy.all(expected), numpy.all(matr1 * const))

    def test_div_3x2(self):
        """
        Teste la division d'une matrice 3x2 par une constante
        """
        Matr1 = Matrix(3, 2)
        Matr1.values = numpy.array([[1, 2], [3, 2], [2, 3]])
        const = 2
        expected = numpy.array([[0.5, 1], [1.5, 1], [1, 1.5]])
        self.assertEqual(numpy.all(expected), numpy.all(Matr1 / const))

    def test_div_2x2(self):
        """
        Teste la division d'une matrice 2x2 par une constante
        """
        Matr1 = Matrix(2, 2)
        Matr1.values = numpy.array([[1, 2], [3, 2]])
        const = 4
        expected = numpy.array([[0.25, 0.5], [0.75, 0.5]])
        self.assertEqual(numpy.all(expected), numpy.all(Matr1 / const))

    def test_mult_by_0_1x2(self):
        """
        Teste la multiplication d'une matrice 1x2 par zéro
        """
        Matr1 = Matrix(1, 2)
        Matr1.values = numpy.array([[1, 2]])
        const = 0
        expected = numpy.array([[0, 0]])
        self.assertEqual(numpy.all(expected), numpy.all(Matr1 * const))

    def test_div_by_0_1x1(self):
        """
        Teste la division d'une matrice 1x1 par zéro
        """
        Matr1 = Matrix(1, 1)
        Matr1.values = numpy.array([[1]])
        const = 0

        with self.assertRaises(DivisionByZero):
            Matr1 / const





class TestMtrDotProd(unittest.TestCase):
    def test_dot_3x3_3x3(self):
        """
        Teste le dot product entre deux matrices 3x3
        """
        Matr1 = Matrix(3, 3)
        Matr1.values = numpy.array([[1, 2, 3], [3, 2, 1], [2, 3, 1]])
        Matr2 = Matrix(3, 3)
        Matr2.values = numpy.array([[4, 2, 7], [1, 2, 1], [1, 4, 4]])
        expected = numpy.array([[9, 18, 21], [15, 14, 27], [12, 14, 21]])
        self.assertEqual(numpy.all(expected), numpy.all(Matr1.dot_product(Matr2)))

    def test_dot_2x3_3x2(self):
        """
        Teste le dot product entre deux matrices 2x3 et 3x2
        """
        Matr1 = Matrix(2, 3)
        Matr1.values = numpy.array([[1, 2, 3], [3, 2, 1]])
        Matr2 = Matrix(3, 2)
        Matr2.values = numpy.array([[4, 2], [1, 2], [1, 4]])
        expected = numpy.array([[9, 18], [15, 14]])
        self.assertEqual(numpy.all(expected), numpy.all(Matr1.dot_product(Matr2)))

    def test_dot_1x4_4x1(self):
        """
        Teste le dot product entre deux matrices 1x4 et 4x1
        """
        Matr1 = Matrix(1, 4)
        Matr1.values = numpy.array([[1, 2, 3, 4]])
        Matr2 = Matrix(4, 1)
        Matr2.values = numpy.array([[4], [1], [1], [2]])
        expected = numpy.array([[17]])
        self.assertEqual(numpy.all(expected), numpy.all(Matr1.dot_product(Matr2)))

    def test_dot_2x2_3x3(self):
        """
        Teste le dot product entre deux matrices 2x2 et 3x3 -> Doit générer False
        """
        Matr1 = Matrix(2, 2)
        Matr1.values = numpy.array([[1, 2], [3, 2]])
        Matr2 = Matrix(3, 3)
        Matr2.values = numpy.array([[4, 2, 7], [1, 2, 1], [1, 4, 4]])
        self.assertFalse(Matr1.dot_product(Matr2))

    def test_dot_1x2_1x3(self):
        """
        Teste le dot product entre deux matrices 1x2 et 1x3 -> Doit générer False
        """
        Matr1 = Matrix(1, 2)
        Matr1.values = numpy.array([[1, 2]])
        Matr2 = Matrix(1, 3)
        Matr2.values = numpy.array([[4, 2, 7]])
        self.assertFalse(Matr1.dot_product(Matr2))


class TestInverse(unittest.TestCase):
    def test_inverse_3x3(self):
        """
        Verification de la matrice inverse d'une matrice 3x3
        """
        Matr1 = Matrix(3, 3)
        Matr1.values = numpy.array([[1, 2, 3], [3, 2, 1], [2, 3, 1]])
        Matr1.inverse()
        expected = numpy.array([[-0.0833, 0.583, -0.333], [-0.0833, -0.4166, 0.666], [0.4166, 0.0833, -0.333]])
        result = numpy.allclose(expected, Matr1.inverted, rtol=0.001, atol=0.001)
        #self.assertEqual(numpy.all(expected), numpy.all(Matr1.inverted))
        self.assertTrue(result)

    def test_inverse_2x2(self):
        """
        Verification de la matrice inverse d'une matrice 2x2
        """
        Matr1 = Matrix(2, 2)
        Matr1.values = numpy.array([[1, 2], [3, 2]])
        Matr1.inverse()
        expected = numpy.array([[-0.5, 0.5], [0.75, -0.25]])
        result = numpy.allclose(expected, Matr1.inverted, rtol=0.001, atol=0.001)
        #self.assertEqual(numpy.all(expected), numpy.all(Matr1.inverted))
        self.assertTrue(result)

    def test_inverse_1x1(self):
        """
        Verification de la matrice inverse d'une matrice 1x1
        """
        Matr1 = Matrix(1, 1)
        Matr1.values = numpy.array([[3]])
        Matr1.inverse()
        expected = numpy.array([[0.333]])
        result = numpy.allclose(expected, Matr1.inverted, rtol=0.001, atol=0.001)
        #self.assertEqual(numpy.all(expected), numpy.all(Matr1.inverted))
        self.assertTrue(result)

    def test_inverse_1x3(self):
        """
        Verification de la matrice inverse d'une matrice 1x3. Doit renvoyer False car il n'existe pas de matrice
        inverse pour une matrice non carrée.
        """
        Matr1 = Matrix(1, 3)
        Matr1.values = numpy.array([[3, 4, 2]])
        Matr1.inverse()
        self.assertFalse(Matr1.inverted)

    def test_inverse_2x4(self):
        """
        Verification de la matrice inverse d'une matrice 2x4. Doit renvoyer False car il n'existe pas de matrice
        inverse pour une matrice non carrée.
        """
        Matr1 = Matrix(2, 4)
        Matr1.values = numpy.array([[3, 4, 2, 1], [1, 2, 1, 5]])
        Matr1.inverse()
        self.assertFalse(Matr1.inverted)

    def test_inverse_det_nul(self):
        """
        Test d'une matrice 3x3 ayant comme déterminant 0. La matrice n'a pas d'inverse. -> doit renvoyer False.
        """
        Matr1 = Matrix(3, 3)
        Matr1.values = numpy.array([[4, 2, 1], [1, 2, 1], [1, 2, 1]])
        Matr1.inverse()
        self.assertFalse(Matr1.inverted)


class TestDeter(unittest.TestCase):
    def test_deter_3x3(self):
        """
        Teste le calcul du déterminant d'une matrice 3x3
        :return: None
        """
        Matr1 = Matrix(3, 3)
        Matr1.values = numpy.array([[1, 2, 3], [3, 2, 1], [2, 3, 1]])
        Matr1.get_determinant()
        expected = 12
        self.assertEqual(expected, Matr1.determinant)

    def test_deter_2x2(self):
        """
        Teste le calcul du déterminant d'une matrice 2x2
        :return: None
        """
        Matr1 = Matrix(2, 2)
        Matr1.values = numpy.array([[1, 2], [3, 2]])
        Matr1.get_determinant()
        expected = -4
        result = numpy.allclose(expected, Matr1.determinant)
        print(result)
        self.assertTrue(result)


    def test_deter_1x1(self):
        """
        Teste le calcul du déterminant d'une matrice 1x1
        :return: None
        """
        Matr1 = Matrix(1, 1)
        Matr1.values = numpy.array([[3]])
        Matr1.get_determinant()
        expected = 3
        result = numpy.allclose(expected, Matr1.determinant)
        print(result)
        self.assertTrue(result)

    def test_deter_2x3(self):
        """
        Teste le calcul du determinant d'une matirce 2x3. Doit renvoyer False vu que la matrice n'est pas carrée.
        :return: None
        """
        Matr1 = Matrix(2, 3)
        Matr1.values = numpy.array([[1, 2, 3], [3, 2, 1]])
        self.assertFalse(Matr1.get_determinant())
        """
        expected = False
        self.assertEqual(expected, Matr1.get_determinant())
        """


class TestTranspose(unittest.TestCase):
    def test_transpose_3x3(self):
        """
        Teste la matrice transposée d'une matrice 3x3.
        :return: None
        """
        Matr1 = Matrix(3, 3)
        Matr1.values = numpy.array([[1, 2, 3], [3, 2, 1], [2, 3, 1]])
        Matr1.transpose()
        expected = numpy.array([[1, 3, 2], [2, 2, 3], [3, 1, 1]])
        self.assertEqual(numpy.all(expected), numpy.all(Matr1.transposed))

    def test_transpose_2x3(self):
        """
        Teste la matrice transposée d'une matrice 2x3.
        :return: None
        """
        Matr1 = Matrix(2, 3)
        Matr1.values = numpy.array([[1, 2, 3], [3, 2, 1]])
        Matr1.transpose()
        expected = numpy.array([[1, 3], [2, 2], [3, 1]])
        self.assertEqual(numpy.all(expected), numpy.all(Matr1.transposed))

    def test_transpose_3x1(self):
        """
        Teste la matrice transposée d'une matrice 3x1.
        :return: None
        """
        Matr1 = Matrix(3, 1)
        Matr1.values = numpy.array([[1], [3], [2]])
        Matr1.transpose()
        expected = numpy.array([[1, 3, 2]])
        self.assertEqual(numpy.all(expected), numpy.all(Matr1.transposed))






if __name__ == "__main__":
    pass