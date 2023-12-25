import pygame

from file_functions import font_path

BACKGROUND_COLOR = (0, 16, 64)
FOREGROUND_COLOR = (0, 128, 192)
SELECTION_COLOR = (255, 255, 255)

pygame.font.init()

FONT_SIZE = 32
FONT = pygame.font.Font(font_path, FONT_SIZE)


selection_value = 0


def draw_background(screen):
    screen.fill(BACKGROUND_COLOR)


def draw_title(screen):
    TITLE_SURFACE = FONT.render("Le pendu", True, FOREGROUND_COLOR)
    TITLE_MIDDLE = TITLE_SURFACE.get_width() / 2
    screen.blit(TITLE_SURFACE, (320 - TITLE_MIDDLE, 120))


def render_options(screen):
    NEW_GAME_SURFACE = FONT.render("Jouer", True, FOREGROUND_COLOR)
    NEW_GAME_MIDDLE = NEW_GAME_SURFACE.get_width() / 2

    ADD_WORD_SURFACE = FONT.render("Ajouter mot", True, FOREGROUND_COLOR)
    ADD_WORD_MIDDLE = ADD_WORD_SURFACE.get_width() / 2

    QUIT_GAME_SURFACE = FONT.render("Quitter", True, FOREGROUND_COLOR)
    QUIT_GAME_MIDDLE = QUIT_GAME_SURFACE.get_width() / 2

    if selection_value == 0:
        NEW_GAME_SURFACE = FONT.render("Jouer", True, SELECTION_COLOR)
    elif selection_value == 1:
        ADD_WORD_SURFACE = FONT.render("Ajouter mot", True, SELECTION_COLOR)
    elif selection_value == 2:
        QUIT_GAME_SURFACE = FONT.render("Quitter", True, SELECTION_COLOR)
    else:
        raise ValueError("Valeur selection invalide")

    screen.blit(NEW_GAME_SURFACE, (320 - NEW_GAME_MIDDLE, 240))
    screen.blit(ADD_WORD_SURFACE, (320 - ADD_WORD_MIDDLE, 280))
    screen.blit(QUIT_GAME_SURFACE, (320 - QUIT_GAME_MIDDLE, 320))
