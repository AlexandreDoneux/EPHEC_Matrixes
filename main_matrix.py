# Alexandre Doneux
# Python 3.10

import exercices.matrix
from exercices import add_substr, mult_div, dot_product, determinant, inverse, transpose
import numpy as np
from ast import literal_eval

# ----------------------------------------------------------------------------------------------------------


def running_ex(help_text):
    """
    Fonction s'occupant de faire tourner un exercice. Vérifiaction des commandes, réponses justes ou non,
    autre essai pour la réponse, retour au menu des exercices.
    :param help_text: Texte d'aide pour l'exercice en particulier.
    :return: False, renvoyé quand on introduit stop, quand veut quitter l'exercice et renvenir au menu
    """
    try_ex = True
    while try_ex:

        awnser = input(str(exercice))

        if awnser in ['help', 'stop']:
            if awnser == 'help':
                print(help_text)
            elif awnser == 'stop':
                print("Arrêt de l'exercice")
                exercice_running = False  # On ne fait plus tourner la boucle de l'exercice
                return exercice_running

        else:
            try:
                literal_eval(awnser)
            except ValueError:
                # si une erreur est générée par la transformation en numpy.ndarray de la réponse:
                print("Erreur! Veuillez insérer help stop ou la réponse sous le bon format (voir 'help').")
                continue
            except SyntaxError:
                # si une erreur est générée par la transformation en numpy.ndarray de la réponse:
                print("Erreur! Aucune réponse insérée")
                continue

            if exercice.check_result(
                    literal_eval(awnser)):  # literal_eval() -> transforme un string ressemblant à un tableau en tableau
                print("Correct \n")
                try_ex = False

            else:
                print("Incorrect.\n")
                test_retry = True
                while test_retry:  # Boucle pour demander si on veut réessayer en cas d'erreur
                    retry = input("Voulez-vous réessayer ? (oui/non) \n: ")
                    if retry == "non":
                        test_retry = False
                        try_ex = False
                        print("\nDommage....La réponse était: \n{0}\nEssayons un autre exercice\n"
                              .format(exercice.result))
                    elif retry == "oui":
                        test_retry = False
                        # try_ex = True  # On laisse la boucle pour réessayer l'exercice
                    else:
                        print("Répondez oui ou non seulement")


help_text = "\nLorsque la réponse est sous la forme d'une matrice vous devez l'écrire sous une forme " \
            "d'imbrications de crochets. Par exemple: [[1,2],[3,4]]\nTappez 'stop' pour sortir de l'exercice.\n"
help_text_123 = "Besoins d'infos sur la question ?  https://www.alloprof.qc.ca/fr/eleves/bv/mathematiques/les-opera" \
                "tions-sur-les-matrices-m1467  \n"
help_text_4 = "Besoins d'infos sur la question ? https://www.methodemaths.fr/determinant_matrice/  \n"
help_text_5 = "Besoins d'infos sur la question ? https://homeomath2.imingo.net/invmat.htm  \n"
help_text_6 = "Besoins d'infos sur la question ? https://uel.unisciel.fr/mathematiques/calculmat1/calculmat1_ch01/co/" \
              "apprendre_ch1_01_11.html  \n"

# -----------------------------------------------------------------------------------------------------------------------
app_running = True  # l'app tourne de base

while app_running:
    print("\n----------------------------------------------------------------------------------------------------------"
          "------------------------")
    print("Bienvenue dans cette application d'exercices sur les matrices. Tapez 'help' à tout moment pour obtenir de "
          "l'aide et stop pour quitter.\n")
    print("Quel type d'exercice voulez vous faire? \n"
          "     1.Additions et soustractions\n"
          "     2.Multiplications et divisions\n"
          "     3.Produits matriciels\n"
          "     4.Calcul de déterminants\n"
          "     5.Calculs de matrices inverses\n"
          "     6.Calculs de matrices transposées\n\n")
    ex_num = input("Indiquez le numéro correspondant: ")

