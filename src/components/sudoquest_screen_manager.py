from pygame.event import Event
from pygame_roar.screen_manager import ScreenManager, TransitionType

from src.custom_events import ScreenTransitionEvent
from src.screens.background_screen import BackgroundScreen
from src.screens.sudoku_screen import SudokuScreen


class SudoquestScreenManager(ScreenManager):
    def __init__(self: 'SudoquestScreenManager'):
        super().__init__()
        self.add_screen(BackgroundScreen())
        self.add_screen(SudokuScreen())
    
    def handle_events(self: 'ScreenManager', events: Event) -> None:
        for event in events:
            match event.type:
                case _: return # Do Nothing
