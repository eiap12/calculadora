from abc import ABC
import msvcrt
import pygame


class KEYBOARD(ABC):
    # Eventos de teclado usando el módulo msvcrt
    # en próximas actualizaciones
    pass


class MOUSE_EVENTS(ABC):
    def __init__(self, obj):
        # Obtiene los atributos del objeto dado como parámetro
        self._width = obj.width
        self._height = obj.height
        self._pos = obj.pos

    def onClick(self, f=None, *args):
        # Detecta cuando hay un click en el objeto, devuelve True si es presionado
        cursor_on = self.mouse_over()
        click = self.click()
        if cursor_on and click:
            try:
                f(*args)
            except TypeError:
                pass
            return True
        else:
            return False

    def mouse_over(self):
        # Detecta si el puntero esta encima del objeto
        mouse_pos = pygame.mouse.get_pos()
        if self._pos[0] < mouse_pos[0] < (self._pos[0] + self._width) and \
                self._pos[1] < mouse_pos[1] < (self._pos[1] + self._height):
            return True
        else:
            return False

    def click(self):
        # Detecta si hubo un click en pantalla
        button = pygame.mouse.get_pressed(3)
        if button[0]:
            return True
        else:
            return False


class Events:
    def __init__(self, obj):
        # Esta clase agrupa todos los eventos
        self.obj = obj
        self.mouse_event = None

    def create_mouse_event(self):
        # crea un evento de mouse
        self.mouse_event = self.Mouse(self.obj)

    class Mouse(MOUSE_EVENTS):
        pass
