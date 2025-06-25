import pygame

from Illusion import ui
from Illusion.frame_data_f import FrameData
import globals as g
from Illusion.importer import Importer, Assets


class Scene:
    def __init__(self,importer: Importer,assets: Assets):
        self._objs = []
        self._uis = [ui.UI("default")]
        self.data = {}
        self.__clear_data()
        self.fill_color = (0,0,0)

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

    def __ui_index_from_id(self, id: str):
        for i, ui_o in enumerate(self._uis):
            if ui_o.id == id:
                return i
        return -1

class MainMenuSc(Scene):
    def __init__(self,importer: Importer, assets: Assets):
        super().__init__(importer, assets)
        self.fill_color = (255,255,255)

class LoadSc(Scene):
    def __init__(self, importer: Importer, assets: Assets):
        super().__init__(importer, assets)
        self._uis[0].new_animation("logo",importer.get_animated_sprite("logo"),(g.WINDOW_WIDTH / 2, g.WINDOW_HEIGHT / 2),10,1)
        importer.get_sound("logo_sound").play()
        self.anim_cooldown = 0
        self.fill_color = (0,80,90)

    def _update(self, frame_data: FrameData):
        if self._uis[0].get_animation("logo").is_done():
            self.anim_cooldown += frame_data.dt
        if self.anim_cooldown >= 0.75:
            self.edit_change_scene_data(True,g.SC_MAIN_MENU)
        super()._update(frame_data)