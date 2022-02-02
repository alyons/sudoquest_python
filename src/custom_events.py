from enum import IntEnum
from pygame.event import custom_type

class AudioEventType(IntEnum):
    PLAY_BGM = custom_type()
    PLAY_SFX = custom_type()
    BGM_ENDED = custom_type()
    FADE_OUT_BGM = custom_type()