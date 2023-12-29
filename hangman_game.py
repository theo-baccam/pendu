import os
from random import choice

import pygame

import display_values as dv
import file_functions as ff

pygame.font.init()

def word_list_loader():
    with open(ff.word_file_path, "r") as file:
        word_list = file.read().split(os.linesep)
        word_list.pop(-1)
        return word_list




def word_chooser(word_list):
    random_word = choice(word_list)
    return random_word


def draw_background(screen):
    screen.fill(dv.BACKGROUND_COLOR)


def draw_image(screen, life_count):
    hangman_center_x, hangman_center_y = (
        ff.image_list[life_count].get_width() / 2,
        ff.image_list[life_count].get_height() / 2,
    )

    hangman_x, hangman_y = (
        320 - hangman_center_x,
        160 - hangman_center_y,
    )

    screen.blit(ff.image_list[life_count], (hangman_x, hangman_y))


def draw_text_field(screen, text_field):
    text_field_surface = dv.FONT.render(text_field, True, dv.FOREGROUND_COLOR)
    text_field_middle = text_field_surface.get_width() / 2
    screen.blit(text_field_surface, (320 - text_field_middle, 320))


def draw_used_letters(screen, used_letter_list):
    used_letters_surface = dv.SECONDARY_FONT.render(" ".join(used_letter_list), True, dv.FOREGROUND_COLOR)
    used_letters_middle = used_letters_surface.get_width() / 2
    screen.blit(used_letters_surface, (320 - used_letters_middle, 384))


def is_letter_in_word(random_word, key_name):
    in_word = False
    for letter in random_word:
        if key_name == letter:
            in_word = True
    return in_word


def letter_was_used(used_letter_list, key_name):
    if key_name in used_letter_list:
        return True
    else:
        return False


def modify_text_field(random_word, text_field, key_name):
    for index, letter in enumerate(random_word):
        if key_name == letter:
            text_field = text_field[:index] + key_name + text_field[index + 1:]

    return text_field


def render_lose_screen(screen, random_word):
    LOSE_SURFACE = dv.FONT.render("Vous avez perdu!", True, dv.FOREGROUND_COLOR)
    LOSE_MIDDLE = LOSE_SURFACE.get_width() / 2
    screen.blit(LOSE_SURFACE, (320 - LOSE_MIDDLE, 208))

    random_word_surface = dv.FONT.render(random_word, True, dv.FOREGROUND_COLOR)
    random_word_middle = random_word_surface.get_width() / 2
    screen.blit(random_word_surface, (320 - random_word_middle, 320))


def render_win_screen(screen, random_word):
    WIN_SURFACE = dv.FONT.render("Vous avez gagné!", True, dv.FOREGROUND_COLOR)
    WIN_MIDDLE = WIN_SURFACE.get_width() / 2
    screen.blit(WIN_SURFACE, (320 - WIN_MIDDLE, 208))

    random_word_surface = dv.FONT.render(random_word, True, dv.FOREGROUND_COLOR)
    random_word_middle = random_word_surface.get_width() / 2
    screen.blit(random_word_surface, (320 - random_word_middle, 320))


def hangman_game(screen):
    running = True

    MAX_LIFE_COUNT = 7
    life_count = 0

    word_list = word_list_loader()
    used_letter_list = []
    random_word = word_chooser(word_list)
    text_field = "_" * len(random_word)

    while running:
        for event in pygame.event.get():
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_ESCAPE:
                running = False

            if life_count == 7 or text_field == random_word:
                continue

            if pygame.K_a <= event.key <= pygame.K_z:
                key_name = pygame.key.name(event.key)
                if letter_was_used(used_letter_list, key_name):
                    continue
                used_letter_list.append(key_name)
                used_letter_list.sort()

                if not is_letter_in_word(random_word, key_name):
                    life_count += 1
                    continue

                text_field = modify_text_field(random_word, text_field, key_name)

        draw_background(screen)
        draw_image(screen, life_count)
        draw_used_letters(screen, used_letter_list)

        if life_count == 7:
            render_lose_screen(screen, random_word)
        elif text_field == random_word:
            render_win_screen(screen, random_word)
        else:
            draw_text_field(screen, text_field)

        pygame.display.flip()

