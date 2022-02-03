from enum import IntEnum
from pygame.event import custom_type


class AudioEventType(IntEnum):
    PLAY_BGM = custom_type()
    PLAY_SFX = custom_type()
    BGM_ENDED = custom_type()
    FADE_OUT_BGM = custom_type()


class ScreenTransitionEvent(IntEnum):
    MAIN_TO_ENDLESS = custom_type()
    MAIN_TO_OPTIONS = custom_type()
    OPTIONS_TO_MAIN = custom_type()
