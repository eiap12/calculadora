from abc import ABC

from NLS.Graphics import *
from sn import Sn
from NLS.GRAPHIC_OBJECT_TEMPLATE import *


class CONTAINER(ABC):
    def __init__(self, father=None):
        self.father = father
        self.childs = []

    def append(self, obj):
        self.childs.append(obj)

    def remove(self, obj):
        self.childs.remove(obj)
        del obj

    def get_object(self):
        return self.childs


class Element(GRAPHIC_OBJECT_TEMPLATE, CONTAINER, RECT):
    def __init__(self, pos, width, height, color):
        GRAPHIC_OBJECT_TEMPLATE.__init__(self)
        CONTAINER.__init__(self)
        RECT.__init__(self, pos, width, height, color)
        self.value = None

    def set_value(self, value):
        self.value = value

    def anim(self):
        pass

    def start(self):
        pass

    def update(self):
        pass

    def fixedUpdate(self):
        self.render()


class Div_father(GRAPHIC_OBJECT_TEMPLATE, Sn):
    def __init__(self, screen, color, width, height=None, center="", pos_x=0, pos_y=0, click_on=False):
        GRAPHIC_OBJECT_TEMPLATE.__init__(self)
        Sn.__init__(self, screen)
        self.child_id = {}
        self.pos_xp = pos_x
        self.pos_yp = pos_y
        self.color = list(color)
        self.width = width
        self.height = height
        self.center = center
        self.center_pos = None
        self.value = None
        self.click_on = click_on
        self.mouse_press = False
        self.text_attributes = {'num': None, 'color': (0, 0, 0), 'width': None, 'posx': 0, 'posy': 0}

    def show(self):
        if self.height is None:
            self.height = self.width
            Graphics.box(self, self.width, self.pos_xp, self.pos_yp, self.color)
        else:
            self.center_pos = Graphics.rect(self, self.width, self.height, self.color, self.center, self.pos_xp,
                                            self.pos_yp)

    def append_child(self, Id, color, width, height=None, center="", posx=0, posy=0):
        if Id in self.child_id:
            print(Fore.YELLOW + "Append_child Log:" + Fore.RESET)
            print("Ya se encuentra registrado")
        else:
            print("APPEND_CHILD_ID", Id)
            pos_x = self.pos_xp + posx
            pos_y = self.pos_yp + posy

            self.child_id[Id] = Div_child(self.screen, color, width, height, center, pos_x, pos_y)

            print(Fore.YELLOW + "Append_child Log:" + Fore.RESET)
            print("Childs creados: ", self.child_id)
            print("objetos del administrador: ", obj_admin.objetos)

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def text(self):
        if self.text_attributes['num'] is not None:
            pos_x = self.pos_xp + self.text_attributes['posx']
            pos_y = self.pos_yp + self.text_attributes['posy']
            self.render_numbers(self.text_attributes['num'], self.text_attributes['color'],
                                self.text_attributes['width'],
                                pos_x, pos_y)

    def mouse_event(self):
        mouse_pos = pygame.mouse.get_pos()
        button = pygame.mouse.get_pressed(3)
        if self.pos_xp < mouse_pos[0] < (self.pos_xp + self.width) and self.pos_yp < mouse_pos[1] < (
                self.pos_yp + self.width):
            if button[0]:
                print(self.value, mouse_pos)
                self.mouse_press = True
            else:
                self.mouse_press = False
        else:
            self.mouse_press = False

    def start(self):
        pass

    def anim(self):
        if self.click_on:
            if self.mouse_press:
                if self.color[0] < 255:
                    self.color[0] += (255 / 5)
            else:
                self.color[0] = 0

    def list_childs(self):
        print(self.child_id)
        return self.child_id

    def len_childs(self):
        print(len(self.child_id))
        return len(self.child_id)

    def get_obj(self):
        # id_obj = id(self)
        # instance = ctypes.cast(id_obj, ctypes.py_object).value
        return self

    def update(self):
        if self.click_on:
            self.mouse_event()

    def fixedUpdate(self):
        self.show()
        self.text()
        if self.child_id != {}:
            for e in self.child_id:
                self.child_id[e].fixedUpdate()
        print("fixedUpdate de: ", self)


class Div_child(Div_father):
    pass
