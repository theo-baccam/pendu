import pygame

from file_functions import font_path

BACKGROUND_COLOR = (0, 16, 64)
FOREGROUND_COLOR = (0, 128, 192)
SELECTION_COLOR = (255, 255, 255)

pygame.font.init()

FONT_SIZE = 32
FONT = pygame.font.Font(font_path, FONT_SIZE)
