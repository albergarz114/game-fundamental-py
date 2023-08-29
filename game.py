import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


player = pygame.Rect((300, 20, 50, 50))

run = True
while run:
    
    screen.fill((0,0,0))    ##BLACK
    pygame.draw.rect(screen, (255, 0, 0), player)  #RBG: RED


    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:     #PRESS button a: SQUARE GOES left
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:   #PRESS button d: SQUARE GOES right
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:   #PRESS button w: SQUARE GOES up
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:   #PRESS button s: SQUARE GOES down
        player.move_ip(0, 1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()

