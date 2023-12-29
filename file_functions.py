import os

import pygame


hangman_directory = os.path.dirname(os.path.abspath(__file__))

font_path = os.path.join(hangman_directory, "NotoSansMono-Regular.ttf")

word_file_path = os.path.join(hangman_directory, "mots.txt")

image_list = (
    pygame.image.load(os.path.join(hangman_directory, "images", "hangman_0.png")),
    pygame.image.load(os.path.join(hangman_directory, "images", "hangman_1.png")),
    pygame.image.load(os.path.join(hangman_directory, "images", "hangman_2.png")),
    pygame.image.load(os.path.join(hangman_directory, "images", "hangman_3.png")),
    pygame.image.load(os.path.join(hangman_directory, "images", "hangman_4.png")),
    pygame.image.load(os.path.join(hangman_directory, "images", "hangman_5.png")),
    pygame.image.load(os.path.join(hangman_directory, "images", "hangman_6.png")),
    pygame.image.load(os.path.join(hangman_directory, "images", "hangman_7.png")),
)
