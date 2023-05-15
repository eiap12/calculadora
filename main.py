import sys
from Keyboard import *
from NLS.Div import *

# Crea la instancia aquí:
k1 = Keyboard()

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
