from abc import ABC
from pygame import gfxdraw
from global_code import *


# Arreglar compatibilidad de center con admin y div.
# En esta primera version la clase graphics solo puede dibujar rectangulos en pantalla
class Graphics:
    # Esta clase funciona como base para dibujar figuras varias

    @staticmethod
    def draw(width, height, pos_x, pos_y, color):  # Dibuja en pantalla
        """
        Dibuja un rectangulo en pantalla.

        :param width: El ancho del rectángulo.
        :type width: int
        :param height: Altura del rectángulo.
        :type height: int
        :param pos_x: Posición del rectángulo en el eje x.
        :type pos_x: int
        :param pos_y: Posición del rectángulo en el eje y.
        :type pos_y: int
        :param color: Color del rectángulo.
        :type color: tuple(int, int, int)
        """
        pixel_x = 0
        pixel_y = 0
        while pixel_y != height:
            for x in range(width):
                pygame.gfxdraw.pixel(screen, pos_x + pixel_x, pos_y + pixel_y, color)
                pixel_x = pixel_x + 1
            pixel_y = pixel_y + 1
            pixel_x = 0

    def box(self, width, pos_x, pos_y, color):  # Dibuja un cuadrado
        # Esta funcion sera eliminada porque draw ya hace esto
        width = width
        height = width

        self.draw(width, height, pos_x, pos_y, color)

    def rect(self, width, height, color, center="", pos_x=0, pos_y=0):
        # Esta funcion sera eliminada porque draw ya hace esto
        """Dibuja un rectángulo, este se puede centrar vertical y horizontal con el parámetro center.
            center toma los siguientes valores: center_x, center_y, center_xy"""
        width = width
        height = height
        wh_screen = self.screen.get_size()

        if center == "center_x":
            posc_x = int((wh_screen[0] - width) / 2)
            self.draw(width, height, posc_x, pos_y, color)
            return posc_x, pos_y
        if center == "center_y":
            posc_y = int((wh_screen[2] - height) / 2)
            self.draw(width, height, pos_x, posc_y, color)
            return posc_y, pos_x

        # center_xy ERROR arreglar
        if center == "center_xy":
            posc_x = int((wh_screen[0] - width) / 2)
            posc_y = int((wh_screen[2] - height) / 2)
            self.draw(width, height, posc_x, posc_y, color)
        if center == "":
            self.draw(width, height, pos_x, pos_y, color)
            return pos_x, pos_y


class RECTANGLE(ABC):
    # Interfaz RECTANGLE sirve de base para renderizar figuras en pantalla
    def __init__(self, pos, width, height, color):
        self.pos = pos
        self.width = width
        self.height = height
        self.color = color

    def render(self):
        # Dibuja la figura
        Graphics.draw(self.width, self.height, self.pos[0], self.pos[1], self.color)
