# importing modules
import pygame
import sys
from constants import *
from board import *

# main function
def main():
    # initializing pygame
    pygame.init()
    
    # Setting the width and height of the screen
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    screen.fill(WHITE)
    pygame.display.set_caption("Tic Tac Toe")
    
    # initializing clock
    clock = pygame.time.Clock()

    # drawing board
    board = Board(screen)

    # Checking for events
    def check_for_events():
        global x_pos, y_pos, done
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                sys.exit()
            # Getting coordinates from the mouse   
            if event.type == pygame.MOUSEBUTTONDOWN:
                coordinates = pygame.mouse.get_pos()
                x_pos = coordinates[0] // CUBE_SIZE
                y_pos = coordinates[1] // CUBE_SIZE
                board.put_mark((y_pos, x_pos))
                board.check_for_win()
            # Setting space as a reset button only if game is over
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and board.game_is_on == False:
                main()

    # Main loop            
    done = False            
    while not done:

            check_for_events()
            pygame.display.flip()
            clock.tick(60)

    pygame.quit()

main()