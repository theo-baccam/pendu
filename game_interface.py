from game_logic import HangmanLogic
import pygame
import os


class HangmanDisplay:
    def __init__(
        self,
        MAIN_FONT,
        FOREGROUND,
        HALF_SCREEN_WIDTH,
        SCREEN_BOTTOM,
        hangman_directory,
        random_word,
    ):
        self.hl = HangmanLogic()
        self.LOSE_SURFACE = MAIN_FONT.render("Perdu!", True, FOREGROUND)

        self.WIN_SURFACE = MAIN_FONT.render("Gagné!", True, FOREGROUND)

        self.solution_surface = MAIN_FONT.render(random_word, True, FOREGROUND)
        self.solution_center = self.solution_surface.get_width() / 2
        self.solution_x, self.solution_y = (
            HALF_SCREEN_WIDTH - self.solution_center,
            SCREEN_BOTTOM - 30,
        )

        self.image_list = (
            pygame.image.load(
                os.path.join(hangman_directory, "images", "hangman_0.png")
            ),
            pygame.image.load(
                os.path.join(hangman_directory, "images", "hangman_1.png")
            ),
            pygame.image.load(
                os.path.join(hangman_directory, "images", "hangman_2.png")
            ),
            pygame.image.load(
                os.path.join(hangman_directory, "images", "hangman_3.png")
            ),
            pygame.image.load(
                os.path.join(hangman_directory, "images", "hangman_4.png")
            ),
            pygame.image.load(
                os.path.join(hangman_directory, "images", "hangman_5.png")
            ),
            pygame.image.load(
                os.path.join(hangman_directory, "images", "hangman_6.png")
            ),
            pygame.image.load(
                os.path.join(hangman_directory, "images", "hangman_7.png")
            ),
        )

    def render_lose_screen(self, screen, HALF_SCREEN_WIDTH, SCREEN_TOP):
        LOSE_CENTER = self.LOSE_SURFACE.get_width() / 2
        LOSE_X, LOSE_Y = (HALF_SCREEN_WIDTH - LOSE_CENTER, SCREEN_TOP)
        screen.blit(self.LOSE_SURFACE, (LOSE_X, LOSE_Y))
        screen.blit(self.solution_surface, (self.solution_x, self.solution_y))
        pygame.display.flip()
        pygame.time.delay(3000)
        return False

    # Fonction pour afficher l'écran win.
    def render_win_screen(self, screen, HALF_SCREEN_WIDTH, SCREEN_TOP):
        WIN_CENTER = self.WIN_SURFACE.get_width() / 2
        WIN_X, WIN_Y = (HALF_SCREEN_WIDTH - WIN_CENTER, SCREEN_TOP)
        screen.blit(self.WIN_SURFACE, (WIN_X, WIN_Y))
        screen.blit(self.solution_surface, (self.solution_x, self.solution_y))
        pygame.display.flip()
        pygame.time.delay(3000)
        return False

    # Fonction pour afficher l'interface principale
    def render_main_ui(
        self,
        word_surface,
        life_count_surface,
        used_letters_surface,
        image_list,
        life_count,
        screen,
        SCREEN_WIDTH,
        HALF_SCREEN_WIDTH,
        HALF_SCREEN_HEIGHT,
        SCREEN_TOP,
        SCREEN_BOTTOM,
    ):
        word_center = word_surface.get_width() / 2
        word_x, word_y = (HALF_SCREEN_WIDTH - word_center, SCREEN_BOTTOM - 30)
        screen.blit(word_surface, (word_x, word_y))

        # Le compteur de vie
        life_count_x, life_count_y = 550, SCREEN_TOP
        screen.blit(life_count_surface, (life_count_x, life_count_y))

        # Affiche la liste de lettres utilisés tout en bas.
        used_letters_center = used_letters_surface.get_width() / 2
        used_letters_x, used_letters_y = (
            SCREEN_WIDTH / 2 - used_letters_center,
            SCREEN_BOTTOM,
        )
        screen.blit(used_letters_surface, (used_letters_x, used_letters_y))

        hangman_center_x, hangman_center_y = (
            self.image_list[self.hl.life_count].get_width() / 2,
            self.image_list[self.hl.life_count].get_height() / 2,
        )
        hangman_x, hangman_y = (
            HALF_SCREEN_WIDTH - hangman_center_x,
            HALF_SCREEN_HEIGHT - hangman_center_y,
        )
        screen.blit(self.image_list[self.hl.life_count], (hangman_x, hangman_y))
