# Alexandre Doneux
# Python 3.10

import exercices.matrix
from exercices import add_substr, mult_div, dot_product, determinant, inverse, transpose
import numpy as np

app_running = True

while app_running:
    print("\n----------------------------------------------------------------------------------------------------------------------------------")
    print("Bienvenue dans cette application d'exercices sur les matrices. Tapez 'help' à tout moment pour obtenir de l'aide.\n")
    print("Quel type d'exercice voulez vous faire? \n"
          "     1.Additions et soustractions\n"
          "     2.Multiplications et divisions\n"
          "     3.Produits matriciels\n"
          "     4.Calcul de déterminants\n"
          "     5.Calculs de matrices inverses\n"
          "     6.Calculs de matrices transposées\n\n")
    ex_num = int(input("Indiquez le numéro correspondant: "))

    # dict_num_to_ex = {1: }

    if ex_num == 1:
        help_text = "Lorsque la réponse est sous la forme d'une matrice vous devez l'écrire sous une forme " \
                    "d'imbrications de crochets. Par exemple: [[1,2],[3,4]]\nTappez 'stop' pour sortir de l'exercice."
        exercice_running = True
        while exercice_running:
            dim_x = ex_num = np.random.randint(1, 4)
            dim_y= ex_num = np.random.randint(1, 4)

            matrix1 = exercices.matrix.Matrix(dim_x, dim_y)
            matrix2 = exercices.matrix.Matrix(dim_x, dim_y)
            matrix1.get_random_values(-5, 5)
            matrix2.get_random_values(-5, 5)

            ex_num = np.random.randint(0, 2)  # détermine si on fera une addition ou une soustraction au hasard -> vérifier

            exercice = add_substr.ExerciceAddSubstr(matrix1, matrix2, ex_num)

            awnser = input(str(exercice))
            if awnser in ['help', 'stop']:
                if awnser == 'help':
                    print(help_text)
                elif awnser == 'stop':
                    print("Arrêt de l'exercice")
                    break

            if exercice.check_result(awnser) == True:   # vérifier que le mode d'écriture de l'utilisateur est ok pour la comparaison des matrices
                print("Correct")
            else:
                print("Incorrect. Vous avez une seconde chance: \n")
                #awnser = input(str(exercice))

            exercice_running = False
    app_running = False
