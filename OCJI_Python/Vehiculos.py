class Vehiculo():
    def __init__(self, **kwargs):
        self._marca = None
        self._modelo = None
        self._anio = None
        self.precio_dia = 0
        self.total_renta = 0
        self._estado = True
        self.dias = kwargs.get("dias", 0)

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        if isinstance(value, str) and value.strip():
            self._marca = value
        else:
            raise ValueError("Marca no válida")
    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        if isinstance(value, str) and value.strip():
            self._modelo = value
        else:
            raise ValueError("Modelo no válida")
    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, value):
        if isinstance(value, str) and value.strip():
            self._anio = value
        else:
            raise ValueError("Año no valido")        

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        if isinstance(value, str) and value.strip():
            self._estado = value
        else:
            raise ValueError("Estado no válido")

    def calcular_precio(self):
        self.total_renta = self.precio_dia * self.dias


class moto(Vehiculo):
    pass


class auto(Vehiculo):
    pass


class camion(Vehiculo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._capacidad = 0

    @property
    def capacidad(self):
        return self._capacidad

    @capacidad.setter
    def capacidad(self, value):
        if isinstance(value, int) and value > 0:
            self._capacidad = value
        else:
            raise ValueError("Capacidad no válida")

    def calcular_precio(self):
        if self.capacidad <= 18:
            self.total_renta = (self.precio_dia + 320) * self.dias
        elif self.capacidad <= 27:
            self.total_renta = (self.precio_dia + 530) * self.dias
        else:
            self.total_renta = (self.precio_dia + 845) * self.dias
