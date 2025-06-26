import pygame
from enum import Enum

from frame_data_f import FrameData


class UI:
    def __init__(self,id):
        self.id = id
        self._hud = self._HUD()
        self._gui = self._GUI()
        self.data = {}

    class _HUD:
        def __init__(self):
            self.surface_s = []

        class Img:
            def __init__(self,center_pos: tuple[float,float],img: pygame.Surface):
                self.img = img.copy()
                self.pos = (center_pos[0] -self.img.get_width()/2,center_pos[1] -self.img.get_height()/2)

            def draw(self,surface: pygame.Surface):
                surface.blit(self.img,self.pos)

        class Animation:
            def __init__(self,name: str,center_pos: tuple[float,float],sprites: list,fps:int,play_amount:int = 0):
                self.name = name
                self.sprites = sprites.copy()
                self.c_pos = center_pos
                self.frame_time = [-0.05,1 / fps]
                self.current_frame = 0
                self.repetition_count = 0
                self.play_count = [play_amount,False]

            def update(self,frame_data: FrameData):
                if not self.play_count[1]:
                    self.frame_time[0] += frame_data.dt
                    if self.frame_time[1] < self.frame_time[0]:
                        self.current_frame += 1
                        if self.current_frame == len(self.sprites):
                            self.repetition_count += 1
                            self.current_frame = 0
                            if self.play_count[0] != 0:
                                if self.repetition_count == self.play_count[0]:
                                    self.play_count[1] = True
                                    self.current_frame = len(self.sprites) - 1
                        self.frame_time[0] = 0

            def draw(self,surface: pygame.Surface):
                r = self.sprites[self.current_frame].get_rect()
                r.center = self.c_pos
                surface.blit(self.sprites[self.current_frame],
                             r.topleft
                             )

            def is_done(self):
                return self.play_count[1]

        def add_img(self,img: pygame.Surface):
            self.surface_s.append(img)

        def draw(self, surface: pygame.Surface):
            for s in self.surface_s:
                s.draw(surface)

        def update(self,frame_data: FrameData):
            for surface in self.surface_s:
                if isinstance(surface,self.Animation):
                    surface.update(frame_data)

        def find_animation(self,name:str):
            i = None
            for index, a in enumerate(self.surface_s):
                if isinstance(a, self.Animation):
                    if a.name == name:
                        i = index
            if i is None:
                print("'"+name+"' animation not found")
                return
            return self.surface_s[i]

    class _GUI:
        def __init__(self):
            self.buttons = []
            self.data = {}
            self.__clear_data()

        def __clear_data(self):
            self.data = {
                "should_change_scene": False,
                "scene_to_change_to": 0
            }

        class Button:
            class State(Enum):
                DEFAULT = 0
                HOVERED = 1
                PRESSED = 2

            def __init__(self, identifier: str, center_pos: pygame.Vector2, rect_size: tuple[float,float], animated_sprite: list,
                         sound: list[pygame.mixer.Sound,pygame.mixer.Sound] = [None,None], delay:float = None, rendered_text: list = None):
                self.identifier = identifier
                self.rect = pygame.Rect((0,0),rect_size)
                self.rect.center = center_pos
                self.current_state = self.State.DEFAULT
                self.frames = animated_sprite
                self.sounds = sound
                self.delay = [0,delay,False]
                self.lag_frame = False
                self.text_surface = rendered_text.copy() if rendered_text is not None else None

                if self.text_surface is not  None:
                    txt_l = len(self.text_surface)
                    if txt_l < 3:
                        for n in range(3-txt_l):
                            self.text_surface.append(self.text_surface[0])

                print(self.text_surface)

            def update(self, frame_data: FrameData, data: dict):
                if not self.delay[2]:  # If delay not started, check for hover/click
                    self.current_state = self.State.DEFAULT
                    if self.rect.collidepoint(frame_data.mouse_pos):
                        if frame_data.mbtn_just_pressed[0]:
                            self.current_state = self.State.PRESSED
                            self.delay[2] = True  # Start the delay
                            self.lag_frame = True
                            if self.sounds[1] is not None and not self.lag_frame:
                                self.sounds[1].play()
                        else:
                            self.current_state = self.State.HOVERED
                else:
                    # Delay already started — maintain visual feedback and accumulate time
                    self.current_state = self.State.PRESSED
                    if self.delay[1] is not None:
                        self.delay[0] += frame_data.dt
                        if self.delay[0] > self.delay[1]:
                            self.on_click(data)
                            self.reset()
                    else:
                        self.on_click(data)
                        self.reset()
                if self.current_state == self.State.HOVERED:
                    frame_data.hovers = True
                self.lag_frame = False

            def reset(self):
                d = [
                    0,
                    self.delay[1],
                    False
                ]
                self.delay = d

            def on_click(self, data:dict):
                if self.sounds[0] is not None:
                    self.sounds[0].play()

            def draw(self,surface: pygame.Surface):
                surface.blit(self.frames[self.current_state.value],self.rect.topleft)
                if self.text_surface is not None:
                    dest_ = (
                        self.rect.center[0] - self.text_surface[self.current_state.value].get_width()/2,
                        self.rect.center[1] - self.text_surface[self.current_state.value].get_height()/2
                    )
                    surface.blit(self.text_surface[self.current_state.value],dest_)

        class ChangeScButton(Button):
            def __init__(self, identifier: str, center_pos: pygame.Vector2, rect_size: tuple[float, float],
                         animated_sprite: list, scene_to_change_to: int, sound: pygame.mixer.Sound = None, delay=None):
                super().__init__(identifier, center_pos, rect_size, animated_sprite, sound, delay)
                self.scene = scene_to_change_to

            def on_click(self, data:dict):
                super().on_click(data)
                if not data["should_change_scene"]:
                    data["should_change_scene"] = True
                    data["scene_to_change_to"] = self.scene

        def update(self,frame_data: FrameData):
            for button in self.buttons:
                button.update(frame_data,self.data)

        def draw(self,surface: pygame.Surface):
            for button in self.buttons:
                button.draw(surface)

    def new_test_button(self, identifier: str, center_pos: pygame.Vector2,size: tuple[float,float],sprites: list,sound: pygame.mixer.Sound = [None,None],delay: float = None,rendered_text: list = None):
        self._gui.buttons.append(
            self._gui.Button(
                identifier,
                center_pos,
                size,
                sprites,
                sound,
                delay,
                rendered_text
            )
        )

    def new_scene_change_button(self,identifier: str, center_pos: pygame.Vector2,size: tuple[float,float],sprites: list,scene_to_change_to,sound: pygame.mixer.Sound = [None,None],delay: float = None,rendered_text: list = None):
        self._gui.buttons.append(
            self._gui.ChangeScButton(
                identifier,
                center_pos,
                size,
                sprites,
                scene_to_change_to,
                sound,
                delay
            )
        )

    def new_img(self,img: pygame.Surface,center_pos: pygame.Vector2):
        self._hud.surface_s.append(
            self._hud.Img(
                center_pos, img
            )
        )

    def new_animation(self,name:str,sprites: list,center_pos: pygame.Vector2,fps:int,play_count: int = 0):
        self._hud.surface_s.append(
            self._hud.Animation(
                name,
                center_pos,
                sprites,
                fps,
                play_count
            )
        )

    def get_animation(self,name:str):
        return  self._hud.find_animation(name)

    def update(self,frame_data: FrameData):
        self._hud.update(frame_data)
        self._gui.update(frame_data)

    def draw(self,surface: pygame.Surface):
        self._hud.draw(surface)
        self._gui.draw(surface)
