from Illusion.importer import Importer, Assets
import Illusion.globals as g
from Illusion.scene import Scene


class Test(Scene):
    def __init__(self,importer: Importer, assets: Assets):
        super().__init__(importer, assets)
        self.fill_color = (255,255,255)
        self._uis[0].new_test_button("btn",(g.WINDOW_WIDTH / 2, g.WINDOW_HEIGHT / 2),(100,100),importer.get_animated_sprite("logo"))
