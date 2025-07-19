import pygame

from Illusion.importer import MusicManager
from importer import Importer, Assets
from frame_data_f import FrameData
from scene_manager import SceneManager


class GameManagerPreset:
    def __init__(self):
        self._scene_manager = SceneManager()
        self._importer = Importer()
        self._assets = Assets()
        self._music_manager = MusicManager()

        self._importer.set_img_prefix("../assets/textures")
        self._importer.set_animated_sprite_prefix("../assets/textures/animated/")
        self._importer.set_sound_prefix("../assets/sounds/effects/")
        self._music_manager.set_path_prefix("../assets/sounds/music/")

    def update_and_draw(self,frame_data: FrameData,surface: pygame.Surface):
        self._scene_manager.update_and_draw(frame_data,surface)