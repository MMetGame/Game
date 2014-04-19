#GRAVITY = 10

#def move(self, delta):
#    self.x+= (self.vx * delta)
#    self.y+= (self.vy * delta)

#def speed(self, delta):
#    self.vy += (GRAVITY * delta)

#clock.tick()

#while True:
#    clock.tick()
#    delta = (clock.get_time() / 100) #should be /1000
#    ball.move(delta)
#    ball.speed(delta)


# Modulos
import pygame                  #importamos modulo para trabajar con juegos
from pygame.locals import *    #carga las constantes, sin llamar a pygame
from optparse import OptionParser  #para el parceo
import sys


# Constantes
WIDTH = 680   # ancho de la ventana
HEIGHT = 544  # alto de la ventana
INIT = 0 # posicion 0 del largo y ancho de la ventana
JUMP = 5

WIDTH_BALL = 16  # ancho de la pelota
HEIGHT_BALL = 16  # largo de la pelota

# Clases
#-------------------------------------------------------------------------------
class Pelota(pygame.sprite.Sprite):

    def __init__(self, x=WIDTH, y=HEIGHT):
        self.image = load_image('images/ball.png')
        self.rect = self.image.get_rect() #dimension y posicion de la imagen
        self.rect.centerx = x/2
        self.rect.centery = y/2
        self.speed = [0.10,0.10]

    def movimiento(self, time):
        self.rect.centerx = self.rect.centerx + (self.speed[0] * time)
        self.rect.centery = self.rect.centery + (self.speed[1] * time)
        if (self.rect.centerx <= INIT or self.rect.centerx >= WIDTH):
            self.speed[0] = -self.speed[0]
            self.rect.centerx = self.rect.centerx + (self.speed[0] * time)
        if (self.rect.centery <= INIT or self.rect.centery >= HEIGHT):
            self.speed[1] = -self.speed[1]
            self.rect.centery = self.rect.centery + (self.speed[1] * time)


#class 

    # Funcion para mover por teclado
    def move_object(self, time):
        teclas = pygame.key.get_pressed()
        if (self.rect.centery + HEIGHT_BALL/2 < HEIGHT):
            if teclas[K_DOWN]:
                self.rect.centery = self.rect.centery + (self.speed[1] * time)
        if (self.rect.centery - HEIGHT_BALL/2 > INIT):
            if teclas[K_UP]:
                self.rect.centery = self.rect.centery - (self.speed[1] * time)
        if (self.rect.centerx - WIDTH_BALL/2 > INIT):
            if teclas[K_LEFT]:
                self.rect.centerx = self.rect.centerx - (self.speed[0] * time)
        if (self.rect.centerx + WIDTH_BALL/2 < WIDTH):
            if teclas[K_RIGHT]: 
                self.rect.centerx = self.rect.centerx + (self.speed[0] * time)

# Funciones
#-------------------------------------------------------------------------------


def load_image(filename):
    try:
        #agregar un try por si no se carga la imagen
        image = pygame.image.load(filename)
    #exepcion: no se pudo abrir el archivo y se guarda en message
    except pygame.error, message:
        #si hubo error al cargar mandamos un mensaje de lo que ocurrio
        raise SystemExit, message
    return image



def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) #Creo la ventana
    pygame.display.set_caption("Daro") #defino el titulo de la ventana
    ball1 = Pelota()
    ball2 = Pelota(WIDTH_BALL/2, HEIGHT_BALL/2)
    try:
        #cargando fondo
        fondo = load_image("images/campo.jpg")
    except:
        #si hubo error al cargar fondo salimos del programa
        sys.stderr.write("El archivo no existe\n")
        sys.exit(1)
    #cuanto tiempo estoy jugando
    time_clock = pygame.time.Clock()
    while True:
        time = time_clock.tick(60)
        #recorremos la lista de eventos de pygame para ver si hay un QUIT
        for event in pygame.event.get():
            #cierro la ventana si el tipo de evento es QUIT
            if event.type == QUIT:
                sys.exit(0)
        #imprime el fondo en la posicion (0,0) de la ventana
        screen.blit(fondo, (0, 0))
        screen.blit(ball1.image, ball1.rect)
        screen.blit(ball2.image, ball2.rect)
        #controlo la velocidad de la pelota
        ball1.movimiento(time)
        ball2.move_object(time)

        #si hubo colision
        if (pygame.sprite.collide_rect(ball1, ball2)):
            ball1.speed[0] = -ball1.speed[0]
            ball1.speed[1] = -ball1.speed[1]
            ball1.rect.centerx = ball1.rect.centerx + (ball1.speed[0] * time)
            ball1.rect.centery = ball1.rect.centery + (ball1.speed[1] * time)


        #Actualiza la ventana
        pygame.display.flip()
    return 0


if __name__ == '__main__':
    #pygame.init()     #inicializamos el modulo pygame
    main()

