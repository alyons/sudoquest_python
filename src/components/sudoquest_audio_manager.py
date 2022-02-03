from pygame import mixer
from pygame.event import Event, post
from pygame_roar.audio_manager import AudioManager
from pygame_roar.resource_manager import StaticResourceManager

from src.custom_events import AudioEventType


def play_background_music(id: str, loops: int = -1):
    post(Event(AudioEventType.PLAY_BGM, { 'id': id, 'loops': loops }))


def play_sound_effect(id: str):
    post(Event(AudioEventType.PLAY_SFX, { 'id': id }))


class SudoquestAudioManager(AudioManager):
    def __init__(self: 'SudoquestAudioManager') -> None:
        super().__init__()
        self.active_bgm: str = ''
        mixer.set_reserved(0)
        self.bgm_channel = mixer.Channel(0)
    
    def handle_events(self, events: list[Event]) -> None:
        for event in events:
            match event.type:
                case AudioEventType.PLAY_SFX:
                    mixer.find_channel().play(StaticResourceManager.get_sound(event.id))
                    return
                case AudioEventType.PLAY_BGM:
                    if self.active_bgm != event.id:
                        self.active_bgm = event.id
                        if self.bgm_channel.get_busy():
                            self.bgm_channel.set_endevent(AudioEventType.BGM_ENDED)
                            self.bgm_channel.fadeout(250)
                        else:
                            self.bgm_channel.play(StaticResourceManager.get_sound(self.active_bgm), loops=event.loops)
                    return
                case AudioEventType.FADE_OUT_BGM:
                    if self.bgm_channel.get_busy():
                        self.bgm_channel.fadeout(250)
                    return
                case AudioEventType.BGM_ENDED:
                    if self.active_bgm:
                        self.bgm_channel.play(StaticResourceManager.get_sound(self.active_bgm))
                    return
