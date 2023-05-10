from abc import ABC
import pygame


class MOUSE_EVENTS(ABC):
    def __init__(self, obj):
        self._width = obj.width
        self._height = obj.height
        self._pos = obj.pos

    def onclick(self,f, *args):
        cursor_on = self.check_cursor_position()
        click = self.click()
        if cursor_on and click:
            f(*args)
            return True
        else:
            return False

    def check_cursor_position(self):
        mouse_pos = pygame.mouse.get_pos()
        if self._pos[0] < mouse_pos[0] < (self._pos[0] + self._width) and \
                self._pos[1] < mouse_pos[1] < (self._pos[1] + self._height):
            return True
        else:
            return False

    def click(self):
        button = pygame.mouse.get_pressed(3)
        if button[0]:
            return True
        else:
            return False


class Events:
    def __init__(self, obj):
        self.obj = obj
        self.mouse_event = None

    def create_mouse_event(self):
        self.mouse_event = self.Mouse(self.obj)

    class Mouse(MOUSE_EVENTS):
        pass
