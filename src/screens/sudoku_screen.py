import pygame
from pygame.event import Event
from pygame_roar.game_screen import GameScreen
from pygame_roar.input_manager import StaticInputManager
from src.game_components.battle.board import Board

KEY_TO_NUMBER = {
    pygame.K_1: 1,
    pygame.K_2: 2,
    pygame.K_3: 3,
    pygame.K_4: 4,
    pygame.K_5: 5,
    pygame.K_6: 6,
    pygame.K_7: 7,
    pygame.K_8: 8,
    pygame.K_9: 9,
    pygame.K_KP_1: 1,
    pygame.K_KP_2: 2,
    pygame.K_KP_3: 3,
    pygame.K_KP_4: 4,
    pygame.K_KP_5: 5,
    pygame.K_KP_6: 6,
    pygame.K_KP_7: 7,
    pygame.K_KP_8: 8,
    pygame.K_KP_9: 9,
}

class SudokuScreen(GameScreen):
    def __init__(self: 'SudokuScreen') -> None:
        super().__init__()
        self.board: Board = Board("001700509573024106800501002700295018009400305652800007465080071000159004908007053")
        self.board_offset: tuple[int, int] = (0, 0)
    
    def load_content(self: 'SudokuScreen') -> None:
        pass

    def update(self: 'SudokuScreen', time: int, is_transitioning: bool) -> None:
        if is_transitioning: return

        self.handle_events(StaticInputManager.get_raw_events())
    
    def draw(self: 'SudokuScreen') -> None:
        super().draw()
        self.screen.fill('aliceblue')
        self.board.draw()
        self.screen.blit(self.board.surface, self.board_offset)
    
    def mouse_clicking_square(self: 'SudokuScreen', pos: tuple[int, int]) -> tuple[int, int] | None:
        rel_pos = (pos[0] - self.board_offset[0], pos[1] - self.board_offset[1])
        tile_pos = (rel_pos[0] // Board.TILE.get_width(), rel_pos[1] // Board.TILE.get_height())
        if tile_pos[0] in range(0, 9) and tile_pos[1] in range(0, 9):
            return tile_pos
        return None

    def handle_events(self: 'SudokuScreen', events: list[Event]) -> None:
        for event in events:
            match event.type:
                case pygame.KEYDOWN:
                    if event.key in KEY_TO_NUMBER.keys() and self.board.selected_square:
                        self.board.submit_number(KEY_TO_NUMBER[event.key])
                case pygame.MOUSEBUTTONDOWN:
                    self.board.selected_square = self.mouse_clicking_square(pygame.mouse.get_pos())
                    return
                case _: return # Do Nothing
