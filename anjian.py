import pygame
import time
import sys
pygame.display.set_mode()

keyboradcontrol()    
    while True:
        for even in pygame.event.get():
            for event in pygame.event.get():
                if even.type == KEYDOWN:       
                    if event.type == K_q:
                        sys.exit()
                    elif even.key == K_a:
                        left(50,1)
                    elif even.key == K_w:
                        up(50,1)
                    elif even.key == K_s:
                        down(50,1)
                    elif even.key == K_d:
                        right(50,1)
                elif event.type == KEYUP:
                    stop()
