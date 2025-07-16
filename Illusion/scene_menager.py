import pygame

import globals as g
from Illusion.scene import Scene
from frame_data_f import FrameData


class SceneManager:
    def __init__(self):
        self.__scenes = []
        self.__active_scene = g.SC_LOAD
        self.__sc_data = {}

    def update_and_draw(self,frame_data: FrameData,surface: pygame.Surface):
        self.__get_data_from_scene()
        if self.__sc_data["should_change_scene"]:
            self.__change_scene(self.__sc_data["should_change_scene"])
        self.__scenes[self.__active_scene].update_and_draw(frame_data,surface)

    def __get_data_from_scene(self):
        self.__sc_data = self.__scenes[self.__active_scene].data

    def __change_scene(self,scene_id: int):
        self.__scenes[self.__active_scene].on_changed_from()
        self.__active_scene = scene_id
        self.__scenes[self.__active_scene].on_changed_to()

    def add_scene(self,scene: Scene):
        self.__scenes.append(scene)

