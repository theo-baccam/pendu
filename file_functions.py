# file_functions contient tout ce qui concerne les chemins vers les fichiers.

import os

from pygame import image

# Chemin du repertoire contenant les fichiers pour le jeu
hangman_directory = os.path.dirname(os.path.abspath(__file__))

# Chemin vers le fichier pour la police
font_path = os.path.join(hangman_directory, "DejaVuSansMono.ttf")

# Chemin vers le fichier contenant la liste de mots
word_file_path = os.path.join(hangman_directory, "mots.txt")

# Tuple pour les images du pendu
image_list = (
    image.load(os.path.join(hangman_directory, "images", "hangman_0.png")),
    image.load(os.path.join(hangman_directory, "images", "hangman_1.png")),
    image.load(os.path.join(hangman_directory, "images", "hangman_2.png")),
    image.load(os.path.join(hangman_directory, "images", "hangman_3.png")),
    image.load(os.path.join(hangman_directory, "images", "hangman_4.png")),
    image.load(os.path.join(hangman_directory, "images", "hangman_5.png")),
    image.load(os.path.join(hangman_directory, "images", "hangman_6.png")),
    image.load(os.path.join(hangman_directory, "images", "hangman_7.png")),
)
