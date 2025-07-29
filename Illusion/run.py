import pygame

pygame.init()
hws = True
try:
    pygame.mixer.init()
except:
    hws = False
    print("No audio hardware found.")
import window_size
from game import Game

from frame_data_f import FrameData as Fd

window = pygame.display.set_mode((window_size.width,window_size.height))
game_o = Game(hws)

clock = pygame.time.Clock()
game_on = True
frame_data = Fd()
while game_on:
    frame_data.dt = clock.tick(240) / 1000
    frame_data.reset_mbtn()
    frame_data.hovers = False

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

    game_o.update_and_draw(frame_data, window)

    if frame_data.hovers:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    pygame.display.flip()

pygame.quit()