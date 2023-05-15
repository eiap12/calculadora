from NLS.Div import *


class Keyboard(GRAPHIC_OBJECT_TEMPLATE):
    def __init__(self):
        super().__init__()
        self.color = None
        self.id_button = []
        self.KEYBOARD_BACKGROUND = Element([0, 120], screen.get_size()[0], 350, lightgray, None)

    def child_creator(self):
        x_offset = 0
        y_offset = 0
        column = 0
        num = 1
        for e in self.id_button:
            self.KEYBOARD_BACKGROUND.container.append(e, Button([x_offset, y_offset], 63, 63, dimgray, whitesmoke,
                                                                self.KEYBOARD_BACKGROUND))
            self.KEYBOARD_BACKGROUND.container.childs[e].set_value(num)
            num = num + 1
            x_offset = x_offset + 70
            column = column + 1
            if column == 3 or column == 6 or column == 9:
                y_offset = y_offset + 70
                x_offset = 0
        print("CHILD_ID", self.KEYBOARD_BACKGROUND.container.childs)
        print("ID_BUTTON", self.id_button)

    def anim(self):
        pass

    def start(self):
        if not self.id_button:
            for e in range(9):
                self.id_button.append(("button" + str(e)))

        self.child_creator()

    def update(self):
        pass

    def fixedUpdate(self):
        screen.fill((255, 255, 255))
        print("fixedUpdate de: ", self)
        self.KEYBOARD_BACKGROUND.fixedUpdate()
