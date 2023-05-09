import multiprocessing
import sys
from global_code import *
from NLS.Div import *

# campo de prueba de código


class Keyboard(GRAPHIC_OBJECT_TEMPLATE):
    def __init__(self):
        super().__init__()
        self.color = None
        self.div = None
        self.id_button = []

    def change_color(self, e):
        instance = self.div.child_id[e].get_obj()
        instance.color = white
        print("COLOR: ", instance.color[1])
        print("objetos:", obj_admin.objetos)

    def prev_color(self, e):
        instance = self.div.child_id[e].get_obj()
        instance.color = gray
        print("COLOR: ", instance.color[1])
        print("objetos:", obj_admin.objetos)

    def child_creator(self):
        x = 0
        y = 0
        c = 0
        num = 1
        for e in self.id_button:

            self.div.append_child(e, gray, 63, posx=x, posy=y)
            self.div.child_id[e].set_value(num)
            self.div.child_id[e].click_on = True
            self.div.child_id[e].text_attributes = {'num': num, 'color': black, 'width': 5, 'posx': 0, 'posy': 0}
            num = num + 1
            x = x + 62
            c = c + 1
            if c == 3 or c == 6 or c == 9:
                y = y + 62
                x = 0
        print("CHILD_ID", self.div.child_id)
        print("ID_BUTTOM", self.id_button)

    def anim(self):
        pass

    def start(self):
        if not self.id_button:
            for e in range(9):
                self.id_button.append(("div_child" + str(e)))
        self.div = Div_father(screen, b4, 250, 250, pos_x=0, pos_y=120)
        self.child_creator()

    def update(self):
        pass

    def fixedUpdate(self):
        self.clean_screen(screen)
        print("fixedUpdate de: ", self)
        self.div.fixedUpdate()


class prueba(GRAPHIC_OBJECT_TEMPLATE):
    def __init__(self):
        super().__init__()
        self.box = Graphics(screen)
        self.color = [0, 0, 0]

    def change_color(self):
        if self.color[0] < 255:
            self.color[0] += 5

    def anim(self):
        self.change_color()

    def start(self):
        self.color_process = multiprocessing.Value('i', self.color[0])

    def fixedUpdate(self):
        self.box.draw(50, 50, 0, 0, self.color)


# Inicializa
# k1 = Keyboard()
p1 = Element([0,0],50,50, white)

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
