import pygame
import sys

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("War3")

BLUE = (0, 0, 255)
win.fill((255, 255, 255)) 

center_x = 300
center_y = 300
rect_width = 200
rect_height = 100
gap = 80  
triangle_base = 100
triangle_height = 80

rect_x = center_x - rect_width // 2
rect_y = center_y - rect_height // 2

pygame.draw.rect(win, BLUE, (rect_x, rect_y, rect_width, rect_height))

top_triangle = [
    (center_x, rect_y - gap + triangle_height),  
    (center_x - triangle_base // 2, rect_y - gap),
    (center_x + triangle_base // 2, rect_y - gap)
]
pygame.draw.polygon(win, BLUE, top_triangle)

bottom_triangle = [
    (center_x, rect_y + rect_height + gap - triangle_height), 
    (center_x - triangle_base // 2, rect_y + rect_height + gap),
    (center_x + triangle_base // 2, rect_y + rect_height + gap)
]
pygame.draw.polygon(win, BLUE, bottom_triangle)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
