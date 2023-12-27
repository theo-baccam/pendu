import os
from random import choice

import pygame

import display_values as dv
import file_functions as ff


pygame.font.init()

MAX_LIFE_COUNT = 7
life_count = 0
running = True


def draw_background(screen):
    screen.fill(dv.BACKGROUND_COLOR)


def draw_life_count(screen):
    life_count_surface = dv.FONT.render(
        f"{life_count}/{MAX_LIFE_COUNT}",
        True,
        dv.FOREGROUND_COLOR
    )
    screen.blit(life_count_surface, (576, 0))


def draw_image(screen):
    hangman_center_x, hangman_center_y = (
        ff.image_list[life_count].get_width() / 2,
        ff.image_list[life_count].get_height() / 2,
    )

    hangman_x, hangman_y = (
        320 - hangman_center_x,
        160 - hangman_center_y,
    )

    screen.blit(ff.image_list[life_count], (hangman_x, hangman_y))


def input_loop():
    global life_count
    global running
    for event in pygame.event.get():
        if event.type != pygame.KEYDOWN:
            continue

        if event.key == pygame.K_ESCAPE:
            running = False

        if event.key == pygame.K_UP:
            life_count += 1

        if event.key == pygame.K_DOWN:
            life_count -= 1


def hangman_game(screen):
    while running:
        input_loop()
        draw_background(screen)
        draw_life_count(screen)
        draw_image(screen)

        pygame.display.flip()
