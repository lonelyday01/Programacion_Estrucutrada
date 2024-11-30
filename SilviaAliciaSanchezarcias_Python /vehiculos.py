class Vehiculo():
    def __init__(self, **kwargs):
        self.brand = kwargs.get("brand")
        self.model = kwargs.get("model")
        self.year = kwargs.get("year")
        self.daily_fee = kwargs.get("daily_fee")
        self.matricula = kwargs.get("matricula")
        self.availability = True
    
    def calcular_precio(self, days):
        pass

    def rentar(self, availability):
        if self.availability == True:
            self.availability = False
            print("Felicidades! Has rentado este vehiculo!")
        else:
            print("Este vehiculo no se encuentra disponible en este momento.")

        return self.availability

    def devolver(self, availability):
        if self.availability == False:
            self.availability = True
            print("El vehiculo se ha deuelto en buen estado!")
        else:
            print("Este vehiculo no estaba siendo rentado")

        return self.availability
        

class Auto(Vehiculo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.style = kwargs.get("style")
        self.__total_fee = 0

    def calcular_precio(self, days, daily_fee, style):
        #Se le suma un cargo del seguro al daily fee y se multiplica por los dias de renta
        if style == "4X4":
            self.__total_fee = (daily_fee + 100) * days
        elif style == "Standard":
            self.__total_fee = (daily_fee + 76) * days
        elif style == "Delux":
            self.__total_fee = (daily_fee + 380) * days

        return self.__total_fee

class Motocicleta(Vehiculo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__total_fee = 0

    def calcular_precio(self, days, daily_fee):
        self.__total_fee = daily_fee * days

        return self.__total_fee

class Camion(Vehiculo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__total_fee = 0
        self.load_capacity = kwargs.get("load_capacity")

    def calcular_precio(self, days, daily_fee, load_capacity):
        self.__total_fee = 0
        #Se le suma un cargo del seguro al daily fee y se multiplica por los dias de renta
        if load_capacity <= 18:
            self.__total_fee = (daily_fee + 120) * days
        elif load_capacity >= 19 & load_capacity <= 27:
            self.__total_fee = (daily_fee + 230) * days
        elif load_capacity >=28 & load_capacity <= 32:
            self.__total_fee = (daily_fee + 380) * days

        return self.__total_fee