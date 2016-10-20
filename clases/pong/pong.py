#!/usr/bin/python3

import sys
from pygame import K_UP, K_DOWN, RLEACCEL, QUIT, init
from pygame.display import set_mode, set_caption, flip
from pygame.event import get
from pygame.font import Font
from pygame.image import load
from pygame.key import get_pressed
from pygame.mixer import Sound
from pygame.sprite import Sprite, collide_rect
from pygame.time import Clock

ALTO = 480
ANCHO = 640


def cargar_imagen(nombre, transparent=False):
    """
    Carga la imagen dada su ubicacion NOMBRE, además aplica
    transparencias si se le indica. Devuelve un objeto de tipo
    |pygame.Surface|
    """
    try:
        imagen = load(nombre)
    except Exception as message:
        raise SystemExit(message)
    imagen = imagen.convert()
    if transparent:
        color = imagen.get_at((0, 0))
        imagen.set_colorkey(color, RLEACCEL)
    return imagen


def texto(texto, posicion_x, posicion_y, color=(255, 255, 255)):
    """
    Método para insertar el texto TEXTO en la posición (POSICION_X,
    POSICION_Y) con el color COLOR
    """
    fuente = Font('images/17-years-ago.ttf', 25)
    salida = Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posicion_x
    salida_rect.centery = posicion_y
    return salida, salida_rect


class Pala(Sprite):
    """
    Clase Pala: hereda atributos directamente de la clase Sprite,
    que se encuentra en el paquete pygame.sprite. Permite modelar la
    pala de un jugador (usuario o NPC).
    """

    def __init__(self, centerx):
        """
        Constructor, inicializa los siguientes atributos:

        - Imagen de la pala.
        - Posición, la cuál es representada a través de un rectangulo
          invisible.
        - Velocidad por defecto de la pala.

        El parámetro CENTERX permite determinar la posición inicial de
        la pala.
        """
        Sprite.__init__(self)
        self.image = cargar_imagen("images/pala.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = ALTO / 2
        self.speed = 1

    def mover(self, time, keys):
        """Determina la posición de la pala en el tiempo TIME siempre y
        cuando KEYS sea igual a las teclas UP y DOWN."""
        if self.rect.top >= 0:
            if keys[K_UP]:
                self.rect.centery -= self.speed * time
        if self.rect.bottom <= ALTO:
            if keys[K_DOWN]:
                self.rect.centery += self.speed * time

    def ia(self, time, ball):
        """Inteligencia artifical modelada a través de un agente
        reactivo. Dependiendo de la posición de la pelota BALL va a
        realizar su movimiento para contrarrestar el envio del
        oponente. El parámetro TIME cual es la cantidad de pixeles que
        se debe mover."""
        if ball.speed[0] >= 0 and ball.rect.centerx >= ANCHO / 2:
            if self.rect.centery < ball.rect.centery:
                self.rect.centery += self.speed * time
            if self.rect.centery > ball.rect.centery:
                self.rect.centery -= self.speed * time


class Bola(Sprite):
    """
    Clase Bola: hereda atributos directamente de la clase Sprite, que
    se encuentra en el modulo pygame.sprite. Permite modelar la pelota
    con la que se interactua en el juego.
    """

    def __init__(self):
        """
        Constructor que inicializa los siguientes valores:

        - La imagen a desplegar.
        - Posición, la cual es representada a través de un rectangulo
          invisible.
        - Velocidad por defecto de la pelota en el eje Y y Y
        """
        Sprite.__init__(self)
        self.image = cargar_imagen("images/ball.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO / 2
        self.rect.centery = ALTO / 2
        self.sound = Sound('audios/rebote.wav')
        self.speed = [0.4, 0.4]

    def actualizar(self, time, pala, pala_cpu, puntos):
        """
        Actualiza la posición de la pelota en tantos pixeles
        determinado por TIME. Además permite identificar si interactua
        con PALA y PALA_CPU. En caso de que existan puntos, actualiza
        los valores de PUNTOS.
        """
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time
        if self.rect.left <= 0:
            puntos[1] += 1
        if self.rect.right >= ANCHO:
            puntos[0] += 1
        if self.rect.left <= 0 or self.rect.right >= ANCHO:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <= 0 or self.rect.bottom >= ALTO:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time
        if self.rect.left == 0 or self.rect.right == ANCHO:
            self.sound.play()
        if self.rect.top == 0 or self.rect.bottom == ALTO:
            self.sound.play()
        if collide_rect(self, pala):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
            self.sound.play()
        if collide_rect(self, pala_cpu):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
            self.sound.play()
        return puntos


def game_loop():
    """Ciclo de juego. Mientras no se cierre la ventana, el juego no
    termina."""
    pantalla = set_mode((ANCHO, ALTO))
    set_caption("Pong <3")
    fondo = cargar_imagen('images/fondo_pong.png')
    bola = Bola()
    pala = Pala(30)
    pala_cpu = Pala(ANCHO - 30)
    clock = Clock()
    puntos = [0, 0]
    while True:
        time = clock.tick(60)
        keys = get_pressed()
        for eventos in get():
            if eventos.type == QUIT:
                sys.exit(0)
        bola.actualizar(time, pala, pala_cpu, puntos)
        pala.mover(time, keys)
        pala_cpu.ia(time, bola)
        puntos_jug, puntos_jug_rect = texto(
            "Jugador Puntos: " + str(puntos[0]), 140, 40)
        puntos_cpu, puntos_cpu_rect = texto(
            "Maquina Puntos: " + str(puntos[1]), ANCHO - ANCHO / 4, 40)
        pantalla.blit(fondo, (0, 0))
        pantalla.blit(bola.image, bola.rect)
        pantalla.blit(pala.image, pala.rect)
        pantalla.blit(pala_cpu.image, pala_cpu.rect)
        pantalla.blit(puntos_jug, puntos_jug_rect)
        pantalla.blit(puntos_cpu, puntos_cpu_rect)
        flip()
    return 0

if __name__ == '__main__':
    init()
    game_loop()
