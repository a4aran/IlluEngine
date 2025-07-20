import pygame

from Illusion import ui
from Illusion.frame_data_f import FrameData
from go import GlobalObjects
from Illusion.importer import Importer, Assets, MusicManager


class Scene:
    def __init__(self,importer: Importer,assets: Assets,music_manager: MusicManager,global_objects: GlobalObjects):
        self._objs = []
        self._uis = {}
        self.create_ui("default")
        self.data = {}
        self.__clear_data()
        self.fill_color = (0,0,0)
        self._music_manager = music_manager

    def _update(self, frame_data: FrameData):
        self.get_data_from_uis()
        for o in self._objs:
            o.update(frame_data)
        for ui in self._uis:
            self.get_ui(ui).update(frame_data)

    def __draw(self,surface: pygame.Surface):
        for o in self._objs:
            o.draw(surface)
        for ui in self._uis:
            self.get_ui(ui).draw(surface)

    def update_and_draw(self,frame_data: FrameData,surface: pygame.Surface):
        surface.fill(self.fill_color)
        self._update(frame_data)
        self.__draw(surface)

    def on_changed_from(self):
        self.__clear_data()

    def on_changed_to(self,previous_scene_id):
        pass

    def __clear_data(self):
        self.data["should_change_scene"] = False
        self.data["scene_to_change_to"] = 0

    def edit_change_scene_data(self,should_change:bool,scene_to_change_to:int):
        self.data["should_change_scene"] = should_change
        self.data["scene_to_change_to"] = scene_to_change_to

    def get_data_from_uis(self):
        for ui in self._uis:
            if self.get_ui(ui).data()["should_change_scene"]:
                self.edit_change_scene_data(self.get_ui(ui).data()["should_change_scene"],self.get_ui(ui).data()["scene_to_change_to"])
                self.get_ui(ui).reset_data()
                return

    def create_ui(self,ui_name):
        self._uis[ui_name] = ui.UI(ui_name)

    def get_ui(self,ui_name) -> ui.UI:
        if ui_name in self._uis: return self._uis[ui_name]
        return print("Ui " + ui_name + " not found")

    def delete_ui(self,ui_name: str):
        if ui_name in self._uis:
            self._uis.pop(ui_name)
            return
        print("Ui " + ui_name + " not found")

    def add_ui(self,ui: ui.UI):
        self._uis[ui.id] = ui