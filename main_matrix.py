# Alexandre Doneux
# Python 3.10

import exercices.matrix
from exercices import add_substr, mult_div, dot_product, determinant, inverse, transpose
import numpy as np
from ast import literal_eval
from matplotlib import pyplot

# ----------------------------------------------------------------------------------------------------------


def note_results(person_name, succeeded_ex, total_ex):
    """
    Fonction qui écrit dans un fichier results.txt les points qu'a eu une personne pendant une session d'exercices.
    :param
    - person_name:Nom de la personne ayant effectué l'exercice.
    - succeeded_ex: Nombre d'exercices réussis.
    - total_ex: Nombre total d'exercices effectués.
    :return: None
    """

    try:
        with open("results.txt", "a") as file:
            file.write(person_name + " " + succeeded_ex + " " + total_ex + "\n")

    except IOError:
        print("Erreur IO")
    # Pas d'except si le fichier n'existe pas. On ouvre à chaque fois le même fichier qui existera de base.

def affiche_result():
    """
    La fonction permets d'afficher un graph avec la moyenne de réussite pour chaque matricule. Il va lire ces infos dans
    results.txt.
    :return: None
    """
    dict_etud = {}
    try:
        with open("results.txt", ) as file:
            for line in file:
                # verification de la forme de chaque ligne si j'ai le temps (normalement pas besoin)
                line = line.strip("\n")
                line = line.strip()
                line = line.split()
                if line[0] in dict_etud.keys():
                    dict_etud[line[0]][0] += int(line[1])
                    dict_etud[line[0]][1] += int(line[2])
                    #dict_etud[line[0]] += line[1:]  # plus condensé ?
                else:
                    dict_etud[line[0]] = [int(line[1]), int(line[2])]
                    # on mets à chaque matricule le nombre d'ex réussis et le nombre total d'exercice

    except IOError:
        print("Erreur IO")
    # Pas d'except si le fichier n'existe pas. On ouvre à chaque fois le même fichier qui existera de base.

    averages = [(dict_etud[etudiant][0] / dict_etud[etudiant][1]) * 100 for etudiant in dict_etud.keys()]
    matricules = [etudiant for etudiant in dict_etud.keys()]

    all_total = 0
    all_succeeded = 0
    for etudiant in dict_etud.keys():
        all_succeeded += dict_etud[etudiant][0]
        all_total += dict_etud[etudiant][1]
    all_average = (all_succeeded / all_total) * 100  # moyenne totale de tous les étudiants (en %)
    print(all_average)
    print(all_succeeded)
    print(all_total)


    # Barres horizontales
    pyplot.barh(range(len(averages)), averages, height=0.7, color="yellow", edgecolor="orange", linestyle="solid",
                linewidth=3)
    pyplot.xlabel("Points moyens (%)")

    # Affichage des matricules
    pyplot.yticks(range(len(averages)), matricules)
    pyplot.axvline(x=all_average, color="green", linewidth=4, label="moyenne total")

    pyplot.legend(loc='upper right')
    pyplot.title("Moyenne des élèves")
    pyplot.show()



