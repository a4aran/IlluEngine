import pygame.image

class AssetsManager:
    def __init__(self):
        self.audio_controller = self.AudioController()
        self.__importer = self.Importer()
        self.__assets = self.Assets()

    class Importer:
        def __init__(self):
            self.prefix = [
                '',  # image prefix
                '',  # animated sprite prefix
                ''   # sound prefix
            ]


        def import_img(self, path: str, result_size: tuple[int, int] | int):
            src_img = pygame.image.load(self.prefix[0] + path).convert_alpha()
            if isinstance(result_size, tuple):
                img = pygame.transform.scale(src_img, result_size)
            else:
                rs = (
                    src_img.get_width() * result_size,
                    src_img.get_height() * result_size
                )
                img = pygame.transform.scale(src_img, rs)
            return img

        def import_animated_sprite(self, path: str, frames_amount: int,
                                   result_frame_size: tuple[int, int] | float):
            src_img = pygame.image.load(self.prefix[1] + path).convert_alpha()

            if isinstance(result_frame_size, tuple):
                rfs = result_frame_size
                width = frames_amount * rfs[0]
                height = rfs[1]
            else:
                scale = result_frame_size
                rfs = (
                    int(src_img.get_width() / frames_amount * scale),
                    int(src_img.get_height() * scale)
                )
                width = frames_amount * rfs[0]
                height = rfs[1]

            img = pygame.transform.scale(src_img, (width, height))

            frames = []
            for f in range(frames_amount):
                frame = pygame.Surface(rfs, pygame.SRCALPHA)
                frame.blit(img, (0, 0), (f * rfs[0], 0, *rfs))
                frames.append(frame)

            return frames

        def import_sound(self, path: str):
            return pygame.mixer.Sound(self.prefix[2] + path)

# importing images

    def import_img(self,name: str,path: str, result_size: tuple[int, int] | int):
        self.__assets.add_sprite(name, self.__importer.import_img(path, result_size))

    def import_animated_img(self,name: str ,path: str, frames_amount: int,
                               result_frame_size: tuple[int, int] | float):
        self.__assets.add_animated_sprite(name, self.__importer.import_animated_sprite(path, frames_amount, result_frame_size))

# method from assets class I didn't want to delete
    def add_frame_to_animated_sprite(self,sprite_name: str,frame: pygame.Surface):
        self.__assets.add_frame_to_animated_sprite(sprite_name,frame)

# getting sprites from assets
    def get_sprite(self,name:str):
        self.__assets.get_sprite(name)

    def get_animated_sprite(self,name:str):
        self.__assets.get_sprite(name)

# prefix setting
    def set_importer_img_prefix(self, path_prefix: str):
        self.__importer.prefix[0] = path_prefix

    def set_importer_animated_sprite_prefix(self, path_prefix: str):
        self.__importer.prefix[1] = path_prefix

    def set_importer_sound_prefix(self, path_prefix: str):
        self.__importer.prefix[2] = path_prefix

# importing sound
    def import_sfx(self,name: str, path: str):
        self.audio_controller._add_sfx(name,self.__importer.import_sound(path))

    def import_music(self,name: str, path: str):
        self.audio_controller._add_music(name,path)

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

    class AudioController:
        def __init__(self):
            self._sfx = {}
            self._music = {}
            self._break_time = [0,False] # time between autoplaying the next song
            self._mute = [False,False]
            self._playlist = []
            self._playlist_cursor = 0
            self._random = False

        def _add_sfx(self,name: str,sfx: pygame.mixer.Sound):
            self._sfx[name] = sfx

        def _add_music(self,name: str,path: str):
            self._music[name] = path

        def set_break_time(self,length: float):
            self._break_time[0] = length

        def toggle_break_time(self):
            self._break_time = not self._break_time

        def toggle_mute_sfx(self):
            self._mute[0] = not self._mute[0]

        def toggle_mute_music(self):
            self._mute[1] = not self._mute[1]

        def generate_playlist(self):
            self._playlist = []
            for song in self._music:
                self._playlist.append(self._music[song])

        def toggle_random_playlist_order(self):
            self._random = not self._random

        def play_playlist(self):
            if pygame.mixer.music.get_busy(): return
            pygame.mixer.music.unload()
            self.__increase_playlist_cursor()
            pygame.mixer.music.load(self._playlist[self._playlist_cursor])

        def __increase_playlist_cursor(self):
            self._playlist_cursor += 1
            if len(self._playlist) - 1 <self._playlist_cursor:
                self._playlist_cursor = 0
