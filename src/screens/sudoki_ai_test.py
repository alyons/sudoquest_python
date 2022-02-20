import pygame
from pygame import Surface
from pygame.event import Event
from pygame.font import Font
from pygame_roar.game_screen import GameScreen
from pygame_roar.input_manager import StaticInputManager
from src.game_components.battle.sudoku import Sudoku

class SAITestScreen(GameScreen):
    def __init__(self: 'GameScreen'):
        super().__init__()
        self.sudoku: Sudoku = Sudoku("001700509573024106800501002700295018009400305652800007465080071000159004908007053")

    def load_content(self: 'GameScreen') -> None:
        self.number_font: Font
    
    def update(self: 'GameScreen', time: int, is_transitioning: bool):
        # return super().update(time, is_transitioning)
        if is_transitioning: return
    
    def draw_square(self) -> None:
        pass

    def draw_sudoku(self) -> None:
        pass

    def draw(self) -> None:
        super().draw()
        self.screen.fill('azure1')
        self.draw_sudoku()