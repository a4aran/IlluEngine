import pygame
pygame.init()
pygame.mixer.init()
from frame_data_f import FrameData as Fd
import globals as g
from game_manager import GameManager

window = pygame.display.set_mode((g.WINDOW_WIDTH,g.WINDOW_HEIGHT))
game = GameManager()

clock = pygame.time.Clock()
game_on = True
frame_data = Fd()
while game_on:
    frame_data.dt = clock.tick(240) / 1000
    frame_data.reset_mbtn()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game_on = False
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                frame_data.mbtn_just_pressed[0] = True
            elif e.button == 2:
                frame_data.mbtn_just_pressed[1] = True
            elif e.button == 3:
                frame_data.mbtn_just_pressed[2] = True

    window.fill((255,255,255))

    frame_data.mouse_pos = pygame.mouse.get_pos()
    frame_data.mouse_buttons = pygame.mouse.get_pressed()

    game.update_and_draw(frame_data,window)

    pygame.display.flip()

pygame.quit()