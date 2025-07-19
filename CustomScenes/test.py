from Illusion.frame_data_f import FrameData
from Illusion.importer import Importer, Assets, MusicManager
from Illusion.scene import Scene


class Test(Scene):
    def __init__(self,importer: Importer, assets: Assets,music_manager: MusicManager):
        super().__init__(importer, assets,music_manager)
        self.fill_color = (255,255,255)
    #     self.timer = [0,False]
    #
    # def _update(self, frame_data: FrameData):
    #     self.timer[0] += frame_data.dt
    #     if not self.timer[1] and self.timer[0] > 10:
    #         self.timer[1] = True
    #         self._music_manager.play_track("rumbling")
    #     super()._update(frame_data)
    #
    # def on_changed_to(self):
    #     self._music_manager.play_track("go_slowed_down")