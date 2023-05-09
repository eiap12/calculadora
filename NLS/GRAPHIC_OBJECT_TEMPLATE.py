from NLS.Admin import *
from global_code import *
from abc import ABC, abstractmethod


# Patron de diseño: Template Method
class GRAPHIC_OBJECT_TEMPLATE(ABC):
    # Es una clase abstracta que sirve de plantilla para objetos que pueden aparecer en pantalla
    def __init__(self):
        """
        Registra la instancia en el administrador de objetos para
        posteriormente realizar una serie de tareas para la correcta ejecución y rendimiento del programa.
        """
        self.start_state = False
        obj_admin.add_obj(self)

    def clean_screen(self, color=None):
        # Limpia la pantalla
        if color is None:
            screen.fill((255, 255, 255))
        else:
            screen.fill(color)

    def get_vars(self):
        """
        Devuelve las variables contenidas en la instancia
        para posteriormente en el administrador de objetos se verifique si cambio
        algún valor
        """
        return str(self.__dict__)

    @abstractmethod
    def anim(self):
        """
        Aquí va código que se cambiara atributos del objeto progresivamente en un lapso de tiempo,
        se ejecutará constantemente en un bucle.
        El administrador de objetos toma el código que haya aquí y lo
        ejecutara constantemente en el bucle principal
        """
        pass

    @abstractmethod
    def start(self):

        """

        el administrador de objetos toma el código que haya aquí y lo
        ejecutara una vez en toda el tiempo de vida del objeto
        """
        pass

    @abstractmethod
    def update(self):
        """
        Aquí va la logica del objeto se ejecutará constantemente en un bucle.
        El administrador de objetos toma el código que haya aquí y lo
        ejecutara constantemente en el bucle principal
        """
        pass

    @abstractmethod
    def fixedUpdate(self):
        """
        Aquí se deben colocar únicamente código que se dibuje en pantalla.
        El administrador de objetos toma el código que haya aquí y lo
        ejecutara cada vez que haya un cambio que modifica la forma, color, tamaño, etc. del dibujo.
        """
        pass