def running_ex(help_text, total_ex, succeeded_ex):
    """
    Fonction s'occupant de faire tourner un exercice. Vérifiaction des commandes, réponses justes ou non,
    autre essai pour la réponse, retour au menu des exercices.
    :param
    - help_text: Texte d'aide pour l'exercice en particulier.
    - total_ex: Nombre total d'exercices ayant été fait dans la session d'exercices
    - succeeded_ex: Nombre d'exercices réussis dans la session d'exercices
    :return:
    - False: renvoyé quand on introduit stop, quand veut quitter l'exercice et renvenir au menu
    - True: de base
    - total_ex: tout le temps, mis à jour
    - suceeded_ex: tout le temps, mis à jour
    """
    exercice_running = True
    # De base à True, représente si on fait des exercices dans la catégorie. Quand il est
    # renvoyé à False on sortira de la catégorie d'exercices

    try_ex = True  # représente le réessai de l'exercice
    while try_ex:

        awnser = input(str(exercice))

        if awnser in ['help', 'stop']:
            if awnser == 'help':
                print(help_text)
            elif awnser == 'stop':
                print("Arrêt de l'exercice")
                exercice_running = False  # On ne fait plus tourner la boucle de l'exercice
                return exercice_running, total_ex, succeeded_ex

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
                succeeded_ex += 1 # On ajoute un aux exercices réussi
                total_ex += 1  # On ajoute 1 au nombre total d'exercices faits

            else:
                print("Incorrect.\n")
                test_retry = True
                while test_retry:  # Boucle pour demander si on veut réessayer en cas d'erreur
                    retry = input("Voulez-vous réessayer ? (oui/non) \n: ")
                    if retry == "non":
                        test_retry = False
                        try_ex = False
                        total_ex +=1 # On ajoute 1 au nombre total d'exercices faits
                        print("\nDommage....La réponse était: \n{0}\nEssayons un autre exercice\n"
                              .format(exercice.result))
                    elif retry == "oui":
                        test_retry = False
                        # try_ex = True  # On laisse la boucle pour réessayer l'exercice
                    else:
                        print("Répondez oui ou non seulement")

    return exercice_running, total_ex, succeeded_ex

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
          "l'aide et stop pour quitter.\nEt tapez 'result' pour afficher les moyennes des étudiants.")
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
        elif ex_num == "result":
            affiche_result()
            continue
        else:
            print("Erreur! Tapez un numéro d'exercice, 'stop' pour arreter l'application ou 'result' pour afficher "
                  "la moyenne des résultats.")
            continue

# -------------------------------------------------------------

    if int(ex_num) == 1:
        total_ex = 0
        succeeded_ex = 0
        giving_name = True
        while giving_name:
            person_name = input("Donnez votre matricule (HE******): ")
            person_name = person_name.strip()

            # Vérifie Que le matricule à la bonne longeur, qu'il ne possède pas d'espace et qu'il commence par 'HE'
            if len(person_name) == 8 and person_name.split()[0] == person_name and person_name[:2] == "HE":
                giving_name = False

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

            result = running_ex(help_text + help_text_123, total_ex, succeeded_ex)
            exercice_running = result[0]
            succeeded_ex = result[1]
            total_ex = result[2]

            if exercice_running is False:
                note_results(person_name, str(succeeded_ex), str(total_ex))
                break


# -----------------------------------------------------------------------------------------------------------------------
    elif int(ex_num) == 2:
        total_ex = 0
        succeeded_ex = 0
        giving_name = True
        while giving_name:
            person_name = input("Donnez votre matricule (HE******): ")
            person_name = person_name.strip()
            # Vérifie Que le matricule à la bonne longeur, qu'il ne possède pas d'espace et qu'il commence par 'HE'
            if len(person_name) == 8 and person_name.split()[0] == person_name and person_name[:2] == "HE":
                giving_name = False

        exercice_running = True
        while exercice_running:
            dim_x = np.random.randint(1, 4)
            dim_y = np.random.randint(1, 4)

            matrix = exercices.matrix.Matrix(dim_x, dim_y)
            matrix.get_random_values(-5, 5)
            factor = np.random.randint(1, 5)

            ex_num = np.random.randint(0, 2)  # détermine si on fera une multiplication ou une division au hasard

            exercice = mult_div.ExerciceMultDiv(matrix, factor, ex_num)

            result = running_ex(help_text + help_text_123, total_ex, succeeded_ex)
            exercice_running = result[0]
            succeeded_ex = result[1]
            total_ex = result[2]

            if exercice_running is False:
                note_results(person_name, str(succeeded_ex), str(total_ex))
                break

