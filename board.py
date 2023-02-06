import pygame
from constants import *
import numpy

class Board:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.game_array = numpy.zeros((WINDOW_SIZE // CUBE_SIZE, WINDOW_SIZE // CUBE_SIZE))
        self.draw_board()
        self.turn = 1
        self.game_is_on = True

        

    def draw_board(self):
        # Drawing vertical lines
        for x in range(1, VERTICAL_LINES + 1):
            pygame.draw.line(self.screen, BLACK, (0, CUBE_SIZE * x), (CUBE_SIZE * 3, CUBE_SIZE * x), LINE_WIDTH)
        # Drawing horizontal lines
        for y in range(1, HORIZONTAL_LINES + 1):
            pygame.draw.line(self.screen, BLACK, (CUBE_SIZE * y, 0), (CUBE_SIZE * y, CUBE_SIZE * 3), LINE_WIDTH)

    # Changing turn
    def change_turn(self):
        self.turn *= -1

    # Checking if field is available
    def is_available(self, pos) -> bool:
        if self.game_array[pos[0]][pos[1]] == 0:
            return True
        return False
    
    # put mark on the field and change turn
    def put_mark(self, pos):
        if self.is_available(pos):
            # -1 is cross
            if self.turn == -1:
                # loading image of a cross
                img = pygame.image.load("Tic_Tac_Toe/resources/cross.png")
                img = pygame.transform.scale(img, (CUBE_SIZE // 1.5, CUBE_SIZE // 1.5))
            # 1 is dot
            elif self.turn == 1:
                # loading image of a dot
                img = pygame.image.load("Tic_Tac_Toe/resources/dot.png")
                img = pygame.transform.scale(img, (CUBE_SIZE // 1.5, CUBE_SIZE // 1.5))
            self.game_array[pos[0]][pos[1]] = self.turn
            x = pos[0] * CUBE_SIZE + CUBE_SIZE // 6
            y = pos[1] * CUBE_SIZE + CUBE_SIZE // 6
            self.screen.blit(img, (y, x))
            self.change_turn()

    # Winning line
    def draw_winning_line(self, start_pos:tuple, end_pos:tuple):
        start_x = start_pos[0] * CUBE_SIZE + CUBE_SIZE // 2
        start_y = start_pos[1] * CUBE_SIZE + CUBE_SIZE // 2
        end_x = end_pos[0] * CUBE_SIZE + CUBE_SIZE // 2
        end_y = end_pos[1] * CUBE_SIZE + CUBE_SIZE // 2
        return pygame.draw.line(self.screen, RED, (start_x, start_y), (end_x, end_y), LINE_WIDTH)

    # Ending text
    def write_ending_text(self, text:str):
        font = pygame.font.Font(None, 36)
        text = font.render(f"{text}", True, BLACK)
        space = font.render("Press Space to Restart", True, BLACK)
        self.screen.blit(text, (15, 15))
        self.screen.blit(space, (CUBE_SIZE + CUBE_SIZE // 12, WINDOW_SIZE // 1.05))

    # Checking for win or tie    
    def check_for_win(self):
        # Checking if win for rows
        for row in range(3):
            winning_row = 0
            for col in range(3):
                if self.game_array[row][col] == 1:
                    winning_row += 1
                elif self.game_array[row][col] == -1:
                    winning_row += -1

                if winning_row == 3:
                    self.write_ending_text("Dot wins!")
                    self.draw_winning_line((0, row),(2, row))
                    self.game_is_on = False
                    break
                elif winning_row == -3:
                    self.write_ending_text("Cross wins!")
                    self.draw_winning_line((0, row),(2, row))
                    self.game_is_on = False
                    break
        
        # Checking if win for cols
        for row in range(3):
            winning_col = 0
            for col in range(3):
                if self.game_array[col][row] == 1:
                    winning_col += 1
                elif self.game_array[col][row] == -1:
                    winning_col += -1

                if winning_col == 3:
                    self.write_ending_text("Dot wins!")
                    self.draw_winning_line((row, 0),(row, 2))
                    self.game_is_on = False
                    break
                elif winning_col == -3:
                    self.write_ending_text("Cross wins!")
                    self.draw_winning_line((row, 0),(row, 2))
                    self.game_is_on = False
                    break
        
        # Checking if win for axis
        if self.game_array[0][0] + self.game_array[1][1] + self.game_array[2][2] == 3:
            self.write_ending_text("Dot wins!")
            self.draw_winning_line((0, 0),(2, 2))
            self.game_is_on = False
        elif self.game_array[0][2] + self.game_array[1][1] + self.game_array[2][0] == 3:
            self.write_ending_text("Dot wins!")
            self.draw_winning_line((0, 2),(2, 0))
            self.game_is_on = False
        elif self.game_array[0][0] + self.game_array[1][1] + self.game_array[2][2] == -3:
            self.write_ending_text("Cross wins!")
            self.draw_winning_line((0, 0),(2, 2))
            self.game_is_on = False
        elif self.game_array[0][2] + self.game_array[1][1] + self.game_array[2][0] == -3:
            self.write_ending_text("Cross wins!")
            self.draw_winning_line((0, 2),(2, 0))
            self.game_is_on = False

        # Checking for a tie
        num_of_zeroes = 0
        for row in range(3):
            for col in range(3):
                if self.game_array[row][col] == 0:
                    num_of_zeroes += 1
        if num_of_zeroes == 0 and self.game_is_on:
            self.write_ending_text("It's a tie!")
            self.game_is_on = False



