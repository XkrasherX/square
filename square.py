import pygame
import sys


pygame.init()

screen_width, screen_height = 800, 600

screen = pygame.display.set_mode((screen_width, screen_height))

white = (255, 255, 255)
black = (0, 0, 0)
gray = (150, 150, 150)

rect_width, rect_height = 50, 30

rect_x, rect_y = (screen_width - rect_width) // 2, (screen_height - rect_height) // 2

speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    rect_x += (keys[pygame.K_d] - keys[pygame.K_a]) * speed
    rect_y += (keys[pygame.K_s] - keys[pygame.K_w]) * speed
    screen.fill(white)
    
#прямоугольник
    pygame.draw.rect(screen, gray, (rect_x, rect_y, rect_width, rect_height))

 #тень
    pygame.draw.polygon(screen, black, [(rect_x, rect_y + rect_height),
                                        (rect_x + 10, rect_y + rect_height + 10),
                                        (rect_x + rect_width + 10, rect_y + rect_height + 10),
                                        (rect_x + rect_width, rect_y + rect_height)])
    pygame.display.flip()
    pygame.time.Clock().tick(60)
