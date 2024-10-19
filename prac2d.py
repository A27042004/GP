import pygame
pygame.init()
pygame.display.set_caption(u'Keyboard events')
pygame.display.set_mode((400,400))
while True:
    event=pygame.event.wait()
    if event.type==pygame.QUIT:
        break
    if event.type in (pygame.KEYDOWN,pygame.KEYUP):
        key_name=pygame.key.name(event.key)
        key_name=key_name.upper()
        if event.type==pygame.KEYDOWN:
            print(u'"{}"key pressed'.format(key_name))
        elif event.type==pygame.KEYUP:
            print(u'"{}"key pressed'.format(key_name))
    pygame.draw.rect(screen,(0,125,255),pygame.Rect(30,30,60,60))
    pygame.display.flip()
