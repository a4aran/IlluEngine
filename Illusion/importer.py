import pygame.image

class Importer:
    def __init__(self):
        self.__sprites = {}
        self.__animated_sprites = {}
        self.__sounds = {}

        self.__prefix = [
            '',  # image prefix
            '',  # animated sprite prefix
            ''   # sound prefix
        ]

    def import_img(self, name: str, path: str, result_size: tuple[int, int]):
        src_img = pygame.image.load(self.__prefix[0] + path).convert_alpha()
        img = pygame.transform.scale(src_img, result_size)
        self.__sprites[name] = img

    def import_animated_sprite(self, name: str, path: str, frames_amount: int, result_frame_size: tuple[int, int]):
        width = frames_amount * result_frame_size[0]
        src_img = pygame.image.load(self.__prefix[1] + path).convert_alpha()
        img = pygame.transform.scale(src_img, (width, result_frame_size[1]))

        frames = []
        for f in range(frames_amount):
            frame = pygame.Surface(result_frame_size, pygame.SRCALPHA)
            frame.blit(img, (0, 0), (f * result_frame_size[0], 0, *result_frame_size))
            frames.append(frame)

        self.__animated_sprites[name] = frames

    def import_sound(self, name: str, path: str):
        self.__sounds[name] = pygame.mixer.Sound(self.__prefix[2] + path)

    def get_sprite(self, name: str):
        return self.__sprites[name]

    def get_animated_sprite(self, name: str):
        return self.__animated_sprites[name]

    def get_sound(self, name: str):
        return self.__sounds[name]

    def set_img_prefix(self, path_prefix: str):
        self.__prefix[0] = path_prefix

    def set_animated_sprite_prefix(self, path_prefix: str):
        self.__prefix[1] = path_prefix

    def set_sound_prefix(self, path_prefix: str):
        self.__prefix[2] = path_prefix

class Assets:
    def __init__(self):
        self.__sprites = {}
        self.__animated_sprites = {}

    def add_sprite(self,name: str,sprite: pygame.Surface):
        self.__sprites[name] = sprite

    def add_animated_sprite(self,name:str,sprites: list):
        self.__animated_sprites[name] = sprites

    def add_frame_to_animated_sprite(self,sprite_name: str,frame: pygame.Surface):
        if sprite_name in self.__animated_sprites:
            self.__animated_sprites[sprite_name].append(frame)
        else:
            print("Assets: Can't add " + str(frame) + ", '" + sprite_name + "' doesn't exist")

    def get_sprite(self,name:str):
        return self.__sprites[name]

    def get_animated_sprites(self,name:str):
        return self.__animated_sprites[name]