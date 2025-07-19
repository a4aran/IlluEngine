import pygame

from Illusion import ui
from Illusion.frame_data_f import FrameData
from Illusion.importer import Importer, Assets, MusicManager


class Scene:
    def __init__(self,importer: Importer,assets: Assets,music_manager: MusicManager):
        self._objs = []
        self._uis = [ui.UI("default")]
        self.data = {}
        self.__clear_data()
        self.fill_color = (0,0,0)
        self._music_manager = music_manager

    def _update(self, frame_data: FrameData):
        for o in self._objs:
            o.update(frame_data)
        for ui in self._uis:
            ui.update(frame_data)

    def __draw(self,surface: pygame.Surface):
        for o in self._objs:
            o.draw(surface)
        for ui in self._uis:
            ui.draw(surface)

    def update_and_draw(self,frame_data: FrameData,surface: pygame.Surface):
        surface.fill(self.fill_color)
        self._update(frame_data)
        self.__draw(surface)

    def on_changed_from(self):
        pass

    def on_changed_to(self):
        pass

    def __clear_data(self):
        self.data = {
            "should_change_scene": False,
            "scene_to_change_to": 0
        }

    def edit_change_scene_data(self,should_change:bool,scene_to_change_to:int):
        self.data["should_change_scene"] = should_change
        self.data["scene_to_change_to"] = scene_to_change_to

    def _ui_index_from_id(self, id: str):
        for i, ui_o in enumerate(self._uis):
            if ui_o.id == id:
                return i
        return -1

    def create_ui(self,identifier: str):
        self._uis.append(ui.UI(identifier))