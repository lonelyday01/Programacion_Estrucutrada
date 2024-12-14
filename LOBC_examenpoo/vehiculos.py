# Clase base
class vehiculos:
    def __init__(self, marca, modelo, anio, precio_por_dia):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio_por_dia = precio_por_dia
        self.estado = "disponible"

    def calcular_precio(self, dias):
        pass

# Subclase Motocicletas
class motocicletas(vehiculos):
    def __init__(self, marca, modelo, anio, precio_por_dia):
        super().__init__(marca, modelo, anio, precio_por_dia)

    def calcular_precio(self, dias):
        return self.precio_por_dia * dias

# Subclase Camion
class Camion(vehiculos):
    def __init__(self, marca, modelo, anio, precio_por_dia, capacidad_carga):
        super().__init__(marca, modelo, anio, precio_por_dia)
        self.capacidad_carga = capacidad_carga

    def calcular_precio(self, dias):
        return self.precio_por_dia * dias * 1.2

# Subclase Autos
class Autos(vehiculos):
    def __init__(self, marca, modelo, anio, precio_por_dia, tipo):
        super().__init__(marca, modelo, anio, precio_por_dia)
        self.tipo = tipo

    def calcular_precio(self, dias):
        if self.tipo == "lujo":
            return self.precio_por_dia * dias * 1.3
        return self.precio_por_dia * dias
