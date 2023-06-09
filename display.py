from NLS.Div import *


class Display(GRAPHIC_OBJECT_TEMPLATE):
    # Crea una pantalla en la cual se muestran las operaciones y resultados
    def __init__(self):
        super().__init__()
        self.DISPLAY_BACKGROUND = Element([0, 0], screen.get_size()[0], 120, superlightgray, None)
        self.operation_render = Element([0, 10], screen.get_size()[0], 50, superlightgray, None)
        self.result_render = Element([0, 61], screen.get_size()[0], 50, superlightgray, None)
        self.operation = ""
        self.result = ""

    def add_num(self, num):
        # Agrega un número a self.operation para posteriormente realizar la operación
        if num == "=":
            if self.operation == "":
                self.result = ""
            else:
                self.result = eval(str(self.operation))
                self.operation = ""
        else:
            if self.operation == "":
                self.operation = str(num)
            else:
                self.operation += str(num)
        time.sleep(0.15)

    def fixedUpdate(self):
        self.operation_render.add_text(self.operation, 30, black)
        self.result_render.add_text(self.result, 30, black)
