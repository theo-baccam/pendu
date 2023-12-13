# Pour obtenir les methodes, fonctions et variables de game_logic.py
from game_logic import *

# Le module pygame
import pygame

# Module qui permet d'intéragir avec le système d'exploitation
import os

# Abbreviation des noms de classe
word = WordHandler
verif = VerifyInput
lett = LetterHandler
game = GameState

pygame.init()

# Les constants permet de préciser la signifiance des nombres
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

pygame.font.init()

# Pour spécifier le repertoire où le script se trouve.
hangman_directory = os.path.dirname(os.path.abspath(__file__))

font_path = os.path.join(hangman_directory, "NotoSansMono-Regular.ttf")

# Spécifier les diffférentes tailles de polices
MAIN_FONT_SIZE = 20
MAIN_FONT = pygame.font.Font(font_path, MAIN_FONT_SIZE)

USED_LETTERS_FONT_SIZE = 15
USED_LETTERS_FONT = pygame.font.Font(font_path, USED_LETTERS_FONT_SIZE)

# Les valeurs des couleurs en RGB
BACKGROUND = (32, 32, 64)
FOREGROUND = (0, 192, 255)

play_field = "_" * len(word.random_word)

# Le nombre de "membres"
life_count = 0

# Constants pour des emplacements sur la fenêtre
SCREEN_TOP = 30
SCREEN_BOTTOM = 450
HALF_SCREEN_WIDTH = SCREEN_WIDTH / 2
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT / 2

# Les emplacements des surfaces pour le texte game-over et win.
LOSE_SURFACE = MAIN_FONT.render("Perdu!", True, FOREGROUND)

WIN_SURFACE = MAIN_FONT.render("Gagné!", True, FOREGROUND)

solution_surface = MAIN_FONT.render(word.random_word, True, FOREGROUND)
solution_center = solution_surface.get_width() / 2
solution_x, solution_y = HALF_SCREEN_WIDTH - solution_center, SCREEN_BOTTOM - 30


# Fonction pour afficher l'écran game-over
def render_lose_screen(LOSE_SURFACE):
    LOSE_CENTER = LOSE_SURFACE.get_width() / 2
    LOSE_X, LOSE_Y = HALF_SCREEN_WIDTH - LOSE_CENTER, SCREEN_TOP
    screen.blit(LOSE_SURFACE, (LOSE_X, LOSE_Y))
    screen.blit(solution_surface, (solution_x, solution_y))
    pygame.display.flip()
    pygame.time.delay(3000)
    return False


# Fonction pour afficher l'écran win.
def render_win_screen(WIN_SURFACE):
    WIN_CENTER = WIN_SURFACE.get_width() / 2
    WIN_X, WIN_Y = HALF_SCREEN_WIDTH - WIN_CENTER, SCREEN_TOP
    screen.blit(WIN_SURFACE, (WIN_X, WIN_Y))
    screen.blit(solution_surface, (solution_x, solution_y))
    pygame.display.flip()
    pygame.time.delay(3000)
    return False


# Fonction pour afficher l'interface principale
def render_main_ui(word_surface, life_count_surface, used_letters_surface, image_list, life_count):
    word_center = word_surface.get_width() / 2
    word_x, word_y = HALF_SCREEN_WIDTH - word_center, SCREEN_BOTTOM - 30
    screen.blit(word_surface, (word_x, word_y))

    # Le compteur de vie
    life_count_x, life_count_y = 550, SCREEN_TOP
    screen.blit(life_count_surface, (life_count_x, life_count_y))

    # Affiche la liste de lettres utilisés tout en bas.
    used_letters_center = used_letters_surface.get_width() / 2
    used_letters_x, used_letters_y = (
        SCREEN_WIDTH / 2 - used_letters_center,
        SCREEN_BOTTOM,
    )
    screen.blit(used_letters_surface, (used_letters_x, used_letters_y))

    hangman_center_x, hangman_center_y = (
        image_list[life_count].get_width() / 2,
        image_list[life_count].get_height() / 2
    )
    hangman_x, hangman_y = (
        HALF_SCREEN_WIDTH - hangman_center_x,
        HALF_SCREEN_HEIGHT - hangman_center_y
    )
    screen.blit(image_list[life_count], (hangman_x, hangman_y))

image_list = (
    pygame.image.load(os.path.join("images", "hangman_0.png")),
    pygame.image.load(os.path.join("images", "hangman_1.png")),
    pygame.image.load(os.path.join("images", "hangman_2.png")),
    pygame.image.load(os.path.join("images", "hangman_3.png")),
    pygame.image.load(os.path.join("images", "hangman_4.png")),
    pygame.image.load(os.path.join("images", "hangman_5.png")),
    pygame.image.load(os.path.join("images", "hangman_6.png")),
    pygame.image.load(os.path.join("images", "hangman_7.png")),
)


# Boucle principale pygame
while running:
    # Puisque les valeurs changent, l'emplacement de
    # ces éléments de l'UI sont dans la boucle.
    life_count_surface = MAIN_FONT.render(f"{life_count}/7", True, FOREGROUND)

    word_surface = MAIN_FONT.render(play_field, True, FOREGROUND)

    used_letters_surface = USED_LETTERS_FONT.render(
        " ".join(lett.used_letters), True, FOREGROUND
    )

    # Pour dessiner le fond et l'ui principale
    screen.fill(BACKGROUND)
    render_main_ui(word_surface, life_count_surface, used_letters_surface, image_list, life_count)

    # Si la partie est finie, afficher l'écran approprié
    if game.lose_state(life_count):
        running = render_lose_screen(LOSE_SURFACE)
    elif game.win_state(play_field, word.random_word):
        running = render_win_screen(WIN_SURFACE)

    # Mettre à jour l'écran
    pygame.display.flip()

    # Boucle pour détecter l'input de l'utilisateur
    # Early returns pour empêcher du nesting excessif
    for event in pygame.event.get():
        # Si une clé n'a pas été appuyer, revenir au début
        if event.type != pygame.KEYDOWN:
            continue

        if not event.key >= pygame.K_a and event.key <= pygame.K_z:
            # Si ce n'est pas une touche lettre, revenir au début
            continue

        # chr pour spécifier la lettre correspondant à la touche
        # puis la mettre en minuscule
        letter = chr(event.key).lower()

        # Si cette lettre a déjà été utilisé, ignorer
        if verif.was_used(letter):
            continue

        # Ajouter la nouvelle lettre à liste de lettres utilisés
        lett.add_to_used_letters(letter)

        # Si la lettre n'est pas dans le mot, rajouter un "membre" au pendu.
        if not verif.is_in_word(letter, word.random_word):
            life_count += 1
            continue

        # Mettre les nouvelles lettres entrés par l'utilisateur
        play_field = modify_play_field(letter, play_field, word.random_word)

pygame.quit()
