# Code pour gérer l'affichage du menu principale

import pygame

import display_values as dv

pygame.font.init()

selection_value = 0


# Fonction pour afficher le fond
def draw_background(screen):
    screen.fill(dv.BACKGROUND_COLOR)


# Fonction pour afficher le titre
def draw_title(screen):
    TITLE_SURFACE = dv.FONT.render("Le pendu", True, dv.FOREGROUND_COLOR)
    TITLE_MIDDLE = TITLE_SURFACE.get_width() / 2
    screen.blit(TITLE_SURFACE, (320 - TITLE_MIDDLE, 120))


# Fonction pour afficher les options
def render_options(screen):
    NEW_GAME_SURFACE = dv.FONT.render("Jouer", True, dv.FOREGROUND_COLOR)
    NEW_GAME_MIDDLE = NEW_GAME_SURFACE.get_width() / 2

    ADD_WORD_SURFACE = dv.FONT.render("Ajouter mot", True, dv.FOREGROUND_COLOR)
    ADD_WORD_MIDDLE = ADD_WORD_SURFACE.get_width() / 2

    QUIT_GAME_SURFACE = dv.FONT.render("Quitter", True, dv.FOREGROUND_COLOR)
    QUIT_GAME_MIDDLE = QUIT_GAME_SURFACE.get_width() / 2

    # Changer la couleur de l'option si le joueur la survole
    if selection_value == 0:
        NEW_GAME_SURFACE = dv.FONT.render("Jouer", True, dv.SELECTION_COLOR)
    elif selection_value == 1:
        ADD_WORD_SURFACE = dv.FONT.render("Ajouter mot", True, dv.SELECTION_COLOR)
    elif selection_value == 2:
        QUIT_GAME_SURFACE = dv.FONT.render("Quitter", True, dv.SELECTION_COLOR)
    else:
        raise ValueError("Valeur selection invalide")

    screen.blit(NEW_GAME_SURFACE, (320 - NEW_GAME_MIDDLE, 240))
    screen.blit(ADD_WORD_SURFACE, (320 - ADD_WORD_MIDDLE, 280))
    screen.blit(QUIT_GAME_SURFACE, (320 - QUIT_GAME_MIDDLE, 320))


# Fonction pour afficher le texte indiquant les contrôles
def draw_hints(screen):
    ARROW_HINT_SURFACE_1 = dv.SECONDARY_FONT.render(
        "\u2191 et \u2193 pour naviguer",
        True,
        dv.FOREGROUND_COLOR
    )
    screen.blit(ARROW_HINT_SURFACE_1, (18, 18))

    ENTER_HINT = dv.SECONDARY_FONT.render(
        "\u23CE pour confirmer",
        True,
        dv.FOREGROUND_COLOR
    )

    screen.blit(ENTER_HINT, (18, 36))


def start_menu(screen):
    draw_background(screen)
    draw_title(screen)
    render_options(screen)
    draw_hints(screen)