# -----------------------------------------------------------------------------------------------------------------------
    elif int(ex_num) == 3:
        total_ex = 0
        succeeded_ex = 0
        giving_name = True
        while giving_name:
            person_name = input("Donnez votre matricule (HE******): ")
            person_name = person_name.strip()

            if len(person_name) == 8 and person_name.split()[0] == person_name and person_name[:2] == "HE":
                giving_name = False

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

            result = running_ex(help_text + help_text_123, total_ex, succeeded_ex)
            exercice_running = result[0]
            succeeded_ex = result[1]
            total_ex = result[2]

            if exercice_running is False:
                note_results(person_name, str(succeeded_ex), str(total_ex))
                break

# -----------------------------------------------------------------------------------------------------------------------
    elif int(ex_num) == 4:
        total_ex = 0
        succeeded_ex = 0
        giving_name = True
        while giving_name:
            person_name = input("Donnez votre matricule (HE******): ")
            person_name = person_name.strip()
            # Vérifie Que le matricule à la bonne longeur, qu'il ne possède pas d'espace et qu'il commence par 'HE'
            if len(person_name) == 8 and person_name.split()[0] == person_name and person_name[:2] == "HE":
                giving_name = False

        exercice_running = True
        while exercice_running:
            dim = np.random.randint(1, 4)

            matrix = exercices.matrix.Matrix(dim, dim)
            matrix.get_random_values(-5, 5)

            exercice = determinant.Deter(matrix)

            result = running_ex(help_text + help_text_123, total_ex, succeeded_ex)
            exercice_running = result[0]
            succeeded_ex = result[1]
            total_ex = result[2]

            if exercice_running is False:
                note_results(person_name, str(succeeded_ex), str(total_ex))
                break

# -----------------------------------------------------------------------------------------------------------------------
    elif int(ex_num) == 5:
        total_ex = 0
        succeeded_ex = 0
        giving_name = True
        while giving_name:
            person_name = input("Donnez votre matricule (HE******): ")
            person_name = person_name.strip()
            # Vérifie Que le matricule à la bonne longeur, qu'il ne possède pas d'espace et qu'il commence par 'HE'
            if len(person_name) == 8 and person_name.split()[0] == person_name and person_name[:2] == "HE":
                giving_name = False

        exercice_running = True
        # Une matrice à une inverse que si elle est carrée et que son déterminant est nul (voir inverse.py)
        while exercice_running:
            dim = np.random.randint(1, 4)

            matrix = exercices.matrix.Matrix(dim, dim)
            matrix.get_random_values(-5, 5)

            exercice = inverse.Inverse(matrix)

            result = running_ex(help_text + help_text_123, total_ex, succeeded_ex)
            exercice_running = result[0]
            succeeded_ex = result[1]
            total_ex = result[2]

            if exercice_running is False:
                note_results(person_name, str(succeeded_ex), str(total_ex))
                break

# -----------------------------------------------------------------------------------------------------------------------
    elif int(ex_num) == 6:
        total_ex = 0
        succeeded_ex = 0
        giving_name = True
        while giving_name:
            person_name = input("Donnez votre matricule (HE******): ")
            person_name = person_name.strip()
            # Vérifie Que le matricule à la bonne longeur, qu'il ne possède pas d'espace et qu'il commence par 'HE'
            if len(person_name) == 8 and person_name.split()[0] == person_name and person_name[:2] == "HE":
                giving_name = False

        exercice_running = True
        while exercice_running:
            dim_x = np.random.randint(1, 4)
            dim_y = np.random.randint(1, 4)

            matrix = exercices.matrix.Matrix(dim_x, dim_y)
            matrix.get_random_values(-5, 5)

            exercice = transpose.Transpos(matrix)

            result = running_ex(help_text + help_text_123, total_ex, succeeded_ex)
            exercice_running = result[0]
            succeeded_ex = result[1]
            total_ex = result[2]

            if exercice_running is False:
                note_results(person_name, str(succeeded_ex), str(total_ex))
                break

# ---------------------------------------
    else:
        print("Erreur! Cet exercice n'existe pas.")


if __name__ == "__main__":
    pass

