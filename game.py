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


# Importando Modulos
import pygame                      # importamos modulo para trabajar con juegos
from pygame.locals import *        # carga las constantes, sin llamar a pygame
from optparse import OptionParser  # para el parceo
import sys

# Constantes
WIDTH = 680   # ancho de la ventana
HEIGHT = 544  # alto de la ventana
INIT = 0      # posicion 0 del largo y ancho de la ventana


WIDTH_BALL = 16  # ancho de la pelota
HEIGHT_BALL = 16  # largo de la pelota
eje_x = 0 # posicion en el eje x para ej arreglo de la velocidad
eje_y = 1 # posicion en el eje y para ej arreglo de la velocidad
EXIT_SUCCESS = 0 #Salida exitosa
EXIT_FAILURED = 1 #Salida con fallas


class Pelota(pygame.sprite.Sprite):

    def __init__(self, x=WIDTH, y=HEIGHT):
        self.image = load_image('images/ball.png') # cargamos imagenes
        self.rect = self.image.get_rect()  # dimension y posicion de la imagen
        self.rect.centerx = x / 2# posicion en eje_x en la pantalla
        self.rect.centery = y / 2 # posicion en eje_y en la pantalla
        self.speed = [0.2, 0.2] # Velocidad en eje_x y eje_y de la imagen

    # La pelota que se mueve sola
    def movimiento(self, time):
        self.rect.centerx += (self.speed[eje_x] * time)
        self.rect.centery += (self.speed[eje_y] * time)
        if (self.rect.left <= INIT or self.rect.right >= WIDTH):
            self.speed[eje_x] = -self.speed[eje_x]
            self.rect.centerx += (self.speed[eje_x] * time)
        if (self.rect.top <= INIT or self.rect.bottom >= HEIGHT):
            self.speed[eje_y] = -self.speed[eje_y]
            self.rect.centery += (self.speed[eje_y] * time)

    # Funcion para mover por teclado
    def move_object(self, time):
        # Si la pantalla recibe la entrada del raton
        if pygame.mouse.get_focused():
            # La pelota se desplace a la posicion del mause
            self.rect.center = pygame.mouse.get_pos()
        teclas = pygame.key.get_pressed()
        if (self.rect.bottom < HEIGHT) and teclas[K_DOWN]:
            self.rect.centery += (self.speed[eje_y] * time)
        if (self.rect.top > INIT) and teclas[K_UP]:
            self.rect.centery -= (self.speed[eje_y] * time)
        if (self.rect.left > INIT) and teclas[K_LEFT]:
            self.rect.centerx -= (self.speed[eje_x] * time)
        if (self.rect.right < WIDTH) and teclas[K_RIGHT]:
            self.rect.centerx += (self.speed[eje_x] * time)


# Funciones
#------------------------------------------------------------------------------
def load_image(filename):
    try:
        #agregar un try por si no se carga la imagen
        image = pygame.image.load(filename)
    #exepcion: no se pudo abrir el archivo y se guarda en message
    except pygame.error, message:
        #si hubo error al cargar mandamos un mensaje de lo que ocurrio
        raise SystemExit(message)
    return image

# Funcion que Detecta colisiones entre objetos
def collide(ball1, ball2, time):
    if (pygame.sprite.collide_rect(ball1, ball2)):
        ball1.speed[eje_x] = -ball1.speed[eje_x]
        ball1.speed[eje_y] = -ball1.speed[eje_y]
        ball1.rect.centerx += (ball1.speed[eje_x] * time)
        ball1.rect.centery += (ball1.speed[eje_y] * time)

# Funcion que termina con la ejecucion de mi programa
def program_quit():
    # grabo la entrada del teclado
    teclas = pygame.key.get_pressed()
    #recorremos la lista de eventos de pygame para ver si hay un QUIT
    for event in pygame.event.get():
        #cierro la ventana si el tipo de evento es QUIT o presione Escape
        if event.type == QUIT or teclas[K_ESCAPE]:
            sys.exit(EXIT_SUCCESS)


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Creo la ventana
    pygame.display.set_caption("Daro")     # defino el titulo de la ventana
    ball1 = Pelota()
    ball2 = Pelota(WIDTH_BALL / 2, HEIGHT_BALL / 2)
    try:
        fondo = load_image("images/campo.jpg")
    except:
        #si hubo error al cargar fondo salimos del programa
        sys.stderr.write("El archivo no existe\n")
        sys.exit(EXIT_FAILURED)
    #cuanto tiempo estoy jugando
    time_clock = pygame.time.Clock()
    while True:
        time = time_clock.tick(60)
        #imprime el fondo en la posicion (0,0) de la ventana
        screen.blit(fondo, (0, 0))
        #imprime las pelotas en la posicion definida por ball.rect
        screen.blit(ball1.image, ball1.rect)
        screen.blit(ball2.image, ball2.rect)
        #Movimientos de la pelota
        ball1.movimiento(time)
        ball2.move_object(time)
        #si hubo colision
        collide(ball1, ball2, time)
        #Actualiza la ventana
        pygame.display.flip()
        #cerrando el programa
        program_quit()
    return 0


if __name__ == '__main__':
    #pygame.init()     #inicializamos el modulo pygame
    main()

