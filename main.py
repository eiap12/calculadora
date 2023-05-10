import multiprocessing
import sys
from global_code import *
from NLS.Div import *

# campo de prueba de código


class Keyboard(GRAPHIC_OBJECT_TEMPLATE):
    def __init__(self):
        super().__init__()
        self.color = None
        self.id_button = []
        self.KEYBOARD_BACKGROUND = Element([0, 120], 250, 250, b4, None)

    def child_creator(self):
        x = 0
        y = 0
        c = 0
        num = 1
        for e in self.id_button:
            self.KEYBOARD_BACKGROUND.container.append(e, Element([x, y], 63, 63, green, self.KEYBOARD_BACKGROUND))
            self.KEYBOARD_BACKGROUND.container.childs[e].set_value(num)
            self.KEYBOARD_BACKGROUND.container.childs[e].create_event()
            num = num + 1
            x = x + 62
            c = c + 1
            if c == 3 or c == 6 or c == 9:
                y = y + 62
                x = 0
        print("CHILD_ID", self.KEYBOARD_BACKGROUND.container.childs)
        print("ID_BUTTOM", self.id_button)

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



# Inicializa
k1 = Keyboard()
"""p1 = Element([0,0],50,50, white)
p1.append("puta", Element([0,0],25,25, black))
obj = p1.get_object("puta")
obj.append("perra", Element([0,0],5,5, green))
print(obj.father)"""

# No modificar a menos de que sea necesario
clock = pygame.time.Clock()

while True:
    # Bucle principal
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    clock.tick(60)
    obj_admin.update()
    pygame.display.flip()
