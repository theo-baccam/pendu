import pygame

from file_functions import font_path

BACKGROUND_COLOR = (39, 41, 70)
FOREGROUND_COLOR = (237, 160, 49)
SELECTION_COLOR = (231, 255, 238)

pygame.font.init()

FONT_SIZE = 32
FONT = pygame.font.Font(font_path, FONT_SIZE)

SECONDARY_FONT_SIZE = 18
SECONDARY_FONT = pygame.font.Font(font_path, SECONDARY_FONT_SIZE)
