class Bicicleta:
    def __init__(self):  
        self.nomCliente = ""
        self.tipo = ""
        self.ID = ""
        self.tiemp = 0.0
        self.costo = 0.0

# Método para registrar datos de la bicicleta
    def registrar_bicicleta(self, nomCliente, tipo, ID, tiempo):  
        self.nomCliente = nomCliente
        self.tipo = tipo
        self.ID = ID
        self.tiemp = float(tiempo)  
        self.calcular_costo()

    def calcular_costo(self):
        tarifa_base = 5.0 
        if self.tipo == "deportiva":
            self.costo = self.tiemp * tarifa_base * 1.5
        else:
            self.costo = self.tiemp * tarifa_base

    def mostrar_datos_bicicleta(self):
        print("************** BIENVENIDOS ****************")
        print(f"El nombre del cliente es: {self.nomCliente}")
        print(f"Su número de documento es: {self.ID}")
        print(f"El tipo de bicicleta es: {self.tipo}")
        print(f"Las horas que la usó fueron: {self.tiemp}")
        print(f"El costo total es: ${self.costo:.2f}")
        print("*******************************************")

def recibirdatosbicicleta():
    print("********************* BIENVENIDOS **************************")
    nomCliente = input("Ingrese su nombre: ") 
    id = input("Ingrese sus documentos ")
    tipo = input("¿Que tipo de bicicleta? deportiva/tradicional: ")
    tiemp = input("¿Cuantas horas desea rentar la bicicleta? ") 

    return nomCliente, tipo, id, tiemp

# Crear una instancia de la clase Bicicleta
bicicleta1 = Bicicleta()

# Recibir datos del usuario y registrar la bicicleta
nomCliente, tipo, ID, tiempo = recibirdatosbicicleta()
bicicleta1.registrar_bicicleta(nomCliente, tipo, ID, tiempo)

# Mostrar los datos de la bicicleta registrada
bicicleta1.mostrar_datos_bicicleta()
