#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *
 
# Constantes
WIDTH = 800
HEIGHT = 600
 
# Clases
# ---------------------------------------------------------------------
class Pala(pygame.sprite.Sprite):
    def __init__(self, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/logomeca.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = HEIGHT / 2
        self.rect.centery = y
        self.speed = 0.5

    def mover(self, time, keys):
        if self.rect.left >= 0:
            if keys[K_LEFT]:
               self.rect.centerx -= self.speed * time
        if self.rect.right <= WIDTH:
            if keys[K_RIGHT]:
               self.rect.centerx += self.speed * time
        if self.rect.top >= 0:
            if keys[K_UP]:
               self.rect.centery -= self.speed * time
        if self.rect.bottom <= HEIGHT:
            if keys[K_DOWN]:
               self.rect.centery += self.speed * time

#class Enemigo(pygame.sprite.Sprite):
 #   def

# ---------------------------------------------------------------------
 
# Funciones
# ---------------------------------------------------------------------

def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error as message:
                raise SystemExit(message)
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image




# ---------------------------------------------------------------------
 
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame")

    background_image = load_image('images/fondo_pong.png')
    pala_jug = Pala(30)

    clock = pygame.time.Clock()

    while True:
        time = clock.tick(80)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)


        pala_jug.mover(time, keys)
        screen.blit(background_image, (0, 0))
        screen.blit(pala_jug.image, pala_jug.rect)
        pygame.display.flip()
    return 0

 
if __name__ == '__main__':
    pygame.init()
    main()



                

    

    
