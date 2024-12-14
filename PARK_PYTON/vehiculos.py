#clase_principal
class Vehiculo:
    def __init__(self,marca,color):
      self.__marca = marca
      self.__color = color
    
    def CalcularPresio(self,presio):
        self.__presio = presio
        
#++++++++++++++++++++++++(Decoradores)++++++++++++++++++++++++++++++
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self,valor):
        self.__marca = valor
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,valor):
        self.__color = valor

    @property
    def presio(self):
        return self.__presio
     
    @color.setter
    def presio(self,presio):
        self.__presio = presio

    def __str__(self):
       return 'marca: '+ self.__marca + ', color: '+ self.__color 

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#sup_clases 
class Auto(Vehiculo):
   def __init__(self, marca, color,modelo,estilo):
       super().__init__(marca, color)
       self.__modelo = modelo
       self.__estilo = estilo

class Motosicleta(Vehiculo):
   def __init__(self, marca, color,modelo, motor):
       super().__init__(marca, color)
       self.__modelo = modelo
       self.__motor = motor

class Camion(Vehiculo):
   def __init__(self, marca, color,modelo,tipo):
       super().__init__(marca, color)
       self.__modelo = modelo
       self.__tipo = tipo
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
auto1 = Vehiculo("vmw","rojo")