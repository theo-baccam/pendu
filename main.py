# main.py
import pygame
import os
from game_logic import HangmanLogic
from game_interface import HangmanDisplay

pygame.init()
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.font.init()

hangman_directory = os.path.dirname(os.path.abspath(__file__))
font_path = os.path.join(hangman_directory, "NotoSansMono-Regular.ttf")

MAIN_FONT_SIZE = 20
MAIN_FONT = pygame.font.Font(font_path, MAIN_FONT_SIZE)

USED_LETTERS_FONT_SIZE = 15
USED_LETTERS_FONT = pygame.font.Font(font_path, USED_LETTERS_FONT_SIZE)

BACKGROUND = (32, 32, 64)
FOREGROUND = (0, 192, 255)

SCREEN_TOP = 30
SCREEN_BOTTOM = 450
HALF_SCREEN_WIDTH = SCREEN_WIDTH / 2
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT / 2

hl = HangmanLogic()
random_word = hl.random_word
hd = HangmanDisplay(
    MAIN_FONT,
    FOREGROUND,
    HALF_SCREEN_WIDTH,
    SCREEN_BOTTOM,
    hangman_directory,
    random_word,
    hl,
)

def main():
    running = True
    while running:
        # Puisque les valeurs changent, l'emplacement de
        # ces éléments de l'UI sont dans la boucle.
        life_count_surface = MAIN_FONT.render(f"{hl.life_count}/7", True, FOREGROUND)

        word_surface = MAIN_FONT.render(hl.play_field, True, FOREGROUND)

        used_letters_surface = USED_LETTERS_FONT.render(
            " ".join(hl.used_letters), True, FOREGROUND
        )

        # Pour dessiner le fond et l'ui principale
        screen.fill(BACKGROUND)
        hd.render_main_ui(
            word_surface,
            life_count_surface,
            used_letters_surface,
            hd.image_list,
            hl.life_count,
            screen,
            SCREEN_WIDTH,
            HALF_SCREEN_WIDTH,
            HALF_SCREEN_HEIGHT,
            SCREEN_TOP,
            SCREEN_BOTTOM,
        )

        # Si la partie est finie, afficher l'écran approprié
        if hl.lose_state():
            running = hd.render_lose_screen(screen, HALF_SCREEN_WIDTH, SCREEN_TOP)
        elif hl.win_state():
            running = hd.render_win_screen(screen, HALF_SCREEN_WIDTH, SCREEN_TOP)

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
            if hl.was_used(letter):
                continue

            # Ajouter la nouvelle lettre à liste de lettres utilisés
            hl.add_to_used_letters(letter)

            # Si la lettre n'est pas dans le mot, rajouter un "membre" au pendu.
            if not hl.is_in_word(letter):
                hl.add_to_life_count()
                continue

            hl.modify_play_field(letter)

    pygame.quit()


if __name__ == "__main__":
    main()