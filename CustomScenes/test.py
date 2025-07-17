from Illusion.importer import Importer, Assets
from Illusion.scene import Scene


class Test(Scene):
    def __init__(self,importer: Importer, assets: Assets):
        super().__init__(importer, assets)
        self.fill_color = (255,255,255)
