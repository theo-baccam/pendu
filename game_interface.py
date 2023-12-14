from game_logic import HangmanLogic
import pygame
import os

hl = HangmanLogic()

class HangmanDisplay:
    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH = 640
        self.SCREEN_HEIGHT = 480
        self.screen = (
            pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        )
        self.clock = pygame.time.Clock()
        self.running = True

        pygame.font.init()

        self.hangman_directory = os.path.dirname(os.path.abspath(__file__))
        self.font_path = (
            os.path.join(self.hangman_directory, "NotoSansMono-Regular.ttf")
        )

        self.MAIN_FONT_SIZE = 20
        self.MAIN_FONT = pygame.font.Font(self.font_path, self.MAIN_FONT_SIZE)

        self.USED_LETTERS_FONT_SIZE = 15
        self.USED_LETTERS_FONT = (
            pygame.font.Font(self.font_path, self.USED_LETTERS_FONT_SIZE)
        )

        self.BACKGROUND = (32, 32, 64)
        self.FOREGROUND = (0, 192, 255)

        self.SCREEN_TOP = 30
        self.SCREEN_BOTTOM = 450
        self.HALF_SCREEN_WIDTH = self.SCREEN_WIDTH / 2
        self.HALF_SCREEN_HEIGHT = self.SCREEN_HEIGHT / 2

        self.LOSE_SURFACE = (
            self.MAIN_FONT.render("Perdu!", True, self.FOREGROUND)
        )

        self.WIN_SURFACE = (
            self.MAIN_FONT.render("Gagné!", True, self.FOREGROUND)
        )

        self.solution_surface = (
            self.MAIN_FONT.render(hl.random_word, True, self.FOREGROUND)
        )
        self.solution_center = self.solution_surface.get_width() / 2
        self.solution_x, self.solution_y = (
            self.HALF_SCREEN_WIDTH - self.solution_center,
            self.SCREEN_BOTTOM - 30,
        )

        self.image_list = (
            pygame.image.load(os.path.join("images", "hangman_0.png")),
            pygame.image.load(os.path.join("images", "hangman_1.png")),
            pygame.image.load(os.path.join("images", "hangman_2.png")),
            pygame.image.load(os.path.join("images", "hangman_3.png")),
            pygame.image.load(os.path.join("images", "hangman_4.png")),
            pygame.image.load(os.path.join("images", "hangman_5.png")),
            pygame.image.load(os.path.join("images", "hangman_6.png")),
            pygame.image.load(os.path.join("images", "hangman_7.png")),
        )


    def render_lose_screen(self):
        LOSE_CENTER = self.LOSE_SURFACE.get_width() / 2
        LOSE_X, LOSE_Y = (
            self.HALF_SCREEN_WIDTH - LOSE_CENTER, self.SCREEN_TOP
        )
        self.screen.blit(self.LOSE_SURFACE, (LOSE_X, LOSE_Y))
        self.screen.blit(self.solution_surface, (self.solution_x, self.solution_y))
        pygame.display.flip()
        pygame.time.delay(3000)
        return False


    # Fonction pour afficher l'écran win.
    def render_win_screen(self):
        WIN_CENTER = self.WIN_SURFACE.get_width() / 2
        WIN_X, WIN_Y = (
            self.HALF_SCREEN_WIDTH - WIN_CENTER, self.SCREEN_TOP
        )
        self.screen.blit(self.WIN_SURFACE, (WIN_X, WIN_Y))
        self.screen.blit(self.solution_surface, (self.solution_x, self.solution_y))
        pygame.display.flip()
        pygame.time.delay(3000)
        return False


    # Fonction pour afficher l'interface principale
    def render_main_ui(
        self,
        word_surface,
        life_count_surface,
        used_letters_surface,
        image_list, life_count,
        ):
        word_center = word_surface.get_width() / 2
        word_x, word_y = (
            self.HALF_SCREEN_WIDTH - word_center, self.SCREEN_BOTTOM - 30
        )
        self.screen.blit(word_surface, (word_x, word_y))

        # Le compteur de vie
        life_count_x, life_count_y = 550, self.SCREEN_TOP
        self.screen.blit(life_count_surface, (life_count_x, life_count_y))

        # Affiche la liste de lettres utilisés tout en bas.
        used_letters_center = used_letters_surface.get_width() / 2
        used_letters_x, used_letters_y = (
            self.SCREEN_WIDTH / 2 - used_letters_center,
            self.SCREEN_BOTTOM,
        )
        self.screen.blit(used_letters_surface, (used_letters_x, used_letters_y))

        hangman_center_x, hangman_center_y = (
            self.image_list[hl.life_count].get_width() / 2,
            self.image_list[hl.life_count].get_height() / 2
        )
        hangman_x, hangman_y = (
            self.HALF_SCREEN_WIDTH - hangman_center_x,
            self.HALF_SCREEN_HEIGHT - hangman_center_y
        )
        self.screen.blit(self.image_list[hl.life_count], (hangman_x, hangman_y))

    def run_game(self):
        # Boucle principale pygame
        while self.running:
            # Puisque les valeurs changent, l'emplacement de
            # ces éléments de l'UI sont dans la boucle.
            life_count_surface = (
                self.MAIN_FONT.render(f"{hl.life_count}/7", True, self.FOREGROUND)
            )

            word_surface = self.MAIN_FONT.render(hl.play_field, True, self.FOREGROUND)

            used_letters_surface = self.USED_LETTERS_FONT.render(
                " ".join(hl.used_letters), True, self.FOREGROUND
            )

            # Pour dessiner le fond et l'ui principale
            self.screen.fill(self.BACKGROUND)
            self.render_main_ui(
                word_surface,
                life_count_surface,
                used_letters_surface,
                self.image_list, 
                hl.life_count
            )

            # Si la partie est finie, afficher l'écran approprié
            if hl.lose_state():
                self.running = self.render_lose_screen()
            elif hl.win_state():
                self.running = self.render_win_screen()

            # Mettre à jour l'écran
            pygame.display.flip()

            # Boucle pour détecter l'input de l'utilisateur
            # Early returns pour empêcher du nesting excessif
            for event in pygame.event.get():
                # Si une clé n'a pas été appuyer, revenir au début
                if event.type != pygame.KEYDOWN:
                    continue

                if not event.key >= pygame.K_a and event.key <= pygame.K_z:
                    # Si ce n'est pas une touche lettre, revenir au début
                    continue

                # chr pour spécifier la lettre correspondant à la touche
                # puis la mettre en minuscule
                letter = chr(event.key).lower()

                # Si cette lettre a déjà été utilisé, ignorer
                if hl.was_used(letter):
                    continue

                # Ajouter la nouvelle lettre à liste de lettres utilisés
                hl.add_to_used_letters(letter)

                # Si la lettre n'est pas dans le mot, rajouter un "membre" au pendu.
                if not hl.is_in_word(letter):
                    hl.add_to_life_count()
                    continue

                hl.modify_play_field(letter)

        pygame.quit()
