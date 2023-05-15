from NLS.Graphics import *
from numeros import *


# Funciones estáticas

def desc_num(num):  # Toma cada digito de un numero y lo guarda en una lista
    num = str(num)
    numbers = []
    for e in num:
        numbers.append(int(e))
    return numbers


def cod_num(num):  # Para utilizar la funcion render_number() se necesitan usar listas con las posiciones de pixeles.
    if num == 1:  # Al utilizar cod_num() los numeros entregados en los parametros se convertiran en lista con
        return n1_map  # las posiciones de pixel del numero. Ejemplo cod_num(4) = n4_map
    if num == 2:
        return n2_map
    if num == 3:
        return n3_map
    if num == 4:
        return n4_map
    if num == 5:
        return n5_map
    if num == 6:
        return n6_map
    if num == 7:
        return n7_map
    if num == 8:
        return n8_map
    if num == 9:
        return n9_map
    if num == 0:
        return n0_map


class Sn(Graphics):  # clase Sistema de Números

    def render_number(self, color, nmap, width, pos_x, pos_y):  # se grafica un solo numero
        z = 0  # Esta variable es un contador
        for i in nmap:
            m = nmap[z]
            x = m[0]
            y = m[1]
            self.box(width, pos_x + (x * width), pos_y + (y * width), color)
            z = z + 1

    def render_numbers(self, num, color, width, pos_x, pos_y):
        # se grafica una cadena de números
        numbers = desc_num(num)
        n = 6

        for e in numbers:
            new_pos_x = (width * n) + pos_x
            if numbers.index(e) == 0:
                self.render_number(color, cod_num(e), width, pos_x, pos_y)

            else:
                self.render_number(color, cod_num(e), width, new_pos_x, pos_y)
                n = n + 6


class Text:
    def __init__(self):