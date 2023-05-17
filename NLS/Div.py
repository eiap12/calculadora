import time

from sn import *
from NLS.Events import *
from NLS.GRAPHIC_OBJECT_TEMPLATE import *
from NLS.Graphics import *


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

        self.text = None
        self.container = CONTAINER(father)
        self.rectangle = RECTANGLE(pos, width, height, color)

        self.compare_rectangle = Compare(self.rectangle)
        self.compare_container = Compare(self.container)

        self.container_hash = None
        self.rectangle_hash = None

        self.value = None

        if self.container.father is not None:
            self.rectangle.pos = [(self.container.father.rectangle.pos[0] + self.rectangle.pos[0]),
                                  (self.container.father.rectangle.pos[1] + self.rectangle.pos[1])]

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def get_rect(self):
        rect = {"width": self.rectangle.width, "height": self.rectangle.height, "color": self.rectangle.color}
        return rect

    def get_pos(self):
        return self.rectangle.pos

    def set_pos(self, x, y):
        if self.container.father is not None:
            self.rectangle.pos = [(self.container.father.rectangle.pos[0] + x),
                                  (self.container.father.rectangle.pos[1] + y)]
        else:
            self.rectangle.pos = [x, y]

    def set_color(self, color):
        self.rectangle.color = color

    def show_value(self, size, color):
        self.text = Text(self.value, color, size, self)

    def add_text(self, text, size, color):
        self.text = Text(str(text), color, size, self)

    def update(self):
        self.rectangle_hash = self.compare_rectangle.update()
        self.container_hash = self.compare_container.update()

    def fixedUpdate(self):
        self.rectangle.render()
        if self.text is not None:
            self.text.fixedUpdate()
        if self.container.childs != {}:
            for e in self.container.childs:
                self.container.childs[e].fixedUpdate()


class Button(Element):
        def __init__(self, pos, width, height, color, pressed_color, father):
            super().__init__(pos, width, height, color, father)
            self.color = color
            self.pressed_color = pressed_color
            self.events = Events(self.rectangle)
            self.events.create_mouse_event()
            self.display = None
            self.fun = None
            self.param = None

        def set_fun(self):
            self.fun = self.display.add_num(self.get_value())
            print("numero display:", self.display.operation)

        def mouse_fun(self):
            try:
                if self.fun is not None:
                    self.fun()

            except:
                print("ERROR: Ninguna funcion como paramentro en mouse_fun()")
            finally:
                self.fun = self.display.add_num(self.get_value())
                time.sleep(0.1)

        def click_fun(self):
            self.events.mouse_event.onClick(self.set_color, self.pressed_color)
            self.events.mouse_event.onClick(self.mouse_fun)
            if not self.events.mouse_event.onClick():
                self.set_color(self.color)

        def update(self):
            # funciones que se ejecutan en un while
            self.click_fun()
            self.rectangle_hash = self.compare_rectangle.update()
            self.container_hash = self.compare_container.update()

