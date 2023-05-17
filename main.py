import sys
from Keyboard import *
from display import *
from NLS.Div import *


class Calculadora:
    def __init__(self):
        self.d1 = Display()
        self.k1 = Keyboard(self.d1)
        self.separator = Element([0, 120], screen.get_size()[0], 1, gray, None)
        self.separator2 = Element([0, 60], screen.get_size()[0], 1, lightgray, None)


calculadora = Calculadora()

# No modificar a menos de que sea necesario
clock = pygame.time.Clock()

while True:
    # Bucle principal
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    clock.tick(120)
    obj_admin.update()
    pygame.display.flip()
