class Cliente:
    def __init__(self, nombre, cantidad_boletos, titulo_pelicula, hora_funcion, tipo_funcion, numero_sala, dia_funcion):
        self.nombre = nombre
        self.cantidad_boletos = int(cantidad_boletos)  
        self.titulo_pelicula = titulo_pelicula
        self.hora_funcion = hora_funcion
        self.tipo_funcion = tipo_funcion
        self.numero_sala = numero_sala
        self.dia_funcion = dia_funcion
    
    def calcular_total(self):
        precio_boleto = 5  
        total = self.cantidad_boletos * precio_boleto
        
        if self.dia_funcion.lower() == "miercoles" and self.cantidad_boletos >= 2:
            total = (self.cantidad_boletos // 2) * precio_boleto + (self.cantidad_boletos % 2) * precio_boleto
            
        return total
    
    def mostrar_datos_cliente(self): 
        total = self.calcular_total()  
        print("*******************DATOS DEL CLIENTE**************************") 
        print(f"Su nombre es: {self.nombre}") 
        print(f"Su cantidad de boletos es: {self.cantidad_boletos}") 
        print(f"El título de la película es: {self.titulo_pelicula}") 
        print(f"Su hora de la función es: {self.hora_funcion}") 
        print(f"Su tipo de función es: {self.tipo_funcion}") 
        print(f"Sala: {self.numero_sala}")
        print(f"Día de la función: {self.dia_funcion}")
        print(f"Total a pagar: ${total}") 
        print("**************************************************************") 

    
    def recibir_datos_cliente(): 
        print("********************* BIENVENIDOS **************************") 
        nombre = input("Ingrese su nombre: ") 
        cantidad_boletos = input("Ingrese cuántos boletos quiere: ") 
        titulo_pelicula = input("Ingrese el título de la película: ") 
        hora_funcion = input("Ingrese la hora de la función: ") 
        tipo_funcion = input("¿Qué tipo de función? 2D/3D: ") 
        numero_sala = input("Ingrese su número de sala: ") 
        dia_funcion = input("Ingrese su día de la función: ") 
        return Cliente(nombre, cantidad_boletos, titulo_pelicula, hora_funcion, tipo_funcion, numero_sala, dia_funcion)


cliente1 = Cliente.recibir_datos_cliente() 
cliente1.mostrar_datos_cliente() 
