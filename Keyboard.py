from NLS.Div import *


def prueba(self):
    print("Perra puta", self.get_rect()["color"])


"""
def mouse_fun(objf, objt):
    objf."""


class Keyboard(GRAPHIC_OBJECT_TEMPLATE):
    def __init__(self, display):
        super().__init__()
        self.color = None
        self.id_button = []
        self.KEYBOARD_BACKGROUND = Element([0, 120], screen.get_size()[0], 400, superlightgray, None)
        self.display = display

    def define(self, num, e):
        # Define los signos
        if num == 10:
            self.KEYBOARD_BACKGROUND.container.childs[e].set_value("+")
            self.KEYBOARD_BACKGROUND.container.childs[e].show_value(30, black)
        if num == 11:
            self.KEYBOARD_BACKGROUND.container.childs[e].set_value("0")
            self.KEYBOARD_BACKGROUND.container.childs[e].show_value(30, black)
        if num == 12:
            self.KEYBOARD_BACKGROUND.container.childs[e].set_value("-")
            self.KEYBOARD_BACKGROUND.container.childs[e].show_value(30, black)
        if num == 13:
            self.KEYBOARD_BACKGROUND.container.childs[e].set_value("*")
            self.KEYBOARD_BACKGROUND.container.childs[e].show_value(30, black)
        if num == 14:
            self.KEYBOARD_BACKGROUND.container.childs[e].set_value("/")
            self.KEYBOARD_BACKGROUND.container.childs[e].show_value(30, black)
        if num == 15:
            self.KEYBOARD_BACKGROUND.container.childs[e].set_value("=")
            self.KEYBOARD_BACKGROUND.container.childs[e].show_value(30, black)

    def child_creator(self):
        # Crea el conjunto de botones
        x_offset = int((screen.get_rect().width - 70 * 3) / 2)
        y_offset = 10
        column = 0
        num = 1
        for e in self.id_button:
            self.KEYBOARD_BACKGROUND.container.append(e, Button([x_offset, y_offset], 63, 63, white, whitesmoke,
                                                                self.KEYBOARD_BACKGROUND))
            self.KEYBOARD_BACKGROUND.container.childs[e].display = self.display
            if num > 9:
                self.define(num, e)
            else:
                self.KEYBOARD_BACKGROUND.container.childs[e].set_value(num)
                self.KEYBOARD_BACKGROUND.container.childs[e].show_value(30, black)
                #self.KEYBOARD_BACKGROUND.container.childs[e].set_fun()

            num = num + 1
            x_offset = x_offset + 70
            column = column + 1
            if column == 3 or column == 6 or column == 9 or column == 12:
                y_offset = y_offset + 70
                x_offset = int((screen.get_rect().width - 70 * 3) / 2)
        print("CHILD_ID", self.KEYBOARD_BACKGROUND.container.childs)
        print("ID_BUTTON", self.id_button)

    def start(self):
        if not self.id_button:
            # Crea el nombre de los botones
            for e in range(15):
                self.id_button.append(("button" + str(e)))

        self.child_creator()

    def fixedUpdate(self):
        screen.fill((255, 255, 255))
        print("fixedUpdate de: ", self)
        self.KEYBOARD_BACKGROUND.fixedUpdate()
