import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Polygon Transformations")


n = 3  
radius = 150
default_center = [300, 300]
center = default_center.copy()
angle_offset = 0
scale_x = 1.0
scale_y = 1.0
flip_x = False
flip_y = False
shear = [0, 0]
shift = [0, 0]

clock = pygame.time.Clock()

def get_polygon_points():
    points = []
    for i in range(n):
        angle = 2 * math.pi * i / n - math.pi / 2 + math.radians(angle_offset)
        x = math.cos(angle) * radius * scale_x
        y = math.sin(angle) * radius * scale_y
      
        x += y * shear[0]
        y += x * shear[1]
      
        if flip_x:
            y *= -1
        if flip_y:
            x *= -1
      
        x += center[0] + shift[0]
        y += center[1] + shift[1]
        points.append((x, y))
    return points

run = True
while run:
    clock.tick(60)
    win.fill((255, 255, 0)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
           
            center = default_center.copy()
            scale_x = 1.0
            scale_y = 1.0
            angle_offset = 0
            flip_x = False
            flip_y = False
            shear = [0, 0]
            shift = [0, 0]

            if event.key == pygame.K_1:
                scale_x = 0.5
                scale_y = 0.5
            elif event.key == pygame.K_2:
                angle_offset = 45
            elif event.key == pygame.K_3:
                flip_x = True
                scale_y = 1.5  
            elif event.key == pygame.K_4:
                shear = [0.5, 0]
                center = default_center.copy()
            elif event.key == pygame.K_5:
                scale_y = 0.5
                center[1] = 200
            elif event.key == pygame.K_6:
                angle_offset = -45  
                shear = [0.5, 0]
            elif event.key == pygame.K_7:
                flip_x = True
                flip_y = True
            elif event.key == pygame.K_8:
                angle_offset = 45
                center = [100, 500] 
                scale_y = 0.7
            elif event.key == pygame.K_9:
                angle_offset = 180
                shear = [0.5, 0]
                center = [400, 300]  
    points = get_polygon_points()
    pygame.draw.polygon(win, (0, 0, 255), points)

    pygame.display.update()

pygame.quit()
