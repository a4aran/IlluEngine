from CustomScenes.load import LoadSc
from CustomScenes.test import Test
from Illusion.game_manager import GameManagerPreset


class Game(GameManagerPreset):
    def __init__(self):
        super().__init__()
        self._importer.import_animated_sprite("logo","logo.png",13,(64,192))

        self._importer.import_sound("successful_select","effects/select_successful.wav")
        self._importer.import_sound("denied","effects/select_denied.wav")

        self._importer.import_sound("logo_sound","music/logo_sound.wav")

        self._scene_manager.add_scene(LoadSc(self._importer,self._assets))
        self._scene_manager.add_scene(Test(self._importer, self._assets))

