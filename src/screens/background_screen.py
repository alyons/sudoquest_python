from pygame_roar.game_screen import GameScreen


class BackgroundScreen(GameScreen):
    def __init__(self: 'BackgroundScreen') -> None:
        super().__init__()
    
    def load_content(self: 'GameScreen') -> None:
        pass

    def update(self: 'GameScreen', time: int, is_transitioning: bool) -> None:
        if is_transitioning: return
    
    def draw(self: 'BackgroundScreen') -> None:
        super().draw()
        self.screen.fill((0, 0, 0))
