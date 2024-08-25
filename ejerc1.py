class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Orden:
    def __init__(self):
        self.productos = []
        self.total = 0.0

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.total += producto.precio

    def mostrar_resumen(self):
        print("Resumen de su orden:")
        for producto in self.productos:
            print(f"- {producto.nombre}: ${producto.precio:.2f}")
        print(f"Total a pagar: ${self.total:.2f}")

    def calcular_cambio(self, pago):
        if pago >= self.total:
            return pago - self.total
        else:
            return None

class Restaurante:
    def __init__(self):
        self.menu = {
            '1': Producto('Hamburguesa de res', 5.00),
            '2': Producto('Hamburguesa de pollo', 4.50),
            '3': Producto('Gaseosa pequeña', 1.50),
            '4': Producto('Gaseosa grande', 2.00)
        }

    def mostrar_menu(self):
        print("\nMenú:")
        for clave, producto in self.menu.items():
            print(f"{clave}. {producto.nombre} (${producto.precio:.2f})")
        print("5. Finalizar pedido")

    def tomar_orden(self):
        orden = Orden()

        while True:
            self.mostrar_menu()
            eleccion = input("Seleccione el número del producto que desea: ")

            if eleccion in self.menu:
                orden.agregar_producto(self.menu[eleccion])
            elif eleccion == '5':
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del menú.")

        return orden

def main():
    restaurante = Restaurante()
    print("BIENVENIDOS")

    orden = restaurante.tomar_orden()
    orden.mostrar_resumen()

    pago = float(input("¿Cuánto va a pagar? $"))
    cambio = orden.calcular_cambio(pago)

    if cambio is not None:
        print(f"Su cambio es: ${cambio:.2f}")
    else:
        print("El monto pagado no es suficiente.")

    print("Gracias por su compra. ¡Que tenga un buen día!")

if __name__ == "__main__":
    main()
