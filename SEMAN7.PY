# SEMANA 7
# Creamos la clase restaurante
class Restaurante:
    # Definimos el método __init__ (constructor)
    def __init__(self,nombre, mesa, comida,bebida,postre, precio):
        self.nombre = nombre #Atributo
        self.mesa = mesa
        self.comida = comida
        self.bebida = bebida
        self.postre = postre
        self.precio = precio
    def pagar(self): # Métoco pagar
        print("La persona ya canceló", self.precio) # Imprime el precio

    #Método Destructor
    def __del__(self):
        self.precio = 12 # Cambio del precio
        print("El objeto se ha eliminado de la memoria")    
# Instancia
persona_1 = Restaurante("María","3", "Sopa de pollo", "jugo de maracuyá", "galletas y leche", 15)
persona_1.pagar() # LLama al método pagar