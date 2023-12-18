# add_word.py
import pygame
import os


class AddWord:
    def __init__(
        self,
        hangman_directory,
    ):
        self.word_file = os.path.join(hangman_directory, "mots.txt")
        self.text_field = ""

    def is_too_short(self):
        if len(self.text_field) == 0:
            return True

    def append_to_text(self, new_letter):
        self.text_field = self.text_field + new_letter

    def return_text(self):
        self.text_field = self.text_field[:-1]
    
    def render_text_field(
        self,
        screen,
        MAIN_FONT,
        FOREGROUND,
        HALF_SCREEN_WIDTH,
        HALF_SCREEN_HEIGHT,
    ):
        text_field_surface = MAIN_FONT.render(self.text_field, True, FOREGROUND)
        text_field_center = text_field_surface.get_width() / 2
        text_field_x, text_field_y = (
            HALF_SCREEN_WIDTH - text_field_center,
            HALF_SCREEN_HEIGHT
        )
        screen.blit(text_field_surface, (text_field_x, text_field_y))

    def word_list_append(self):
        try:
            with open(self.word_file, "a") as file:
                new_word = self.text_field + os.linesep
                file.write(new_word)
        except FileNotFoundError:
            with open(self.word_file, "w") as file:
                file.write("")
                return []
