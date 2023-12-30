import pygame
from os import linesep

import display_values as dv
from file_functions import word_file_path

MAXIMUM_LENGTH = 32
text_field = ""


def draw_background(screen):
    screen.fill(dv.BACKGROUND_COLOR)


def draw_text_field(screen):
    text_field_surface = dv.FONT.render(text_field, True, dv.FOREGROUND_COLOR)
    text_field_middle = text_field_surface.get_width() / 2
    screen.blit(text_field_surface, (320 - text_field_middle, 240))


def draw_hints(screen):
    TEXT_HINT_SURFACE = dv.SECONDARY_FONT.render(
        "Donne un mot",
        True,
        dv.FOREGROUND_COLOR
    )
    screen.blit(TEXT_HINT_SURFACE, (18, 18))

    ENTER_HINT_SURFACE = dv.SECONDARY_FONT.render(
        "Ajoute le avec \u23CE",
        True,
        dv.FOREGROUND_COLOR
    )
    screen.blit(ENTER_HINT_SURFACE, (18, 36))

    QUIT_HINT_SURFACE = dv.SECONDARY_FONT.render(
        "ESC pour quitter",
        True,
        dv.FOREGROUND_COLOR
    )
    screen.blit(QUIT_HINT_SURFACE, (18, 54))


def append_to_file():
    with open(word_file_path, "a") as file:
        new_word = text_field + linesep
        file.write(new_word)


def input_loop():
    global running
    global text_field
    for event in pygame.event.get():
        if event.type != pygame.KEYDOWN:
            continue

        if event.key == pygame.K_ESCAPE:
            running = False

        if pygame.K_a <= event.key <= pygame.K_z:
            if len(text_field) == MAXIMUM_LENGTH:
                continue
            text_field = text_field + pygame.key.name(event.key)

        if event.key == pygame.K_BACKSPACE:
            text_field = text_field[:-1]

        if event.key == pygame.K_RETURN:
            append_to_file()
            text_field = ""


def add_word(screen):
    global running
    running = True
    while running:
        input_loop()
        draw_background(screen)
        draw_text_field(screen)
        draw_hints(screen)

        pygame.display.flip()
