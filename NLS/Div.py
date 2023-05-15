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

    def set_pos(self, x, y):
        if self.container.father is not None:
            self.rectangle.pos = [(self.container.father.rectangle.pos[0] + x),
                                  (self.container.father.rectangle.pos[1] + y)]
        else:
            self.rectangle.pos = [x, y]

    def set_color(self, color):
        self.rectangle.color = color

    def update(self):
        self.rectangle_hash = self.compare_rectangle.update()
        self.container_hash = self.compare_container.update()

    def fixedUpdate(self):
        self.rectangle.render()
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

        def mouse_fun(self):
            pass

        def click_fun(self):
            self.events.mouse_event.onClick(self.set_color, self.pressed_color)
            self.events.mouse_event.onClick(self.mouse_fun())
            if not self.events.mouse_event.onClick():
                self.set_color(self.color)

        def update(self):
            self.click_fun()
            self.rectangle_hash = self.compare_rectangle.update()
            self.container_hash = self.compare_container.update()

