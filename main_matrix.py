# Alexandre Doneux
# Python 3.10

import exercices.matrix
from exercices import add_substr, mult_div, dot_product, determinant, inverse, transpose
import numpy as np
from ast import literal_eval

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
            dim_x = np.random.randint(1, 4)
            dim_y = np.random.randint(1, 4)

            matrix1 = exercices.matrix.Matrix(dim_x, dim_y)
            matrix2 = exercices.matrix.Matrix(dim_x, dim_y)
            matrix1.get_random_values(-5, 5)
            matrix2.get_random_values(-5, 5)

            ex_num = np.random.randint(0, 2)  # détermine si on fera une addition ou une soustraction au hasard -> vérifier

            exercice = add_substr.ExerciceAddSubstr(matrix1, matrix2, ex_num)

            try_ex = True
            while try_ex:
                awnser = input(str(exercice))

                if awnser in ['help', 'stop']:
                    if awnser == 'help':
                        print(help_text)
                    elif awnser == 'stop':
                        print("Arrêt de l'exercice")
                        exercice_running = False # On ne fait plus tourner la boucle de l'exercice
                        break

                elif exercice.check_result(literal_eval(awnser)):   # literal_eval() -> transforme un string ressemblant à un tableau en tableau
                    print("Correct")
                    try_ex = False

                else:
                    print("Incorrect.\n")
                    test_retry = True
                    while test_retry:  # Boucle pour demander si on veut réessayer en cas d'erreur
                        retry = input("Voulez-vous réessayer ? (oui/non) \n")
                        if retry == "non":
                            test_retry = False
                            try_ex = False
                        elif retry == "oui":
                            test_retry = False
                            #try_ex = True  # On laisse la boucle pour réessayer l'exercice
                        else:
                            print("Répondez oui ou non seulement")



            #exercice_running = False
    app_running = False

if __name__ == "__main__":
    print("salut")

