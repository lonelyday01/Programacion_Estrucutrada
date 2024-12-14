from Inventario2 import moto1, auto1, camion1

def mostrar_menu(opciones):
    print('Bienvenido al servicio de renta de vehiculos: \n¿Cual desea rentar hoy?')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Motocicleta', accion1),
        '2': ('Automovil', accion2),
        '3': ('Camion de carga', accion3),
        '4': ('Salir', salir)
    }

    generar_menu(opciones, '4')


def accion1():
    print('Has elegido rentar una motocicleta')
    print(moto1.marca, moto1.modelo, moto1.anio)
    moto1.dias = int(input("¿Cuantos dias va a rentar el vehiculo?"))
    moto1.calcular_precio()
    print(moto1.total_renta)

def accion2():
    print('Has elegido rentar un automovil')
    print(auto1.marca, auto1.modelo, auto1.anio)
    auto1.dias = int(input("¿Cuantos dias va a rentar el vehiculo?"))
    auto1.calcular_precio()
    print(auto1.total_renta)

def accion3():
    print('Has elegido rentar un camion de carga')
    print(camion1.marca, camion1.modelo, camion1.anio)
    camion1.dias = int(input("¿Cuantos dias va a rentar el vehiculo?"))
    camion1.calcular_precio()
    print(camion1.total_renta)

def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()