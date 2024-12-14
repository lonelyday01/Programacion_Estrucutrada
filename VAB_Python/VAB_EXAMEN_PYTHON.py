# Clase base abstracta
class Vehiculo:
    # Constructor
    def __init__(self, precio=0.0, estado="disponible"):
        self._estado = estado  # Atributo protegido
        self._precio = precio  # Atributo protegido
    
    # Método para calcular precio (sobrescrito en subclases)
    def calcular_precio(self):
        raise NotImplementedError("Este método debe ser implementado por subclases")
    
    # Métodos para consultar y modificar estado
    def get_estado(self):
        return self._estado

    def set_estado(self, nuevo_estado):
        if nuevo_estado in ["disponible", "alquilado"]:
            self._estado = nuevo_estado
        else:
            print("Estado inválido")

    # Método para mostrar información del vehículo
    def mostrar_informacion(self):
        print(f"Estado: {self._estado}, Precio base: {self._precio}")


# Subclase Auto
class Auto(Vehiculo):
    def __init__(self, precio=0.0, estado="disponible", es_de_lujo=False):
        super().__init__(precio, estado)
        self.es_de_lujo = es_de_lujo  # Atributo adicional

    # Sobrescribir calcular_precio
    def calcular_precio(self):
        if self.es_de_lujo:
            return self._precio * 1.5  # Precio aumenta 50% si es de lujo
        return self._precio

    def mostrar_informacion(self):
        tipo = "de lujo" if self.es_de_lujo else "austero"
        print(f"Auto ({tipo}) - Estado: {self._estado}, Precio final: {self.calcular_precio()}")


# Subclase Camion
class Camion(Vehiculo):
    def __init__(self, precio=0.0, estado="disponible", capacidad_carga=0):
        super().__init__(precio, estado)
        self.capacidad_carga = capacidad_carga  # Atributo adicional

    # Sobrescribir calcular_precio
    def calcular_precio(self):
        return self._precio + (self.capacidad_carga * 10)  # Precio aumenta según la capacidad

    def mostrar_informacion(self):
        print(f"Camión - Estado: {self._estado}, Capacidad de carga: {self.capacidad_carga} toneladas, Precio final: {self.calcular_precio()}")


# Subclase Moto
class Moto(Vehiculo):
    def __init__(self, precio=0.0, estado="disponible", cilindrada=0):
        super().__init__(precio, estado)
        self.cilindrada = cilindrada  # Atributo adicional

    # Sobrescribir calcular_precio
    def calcular_precio(self):
        if self.cilindrada > 500:
            return self._precio * 1.2  # Precio aumenta 20% para cilindrada alta
        return self._precio

    def mostrar_informacion(self):
        print(f"Moto - Estado: {self._estado}, Cilindrada: {self.cilindrada} cc, Precio final: {self.calcular_precio()}")

# --- Crear objetos de las subclases ---

# Crear un auto de lujo
auto1 = Auto(precio=20000, estado="disponible", es_de_lujo=True)
auto1.mostrar_informacion()

# Crear un camión con capacidad de carga
camion1 = Camion(precio=30000, estado="disponible", capacidad_carga=10)
camion1.mostrar_informacion()

# Crear una moto con cilindrada
moto1 = Moto(precio=10000, estado="disponible", cilindrada=600)
moto1.mostrar_informacion()

# Modificar estado de los vehículos
auto1.set_estado("alquilado")
print(f"Nuevo estado del auto: {auto1.get_estado()}")
