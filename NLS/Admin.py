from colorama import Fore
from global_code import *


class Compare:
    def __init__(self, instance):
        self.instance = instance
        self.current_state = {}
        self.prev_state = {}

    def update(self):
        self.current_state[self.instance] = hash(str(self.instance.__dict__))
        if self.current_state != self.prev_state:
            self.prev_state[self.instance] = hash(str(self.instance.__dict__))
            return self.current_state
        else:
            pass


# Patron de diseño: Observer
class Admin:
    """
    Esta clase tiene una unica instancia la cual controla el momento de ejecución
    de los metodos de los objetos creados usando la interfaz GRAPHIC_OBJECT_TEMPLATE
    """
    __instance = None

    def __new__(cls):
        """
        objetos: guarda los objetos en una lista
        :type objetos: list
        current_state: Guarda el objeto key, y el valor es un identificador actual del objeto:type objetos: Diccionario
        prev_state: Guarda el objeto key, y el valor es un identificador anterior del objeto
        :type objetos: Diccionario
        """
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.objetos = []
            cls.__instance.current_state = {}
            cls.__instance.prev_state = {}
        return cls.__instance

    def add_obj(self, obj):
        # Guarda la instancia dada en la lista objetos
        self.objetos.append(obj)

    def update(self):
        # Este método regula el momento en que se ejecutan los métodos de los objetos en la lista objetos

        for instance in self.objetos:
            # Ejecuta una sola vez el método start del objeto
            if not instance.start_state:
                instance.start()
                instance.start_state = True
            """
            Se utiliza hash() en el conjunto de variables y valores del objeto para compararlos
            con los valores anteriores.
            Esto asegura que el objeto se dibujara una vez cada que se modifiquen los valores del objeto.
            """
            self.current_state[instance] = hash(instance.get_vars())

            if self.current_state != self.prev_state:
                instance.fixedUpdate()
                self.prev_state[instance] = hash(instance.get_vars())
                print(Fore.GREEN + "Update Log:" + Fore.RESET)
                print("Se produjo un cambio en: ", instance)
                print("Instancias", self.objetos)
            else:
                pass
            # El método update() del objeto se ejecuta continuamente en el bucle principal
            instance.update()
            instance.anim()


obj_admin = Admin()
