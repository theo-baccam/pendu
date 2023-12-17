# start_menu.py
import pygame
import os


class StartMenu:
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
            self.WHITE if i == selection else FOREGROUND)
            for i, option in enumerate(self.menu_options)
        ]
        option_positions = [
            (HALF_SCREEN_WIDTH - surface.get_width() // 2, 288 + i * 48)
            for i, surface in enumerate(option_surfaces)
        ]
        screen.blit(self.TITLE_SURFACE, (self.TITLE_X, self.TITLE_Y))
        for option, position in zip(option_surfaces, option_positions):
            screen.blit(option, position)
