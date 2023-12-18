# main.py

# le module os permet d'établir dynamiquement le chemin vers le répertoire
# qui contient tous les fichiers nécessaires pour le programme.
import os

# pygame permet, dans notre cas, d'afficher une interface graphique et de
# gérer les inputs de l'utilisateur
import pygame

# imports des modules locaux
from start_menu import StartMenu
from hangman_logic import HangmanLogic
from hangman_display import HangmanDisplay
from add_word import AddWord


pygame.init()
# Les dimensions de l'écran sont des constants qui ne doivent pas changer
# Les noms des constants sont tout en majuscule.
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.font.init()

# Le chemin vers le répertoire et la police.
hangman_directory = os.path.dirname(os.path.abspath(__file__))
font_path = os.path.join(hangman_directory, "NotoSansMono-Regular.ttf")

# Rêgler la police et leurs tailles.
MAIN_FONT_SIZE = 20
MAIN_FONT = pygame.font.Font(font_path, MAIN_FONT_SIZE)

USED_LETTERS_FONT_SIZE = 15
USED_LETTERS_FONT = pygame.font.Font(font_path, USED_LETTERS_FONT_SIZE)

# Les couleurs pour le premier et arrière plan.
BACKGROUND = (32, 32, 64)
FOREGROUND = (0, 192, 255)

# Constants pour des positions souvent utilisés
SCREEN_TOP = 30
SCREEN_BOTTOM = 450
HALF_SCREEN_WIDTH = SCREEN_WIDTH / 2
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT / 2

# Instance de la clase StartMenu, le menu principale
sm = StartMenu(MAIN_FONT, FOREGROUND, HALF_SCREEN_WIDTH)


def hangman_play():
    # Les instances sont crées à chaque fois que la fonction hangman_play est
    # called, afin qu'une nouvelle partie recommence à chaque fois
    hl = HangmanLogic(hangman_directory)
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

    running = True
    while running:
        # Les surfaces sont à l'intérieur de la boucle car elles doivent
        # êtres mises à jour.
        life_count_surface = MAIN_FONT.render(f"{hl.life_count}/7", True, FOREGROUND)

        word_surface = MAIN_FONT.render(hl.play_field, True, FOREGROUND)

        used_letters_surface = USED_LETTERS_FONT.render(
            " ".join(hl.used_letters), True, FOREGROUND
        )

        screen.fill(BACKGROUND)
        # Honnêtement je ne suis pas satisfait avec le très grand nombre de
        # paramètres que cette méthode prend
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

        if hl.lose_state():
            hd.render_lose_screen(screen, HALF_SCREEN_WIDTH, SCREEN_TOP)
            running = False
        elif hl.win_state():
            hd.render_win_screen(screen, HALF_SCREEN_WIDTH, SCREEN_TOP)
            running = False

        pygame.display.flip()

        # boucle pour gérer les inputs
        for event in pygame.event.get():
            # Si une touche n'est pas appuyé, recommencer
            if event.type != pygame.KEYDOWN:
                continue

            # Si echap est appuyé, revenir au menu
            if event.key == pygame.K_ESCAPE:
                running = False

            # Si la touche n'est pas une lettre, recommencer
            if not (pygame.K_a <= event.key <= pygame.K_z):
                continue

            # pour obtenir le caractère correspondant à la touche
            letter = chr(event.key).lower()

            # si le caractère à déjà été utilisé, ignorer
            if hl.was_used(letter):
                continue

            # sinon rajouter au caract_res utilisé
            hl.add_to_used_letters(letter)

            # Si le caractère n'est pas dans le mot, ajouter au pendu
            if not hl.is_in_word(letter):
                hl.add_to_life_count()
                continue

            # si c'est dans le mot, le montrer
            hl.modify_play_field(letter)
    return True


def hangman_add():
    aw = AddWord(hangman_directory)
    running = True

    while running:
        screen.fill(BACKGROUND)
        aw.render_text_field(
            screen, MAIN_FONT, FOREGROUND, HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT
        )

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_ESCAPE:
                running = False

            # Si entrée est appuyé, ajouter le mot à la liste
            if event.key == pygame.K_RETURN:
                aw.word_list_append()

            # Pour effacer le dernier caractère
            if event.key == pygame.K_BACKSPACE:
                aw.return_text()

            if not (pygame.K_a <= event.key <= pygame.K_z):
                continue

            # afficher la lettre qui vient d'être entré
            letter = chr(event.key).lower()
            aw.append_to_text(letter)
    return True


def hangman_quit():
    return False


def main():
    # J'utilise une liste et ses index pour sélectionner les options
    selection = 0
    confirm_selection = [
        hangman_play,
        hangman_add,
        hangman_quit,
    ]

    running = True

    while running:
        screen.fill(BACKGROUND)
        sm.display_menu(screen, MAIN_FONT, FOREGROUND, HALF_SCREEN_WIDTH, selection)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_UP:
                # J'utilise le wrap-around modulo pour sélectionner les options
                selection = (selection + 3 - 1) % 3
            elif event.key == pygame.K_DOWN:
                selection = (selection + 3 + 1) % 3
            elif event.key == pygame.K_RETURN:
                running = confirm_selection[selection]()
            elif event.key == pygame.K_ESCAPE:
                running = False


if __name__ == "__main__":
    try:
        main()
        pygame.quit()
    except Exception as e:
        print(e)
