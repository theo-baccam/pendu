# J'importe que la méthode choice du module random
from random import choice


# Gestion des mots dans la liste
class WordHandler:
    # Pour extraire les mots d'un fichier dans une liste.
    @staticmethod
    def word_list_loader():
        for times in range(2):
            try:
                with open("mots.txt", "r") as file:
                    word_list = file.read().split("\n")
                    word_list.pop(-1)
                return word_list
            # Créer le fichier si il n'existe pas
            except FileNotFoundError:
                with open("mots.txt", "w") as file:
                    file.write("")

    word_list = word_list_loader()

    # Pour extraire un mot aléaotirement dans la liste de mots
    @staticmethod
    def random_word_select(word_list):
        random_word = choice(word_list)
        return random_word

    random_word = random_word_select(word_list)


# Pour vérifier ce qui fût saisie
class VerifyInput:
    # Si la lettre à déjà été utilisé
    @staticmethod
    def was_used(letter):
        if letter in LetterHandler.used_letters:
            return True

    # Si la lettre est dans le mot
    @staticmethod
    def is_in_word(letter, random_word):
        if letter in random_word:
            return True


# Pour rajouter les lettres qui fût utilisé dans une liste
class LetterHandler:
    used_letters = []

    @staticmethod
    def add_to_used_letters(letter):
        LetterHandler.used_letters.append(letter)
        LetterHandler.used_letters.sort()


# Sur le résultat de la partie
class GameState:
    @staticmethod
    def lose_state(count):
        LIFE_LIMIT = 7
        if count == LIFE_LIMIT:
            return True

    @staticmethod
    def win_state(play_field, random_word):
        if play_field == random_word:
            return True


# Pour montrer la lettre si elle est correct.
def modify_play_field(letter, play_field, random_word):
    for index, character in enumerate(random_word):
        if letter == character:
            play_field = play_field[:index] + letter + play_field[index + 1 :]
    return play_field
