from pygame_roar.game import Game
from pygame_roar.config_manager import ConfigManager

from src.components.sudoquest_audio_manager import SudoquestAudioManager, play_background_music
from src.components.sudoquest_screen_manager import SudoquestScreenManager


class SudoquestGame(Game):
    def __init__(self: 'Game'):
        super().__init__()
    
    def init_audio_manager(self: 'Game') -> None:
        self.audio_manager = SudoquestAudioManager()
    
    def init_config_manager(self: 'Game') -> None:
        self.config_manager = ConfigManager()
        self.config_manager.app_name = 'Sudoquest'
        self.config_manager.author = 'Platinum Leo, LLC'
    
    def init_screen_manager(self: 'Game') -> None:
        self.screen_manager = SudoquestScreenManager()
    
    def init(self: Game):
        super().init()
