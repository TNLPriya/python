import pygame

pygame.init()
screen_size = (640,640)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Chess Board')

# Colors
white = (255,255,255)
brown = (153,76,0)

# Draw board
def draw_board():
    for row in range(8):
        for col in range(8):
            color = white if (row+col)%2==0 else brown
            pygame.draw.rect(screen, color, pygame.Rect(col*80, row*80, 80,80))

# Draw pieces
def draw_pieces(board):
    SQUARE_SIZE=80
    piece_images = {
        'p': pygame.transform.scale(pygame.image.load('pawn.png'), (SQUARE_SIZE,SQUARE_SIZE)),
        'r': pygame.transform.scale(pygame.image.load('rook.jpg'), (SQUARE_SIZE,SQUARE_SIZE)),
        'n': pygame.transform.scale(pygame.image.load('knight.png'), (SQUARE_SIZE,SQUARE_SIZE)),
        'b': pygame.transform.scale(pygame.image.load('bishop.png'), (SQUARE_SIZE,SQUARE_SIZE)),
        'q': pygame.transform.scale(pygame.image.load('queen.png'), (SQUARE_SIZE,SQUARE_SIZE)),
        'k': pygame.transform.scale(pygame.image.load('king.png'), (SQUARE_SIZE,SQUARE_SIZE))
    }
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != '.':
                screen.blit(piece_images[piece], pygame.Rect(col*80,row*80,80,80))

# Initial board state
board = [
    ['r','n','b','q','k','b','n','r'],
    ['p','p','p','p','p','p','p','p'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['p','p','p','p','p','p','p','p'],
    ['r','n','b','q','k','b','n','r']
]

draw_board()
draw_pieces(board)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
