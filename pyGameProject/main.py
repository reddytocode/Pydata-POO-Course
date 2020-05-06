import pygame
import Colors
from Invader import Invader

pygame.init()
window_width = 800
window_height = 600
window_size = (window_width, window_height)
main_window = pygame.display.set_mode(window_size)

pygame.display.set_caption("Project")

x = 200
y = 200

width = 20
height = 20

vel = 10

running_game = True

inv_1 = Invader(20, 30)

while running_game:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
            break
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += vel

    if keys[pygame.K_UP] and y > 0:
        y -= vel

    if keys[pygame.K_DOWN] and y < 500 - height:
        y += vel

    inv_1.draw(main_window)
    inv_1.move_in_y(main_window)

    pygame.draw.rect(main_window, Colors.red, (x, y, width, height))

    pygame.display.update()

pygame.quit()