# start_menu.py

# module pygame pour affichage graphique
import pygame


class StartMenu:
    # fonction lorsqu'une classe est instanciée
    def __init__(
        self,
        MAIN_FONT,
        FOREGROUND,
        HALF_SCREEN_WIDTH,
    ):
        self.WHITE = (255, 255, 255)
        self.TITLE_SURFACE = MAIN_FONT.render("Le pendu", True, FOREGROUND)
        self.TITLE_CENTER = self.TITLE_SURFACE.get_width() / 2
        self.TITLE_X, self.TITLE_Y = (
            HALF_SCREEN_WIDTH - self.TITLE_CENTER,
            144,
        )

        # liste + index pour les options du menu
        self.menu_options = [
            "Jouer",
            "Ajouter mot",
            "Quitter",
        ]

    def display_menu(self, screen, MAIN_FONT, FOREGROUND, HALF_SCREEN_WIDTH, selection):
        option_surfaces = [
            MAIN_FONT.render(
                option,
                True,
                # Pour changer la couleur de la police si on "hover" dessus l'option
                self.WHITE if i == selection else FOREGROUND,
            )
            for i, option in enumerate(self.menu_options)
        ]

        option_positions = [
            (HALF_SCREEN_WIDTH - surface.get_width() / 2, 288 + i * 48)
            for i, surface in enumerate(option_surfaces)
        ]

        screen.blit(self.TITLE_SURFACE, (self.TITLE_X, self.TITLE_Y))
        for option, position in zip(option_surfaces, option_positions):
            screen.blit(option, position)
