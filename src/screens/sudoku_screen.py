from pygame_roar.game_screen import GameScreen
from src.game_components.battle.sudoku import Sudoku

class SudokuScreen(GameScreen):
    def __init__(self: 'SudokuScreen') -> None:
        super().__init__()
        self.sudoku: Sudoku = Sudoku("001700509573024106800501002700295018009400305652800007465080071000159004908007053")
    
    def load_content(self: 'GameScreen') -> None:
        pass

    def update(self: 'GameScreen', time: int, is_transitioning: bool) -> None:
        if is_transitioning: return
    
    def draw(self: 'SudokuScreen') -> None:
        super().draw()
        self.screen.fill('aliceblue')
        self.sudoku.draw(self.screen)

