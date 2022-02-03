from pygame import Surface
from pygame.font import Font
from pygame_roar.drawable import Drawable
from pygame_roar.config_manager import StaticConfigManager
from pygame_roar.resource_manager import StaticResourceManager

class Sudoku(Drawable):
    FONT: Font = None
    TILE: Surface = None
    def __init__(self: 'Sudoku', puzzle: str):
        self.base: str = puzzle
        self.surface: Surface = Surface(StaticConfigManager.game_size())
        self.squares_visible: dict[tuple[int, int], int] = {(i // 9, i % 9):int(v) for i, v in enumerate(self.base)}
        self.squares_solved: dict[tuple[int, int], int] = {(i // 9, i % 9):int(v) for i, v in enumerate(self.base)}
        # run logic here to solve the puzzle
        if not Sudoku.FONT: Sudoku.FONT = StaticResourceManager.get_font('default')
        if not Sudoku.TILE: Sudoku.TILE = StaticResourceManager.get_image('sudoku_tile')

    def draw_square(self: 'Sudoku', screen: Surface, pos, number):
        screen.blit(Sudoku.TILE, pos)
        if number > 0:
            numImage = Sudoku.FONT.render(f'{number}', True, (0, 0, 0))
            numSize = numImage.get_size()
            numPos = (pos[0] + ((Sudoku.TILE.get_width() - numSize[0]) / 2) + 1, pos[1] + ((Sudoku.TILE.get_height() - numSize[1]) / 2) + 1)
            screen.blit(numImage, numPos)
    
    def draw_board(self: 'Sudoku', screen: Surface):
        for k, v in self.squares_visible.items():
            pos = (k[0] * Sudoku.TILE.get_width(), k[1] * Sudoku.TILE.get_height())
            self.draw_square(screen, pos, v)

    def draw(self: 'Sudoku', screen: Surface):
        # image = Sudoku.FONT.render(self.base, True, (0, 0, 0))
        # screen.blit(image, (8, 8))
        self.draw_board(screen)
