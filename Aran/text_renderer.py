import pygame.font

font_prefix = "../assets/fonts/"

class TextRenderer:
    def __init__(self, font_name: str):
        self.font_path = font_prefix + font_name
        self.fonts_by_size = {}  # Cache: size -> pygame.Font

    def get_font(self, size: int) -> pygame.font.Font:
        """Return a font object of the specified size, caching it if needed."""
        if size not in self.fonts_by_size:
            self.fonts_by_size[size] = pygame.font.Font(self.font_path, size)
        return self.fonts_by_size[size]

    def render(self, text: str, size: int = 24, color: tuple = (0, 0, 0), antialias: bool = True) -> pygame.Surface:
        """Render text to a surface with the given size and color."""
        font = self.get_font(size)
        return font.render(text, antialias, color)