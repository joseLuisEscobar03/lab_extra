class Estudiante:
    def __init__(self, nombre, codigo, laboratorio1, laboratorio2, parcial):
        self.nombre = nombre
        self.codigo = codigo
        self.laboratorio1 = laboratorio1
        self.laboratorio2 = laboratorio2
        self.parcial = parcial

    def calcular_promedio(self):
        laboratorio1 = 0.30
        laboratorio2 = 0.30
        parcial = 0.40
        
        # Calculo del promedio del estudiante
        promedio = (self.laboratorio1 * laboratorio1) + \
                   (self.laboratorio2 * laboratorio2) + \
                   (self.parcial * parcial)
        return promedio

    def determinar_aprobacion(self):
        promedio = self.calcular_promedio()
        if promedio >= 60:
            return "Aprobado"
        else:
            return "Reprobado"

    def mostrar_resultados(self):
        promedio = self.calcular_promedio()
        resultado = self.determinar_aprobacion()
        print("*******************DATOS DEL ESTUDIANTE**************************") 
        print(f"Nombre: {self.nombre}")
        print(f"Código: {self.codigo}")
        print(f"Promedio Final: {promedio:.2f}")
        print(f"Resultado: {resultado}")

# Función para recibir los datos del estudiante
def recibir_datos_estudiante():
    print("*******************BIENVENIDOS**************************") 
    nombre = input("Ingrese el nombre del estudiante: ")
    codigo = input("Ingrese el código del estudiante: ")
    laboratorio1 = float(input("Ingrese la calificación del Laboratorio 1 (30%): "))
    laboratorio2 = float(input("Ingrese la calificación del Laboratorio 2 (30%): "))
    parcial = float(input("Ingrese la calificación del Parcial (40%): "))
    return Estudiante(nombre, codigo, laboratorio1, laboratorio2, parcial)

# Ejemplo de uso
estudiante1 = recibir_datos_estudiante()
estudiante1.mostrar_resultados()
