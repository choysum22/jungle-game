# import library
import pygame, sys

# define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WINDOW_HEIGHT = 900
WINDOW_WIDTH = 700


def main() -> None:
    # main game loop

    # set pygame environment
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    pygame.display.set_caption("The Jungle Game")
    SCREEN.fill(WHITE)

    # game loop/ restart point
    while True:
        drawBoard()

        # game logic goes here

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def drawBoard() -> None:
    # draw the grid of the board
    gridSize = 100
    for x in range(0, WINDOW_WIDTH, gridSize):
        for y in range(0, WINDOW_HEIGHT, gridSize):
            rect = pygame.Rect(x, y, gridSize, gridSize)
            pygame.draw.rect(SCREEN, RED, rect, 2)
    # draw special tiles
    # draw the pieces on the board


def selectPiece() -> None:
    # handles selection of pieces
    pass


def deselectPiece() -> None:
    # handles deselection of pieces
    pass


def movePiece() -> None:
    # handles movement of pieces
    pass


def isAboutToWin() -> bool:
    # return true if a player is about to win on next move
    pass


# game variables
# selected is a number representing where the selected piece is
# moves is a list of where the selected piece can move
# captures is a list of where the selected piece can capture
# game_board is a list of every space on the board and says what piece exists there
# turn is a number either 1 or 2 representing whose turn it is
turn = 1
selected = None
moves = []
captures = []
red_captured = []
blue_captured = []
game_board = []


# load graphics of the game (pieces, board, special tiles, etc...)

# run the game
main()
