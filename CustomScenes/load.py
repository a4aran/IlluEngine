from Illusion.frame_data_f import FrameData
from Illusion.importer import Importer, Assets
import Illusion.globals as g
from Illusion.scene import Scene


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