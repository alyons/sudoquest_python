from pygame import K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_KP_1, K_KP_2, K_KP_3, K_KP_4, K_KP_5, K_KP_6, K_KP_7, K_KP_8, K_KP_9, Surface
from pygame.event import Event
from pygame.font import Font
from pygame_roar.drawable import Drawable
from pygame_roar.resource_manager import StaticResourceManager
from .sudoku import Sudoku

KEY_TO_NUMBER = {
    K_1: 1,
    K_2: 2,
    K_3: 3,
    K_4: 4,
    K_5: 5,
    K_6: 6,
    K_7: 7,
    K_8: 8,
    K_9: 9,
    K_KP_1: 1,
    K_KP_2: 2,
    K_KP_3: 3,
    K_KP_4: 4,
    K_KP_5: 5,
    K_KP_6: 6,
    K_KP_7: 7,
    K_KP_8: 8,
    K_KP_9: 9,
}

class Board():
    FONT: Font = None
    TILE: Surface = None

    def __init__(self: 'Board', puzzle: str):
        self.sudoku: Sudoku = Sudoku(puzzle) 
        if not Board.FONT: Board.FONT = StaticResourceManager.get_font('default')
        if not Board.TILE: Board.TILE = StaticResourceManager.get_image('sudoku_tile')
        self.surface: Surface = Surface((9 * Board.TILE.get_width(), 9 * Board.TILE.get_height()))
        self.selected_square: tuple[int, int] = None
        self.selector = Surface(Board.TILE.get_size())
        self.selector.fill('yellow')
        self.selector.fill((180, 180, 180), (4, 4, 24, 24))

    def draw_tile(self: 'Board', pos: tuple[int, int], number: int) -> None:
        draw_pos = (pos[0] * Board.TILE.get_width(), pos[1] * Board.TILE.get_height())
        self.surface.blit(Board.TILE, draw_pos)
        if self.selected_square == pos:
            self.surface.blit(self.selector, draw_pos)
        if number > 0:
            numImage = Board.FONT.render(f'{number}', True, 'black' if pos in self.sudoku.default_values else'blue')
            numSize = numImage.get_size()
            numPos = (draw_pos[0] + ((Board.TILE.get_width() - numSize[0]) / 2) + 1, draw_pos[1] + ((Board.TILE.get_height() - numSize[1]) / 2) + 1)
            self.surface.blit(numImage, numPos)
    
    def draw_board(self: 'Board') -> None:
        for k, v in self.sudoku.squares_visible.items():
            self.draw_tile(k, v)
    
    def draw(self: 'Board') -> None:
        self.draw_board()
    
    def submit_number(self: 'Board', value: int) -> bool:
        output = self.sudoku.submit_number(self.selected_square[1], self.selected_square[0], value)
        self.selected_square = None
        return output
