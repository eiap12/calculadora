import time

from sn import *
from NLS.Events import *
from NLS.GRAPHIC_OBJECT_TEMPLATE import *
from NLS.Graphics import *


class CONTAINER(ABC):
    # Interfaz container agrega la funcionalidad de tener padres e hijos
    def __init__(self, father):
        super().__init__()
        self.father = father
        self.childs = {}

    def append(self, name, instance):
        # Agrega un hijo
        self.childs[name] = instance

    def remove(self, name):
        # Elimina hijos
        del self.childs[name]

    def get_object(self, name=None):
        # Devuelve al hijo/s
        if name is None:
            return self.childs
        else:
            return self.childs[name]

    def set_father(self, father):
        # Establece un padre
        self.father = father


class Element(GRAPHIC_OBJECT_TEMPLATE):
    # Clase Element para la fácil creación de gráficos
    # Agrega como componente a CONTAINER, RECTANGLE, COMPARE y Text
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

    def get_value(self):
        # Retorna el valor del objeto
        return self.value

    def get_rect(self):
        # Devuelve los atributos del objeto
        rect = {"width": self.rectangle.width, "height": self.rectangle.height, "color": self.rectangle.color,
                "pos": self.rectangle.pos}
        return rect

    def get_pos(self):
        # Devuelve la posición del objeto
        return self.rectangle.pos

    def set_value(self, value):
        # Establece un valor al objeto
        self.value = value

    def set_pos(self, x, y):
        # Establece la posición del objeto
        if self.container.father is not None:
            self.rectangle.pos = [(self.container.father.rectangle.pos[0] + x),
                                  (self.container.father.rectangle.pos[1] + y)]
        else:
            self.rectangle.pos = [x, y]

    def set_color(self, color):
        # Establece el color al objeto
        self.rectangle.color = color

    def show_value(self, size, color):
        # Renderiza el valor del objeto
        self.text = Text(self.value, color, size, self)

    def add_text(self, text, size, color):
        # Renderiza el texto dado como parámetro
        self.text = Text(str(text), color, size, self)

    def update(self):
        # Compara los atributos de los componentes
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
    # Clase Button hereda a Element agrega los eventos
    def __init__(self, pos, width, height, color, pressed_color, father):
        super().__init__(pos, width, height, color, father)
        self.color = color
        self.pressed_color = pressed_color
        self.events = Events(self.rectangle)
        self.events.create_mouse_event()
        self.display = None

    def add_click_fun(self, fun, param):
        try:
            # Ejecuta la función dada como parámetro
            fun(param)
        except SyntaxError:
            print("ERROR: Ninguna función como parámetro en mouse_fun()")

    def click_fun(self):
        # Ejecuta las respectivas funciones para la correcta funcionalidad del objeto
        self.events.mouse_event.onClick(self.set_color, self.pressed_color)
        self.events.mouse_event.onClick(self.display.add_num, self.get_value())
        self.events.mouse_event.onClick(self.add_click_fun)
        if not self.events.mouse_event.onClick():
            self.set_color(self.color)

    def update(self):
        # funciones que se ejecutan en un while
        self.click_fun()
        self.rectangle_hash = self.compare_rectangle.update()
        self.container_hash = self.compare_container.update()
