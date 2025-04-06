import pygame
import sys
from random import choice

pygame.init()

class TetrisApp:
    BOARD_WIDTH = 10
    BOARD_HEIGHT = 20
    TILE_SIZE= 30

    COLORS = [
        (255,0,0),(0,0,255) ,
        ( 0,255,0),
        ( 255, 255, 0),
        (255, 152, 22),
        (145, 19, 251),
        (251, 77, 186),
        (0, 0, 0)
    ]

    SHAPES =[
    [[1,1,1,1]],#I
    [[1,1,1], #T
     [0,1,0]],
    [[0,1,0],   # S
     [1,1,0]],
    [[1,1,0], #Z
    [0,1,1]],
    [[1,1],
     [1,1]], # O
    [[1,1,1],
     [1,0,0]], # L
    [[1,1,1],
     [0,0,1]] #J
    ]









    def __init__(self):
        self.width = TetrisApp.BOARD_WIDTH * TetrisApp.TILE_SIZE
        self.height =TetrisApp.BOARD_HEIGHT* TetrisApp.TILE_SIZE
        self.screen = pygame.display.set_mode((self.width,self.height))


        self.clock= pygame.time.Clock()
        self.board = [[0] * TetrisApp.BOARD_WIDTH for _ in range( TetrisApp.BOARD_HEIGHT)]
        self.current_piece=None
        self.current_piece_color =None
        self.current_piece_x=None
        self.current_piece_y=None
        self.game_over = False

        self.drop_time= 0
        self.drop_speed= 500 #0.5 second

        self.new_piece()

    def rotate(self):
        rotated = [list(row) for row in zip(*reversed(self.current_piece))]
        if not self.check_collision(self.current_piece_x, self.current_piece_y,rotated):
            self.current_piece = rotated


    def draw_tile(self,x,y,color):
        rect = pygame.Rect(
        x * TetrisApp.TILE_SIZE,
        y * TetrisApp.TILE_SIZE,
        TetrisApp.TILE_SIZE,
        TetrisApp.TILE_SIZE)

        pygame.draw.rect(self.screen, color ,rect)
        pygame.draw.rect(self.screen,(128,128,128),rect,1)

    def draw(self):
        self.screen.fill((0, 216,166))

        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell ==1:
                    self.draw_tile(
                        x+ self.current_piece_x,
                        y+ self.current_piece_y,
                        self.current_piece_color

                    )


        pygame.display.flip()

        pygame.draw.rect(
            self.screen,
            (0,0,255),
            (0,150,30,30)
        )
    def new_piece(self):
        self.current_piece = choice(TetrisApp. SHAPES)
        self.current_piece_color = choice(TetrisApp.COLORS)
        self.current_piece_x= 0
        self.current_piece_y = 0


    def move(self,dx, dy):
        """Move the current piece if possible """
        if not self.check_collision(self.current_piece_x + dx, self.current_piece_y + dy, self.current_piece):
            self.current_piece_x += dx
            self.current_piece_y +=  dy

        if not self.check_collision(dx,dy,self.current_piece):
            self.current_piece_x += dx
            self.current_piece_y += dy
            return True
        return False

    def check_collision(self, px, py, piece):
        """Check if the piece collides with the board boundaries or other pieces."""
        for y, row in enumerate(piece):
            for x, cell in enumerate(row):
                try:
                    # Check if the cell is filled and if it's outside boundaries or colliding
                    if cell and (
                            py + y >= TetrisApp.BOARD_HEIGHT or  # Bottom boundary
                            px + x < 0 or  # Left boundary
                            px + x >= TetrisApp.BOARD_WIDTH or  # Right boundary
                            self.board[py + y][px + x]  # Collision with existing blocks
                    ):
                        return True
                except IndexError:
                    return True
        return False

    def handle_events(self):
        # 이벤트 처리 (특히 창 닫기)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print ("Left arrow key pressed")
                    self.move(-1,0)
                elif event.key == pygame.K_RIGHT:
                    print ("Right arrow key pressed")
                    self.move(1,0)
                elif event.key == pygame.K_DOWN:
                    print ("Down arrow key pressed")
                    self.move(0, 1)
                elif event.key == pygame.K_UP:
                    print("Up arrow key pressed")
                    self.rotate()
                elif event.key == pygame.K_SPACE:
                    print ("Space key pressed")

    def run(self):
        while not self.game_over:
            pygame.draw.rect(self.screen, (0,0,255 ),(0,0,100,50))
            self.handle_events()
            self.draw()
            self.clock.tick(60)
def main():
    app= TetrisApp()
    app.run()

if __name__ == "__main__":
    main()


t_shape = [
    [1, 1, 1],  # T
     [0, 1, 0]]

