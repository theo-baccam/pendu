# hangman_logic.py
# J'importe que la méthode choice du module random
from random import choice

# os pour obtenir le repertoire où se trouve les fichiers
import os


class HangmanLogic:
    # __init__ est call lorsqu'on instancie une classe
    def __init__(self, hangman_directory):
        # le chemin vers le fichier mots.txt
        self.word_file = os.path.join(hangman_directory, "mots.txt")
        # mettre le contenu de mots.txt dans une liste
        self.word_list = self.word_list_loader()

        # selectionner un mot dans la liste
        self.random_word = self.random_word_select()
        self.play_field = "_" * len(self.random_word)

        # un compteur qui va jusqu'à 7, où le joueur perd
        self.life_count = 0

        # la liste de mots utilisés, qui est vide pour le moment
        self.used_letters = []

    def word_list_loader(self):
        # On essaye de charger le fichier deux fois, au cas où il n'existe pas
        for times in range(2):
            try:
                with open(self.word_file, "r") as file:
                    # On sépare les mots dans le fichier.
                    # et on enlève le dernière string de la liste,
                    # qui est vide à cause de `\n`
                    return file.read().split("\n")[:-1]
            except FileNotFoundError:
                with open(self.word_file, "w") as file:
                    # Si le fichier n'existe pas, on crée un fichier vide
                    file.write("")
                    return []

    # Pour choisir un mot dans la liste
    def random_word_select(self):
        return choice(self.word_list)

    # Pour vérifier si la lettre à déjà été utilisé
    def was_used(self, letter):
        if letter in self.used_letters:
            return True

    # Pour vérifier si la lettre est dans le mot
    def is_in_word(self, letter):
        if letter in self.random_word:
            return True

    # Pour ajouter une lettre à la liste de lettres utilisés
    def add_to_used_letters(self, letter):
        self.used_letters.append(letter)
        self.used_letters.sort()

    # Pour vérifier si le joueur à perdu
    def lose_state(self):
        LIFE_LIMIT = 7
        if self.life_count == LIFE_LIMIT:
            return True

    # Pour vérifier si le jouer à gagné
    def win_state(self):
        if self.play_field == self.random_word:
            return True

    # Pour ajouter la lettre dans la grille vide.
    def modify_play_field(self, letter):
        for index, character in enumerate(self.random_word):
            if letter == character:
                self.play_field = (
                    self.play_field[:index] + letter + self.play_field[index + 1 :]
                )

    # Pour ajouter au compteur
    def add_to_life_count(self):
        self.life_count += 1