# -----------------------------------------------------------------------------------------------------------------------
    try:
        int(ex_num)
    except ValueError:   # Test si ex_num peut être transformé en nombre. Si non -> 'stop' ou erreur
        if ex_num == "stop":
            print("Arrêt de l'application. A la prochaine fois")
            break
        else:
            print("Erreur! Tapez un numéro d'exercice ou 'stop pour arreter l'application.")
            continue

# -------------------------------------------------------------

    if int(ex_num) == 1:

        exercice_running = True
        while exercice_running:
            dim_x = np.random.randint(1, 4)
            dim_y = np.random.randint(1, 4)

            matrix1 = exercices.matrix.Matrix(dim_x, dim_y)
            matrix2 = exercices.matrix.Matrix(dim_x, dim_y)
            matrix1.get_random_values(-5, 5)
            matrix2.get_random_values(-5, 5)

            ex_num = np.random.randint(0, 2)  # détermine si on fera une addition ou une soustraction au hasard

            exercice = add_substr.ExerciceAddSubstr(matrix1, matrix2, ex_num)

            # En sortant de la fonction si on indique que l'exercice ne tourne plus, on break pour revenir au menu de
            # choix d'exercices
            if running_ex(help_text + help_text_123) is False:
                break


# -----------------------------------------------------------------------------------------------------------------------
    elif int(ex_num) == 2:

        exercice_running = True
        while exercice_running:
            dim_x = np.random.randint(1, 4)
            dim_y = np.random.randint(1, 4)

            matrix = exercices.matrix.Matrix(dim_x, dim_y)
            matrix.get_random_values(-5, 5)
            factor = np.random.randint(1, 5)

            ex_num = np.random.randint(0, 2)  # détermine si on fera une multiplication ou une division au hasard

            exercice = mult_div.ExerciceMultDiv(matrix, factor, ex_num)

            # En sortant de la fonction si on indique que l'exercice ne tourne plus on, break pour revenir au menu de
            # choix d'exercices
            if running_ex(help_text + help_text_123) is False:
                break

# -----------------------------------------------------------------------------------------------------------------------
    elif int(ex_num) == 3:

        exercice_running = True
        while exercice_running:
            dim_x = np.random.randint(1, 4)
            dim_y = np.random.randint(1, 4)  # dimension y de la première matrice et dimension x de la deuxième
            dim_y2 = np.random.randint(1, 4)

            matrix1 = exercices.matrix.Matrix(dim_x, dim_y)
            matrix2 = exercices.matrix.Matrix(dim_y, dim_y2)
            matrix1.get_random_values(-5, 5)
            matrix2.get_random_values(-5, 5)

            exercice = dot_product.DotProduct(matrix1, matrix2)

            if running_ex(help_text + help_text_123) is False:
                break

# -----------------------------------------------------------------------------------------------------------------------
    elif int(ex_num) == 4:

        exercice_running = True
        while exercice_running:
            dim = np.random.randint(1, 4)

            matrix = exercices.matrix.Matrix(dim, dim)
            matrix.get_random_values(-5, 5)

            exercice = determinant.Deter(matrix)

            if running_ex(help_text + help_text_4) is False:
                break

# -----------------------------------------------------------------------------------------------------------------------
    elif int(ex_num) == 5:

        exercice_running = True
        # Une matrice à une inverse que si elle est carrée et que son déterminant est nul (voir inverse.py)
        while exercice_running:
            dim = np.random.randint(1, 4)

            matrix = exercices.matrix.Matrix(dim, dim)
            matrix.get_random_values(-5, 5)

            exercice = inverse.Inverse(matrix)

            if running_ex(help_text + help_text_5) is False:
                break

# -----------------------------------------------------------------------------------------------------------------------
    elif int(ex_num) == 6:

        exercice_running = True
        while exercice_running:
            dim_x = np.random.randint(1, 4)
            dim_y = np.random.randint(1, 4)

            matrix = exercices.matrix.Matrix(dim_x, dim_y)
            matrix.get_random_values(-5, 5)

            exercice = transpose.Transpos(matrix)

            if running_ex(help_text + help_text_6) is False:
                break

# ---------------------------------------
    else:
        print("Erreur! Cet exercice n'existe pas.")


if __name__ == "__main__":
    pass

