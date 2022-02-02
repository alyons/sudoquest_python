from pygame import mixer
from pygame.event import Event, post
from pygame_roar.audio_manager import AudioManager
from pygame_roar.resource_manager import StaticResourceManager

from src.custom_events import AudioEventType

class SudoquestAudioManager(AudioManager):
    