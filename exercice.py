#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> bool:
    if values is None:
        ordre = True
        # TODO: Demander les valeurs ici
        liste_valeurs = list(input('Veuillez entrer 10 valeurs sans espace: ')) # On voulait seulement un seul type :(
        for index, element in enumerate(liste_valeurs):
            if index + 1 < len(liste_valeurs):
                if element > liste_valeurs[index + 1]:
                    ordre = False
            else:
                continue
    return ordre


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: Demander les mots ici
        pass

    return False


def contains_doubles(items: list) -> bool:
    my_set = set(my_list) 
    return len(my_list) == (len(my_set))


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    for nom in grades:
        grades[nom]
    return {name: result}


def histogram(sentence: str) -> tuple:
    # TODO: Créer l'histogramme a l'aide d'un dictionnaire
    #       Afficher l'histogramme et les lettres les plus fréquentes
    #       Retourner l'histogramme et le tableau de lettres

    return {}, []


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregistrer dans une structure de données 
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    name, result = best_grades(grades)
    print(f"{name} a la meilleure moyenne: {result}")
    
    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
