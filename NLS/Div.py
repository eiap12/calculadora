from abc import ABC
from NLS.Events import *

from NLS.Graphics import *
from sn import Sn
from NLS.GRAPHIC_OBJECT_TEMPLATE import *


class CONTAINER(ABC):
    def __init__(self, father):
        super().__init__()
        self.father = father
        self.childs = {}

    def append(self, name, instance):
        self.childs[name] = instance

    def remove(self, name):
        del self.childs[name]

    def get_object(self, name):
        return self.childs[name]

    def set_father(self, father):
        self.father = father


class Element(GRAPHIC_OBJECT_TEMPLATE):
    def __init__(self, pos, width, height, color, father):
        GRAPHIC_OBJECT_TEMPLATE.__init__(self)

        self.container = CONTAINER(father)
        self.rectangle = RECTANGLE(pos, width, height, color)

        self.value = None
        if self.container.father is not None:
            self.rectangle.pos = [(self.container.father.rectangle.pos[0] + self.rectangle.pos[0]),
                                  (self.container.father.rectangle.pos[1] + self.rectangle.pos[1])]

        self.events = Events(self.rectangle)

    def create_event(self):
        self.events.create_mouse_event()

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_pos(self, x, y):
        if self.container.father is not None:
            self.rectangle.pos = [(self.container.father.rectangle.pos[0] + x),
                                  (self.container.father.rectangle.pos[1] + y)]
        else:
            self.rectangle.pos = [x, y]

    def set_color(self, color):
        self.rectangle.color = color

    def update(self):
        if self.events.mouse_event is not None:
            self.events.mouse_event.onclick(self.set_color, (0,0,0))

    def fixedUpdate(self):
        self.rectangle.render()
        if self.container.childs != {}:
            for e in self.container.childs:
                self.container.childs[e].fixedUpdate()


