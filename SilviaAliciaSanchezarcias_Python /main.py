from vehiculos import Vehiculo, Auto, Motocicleta, Camion

carro1 = Auto(brand = "Suzuki", model = "Jimny", year = "2024", daily_fee = 350.87, matricula = "ED8789", style = "4X4")

print(carro1.calcular_precio(4, carro1.daily_fee, carro1.style))

carro1.rentar(carro1.availability)

carro1.devolver(carro1.availability)

print(carro1.availability)

camion1 = Camion(brand = "Volvo", model = "FH16 Aero", year = "2020", daily_fee = 584.75, matricula = "JS9456", load_capacity = 20)

print(camion1.calcular_precio(7, camion1.daily_fee, camion1.load_capacity))

camion1.rentar(camion1.availability)

camion1.devolver(camion1.availability)

print(camion1.availability)

moto1 = Motocicleta(brand = "Yamaha", model = "Buchon", year = "2021", daily_fee = 93.50, matricula = "FW5613")

print(moto1.calcular_precio(3, moto1.daily_fee))

moto1.rentar(moto1.availability)

moto1.devolver(moto1.availability)

print(moto1.availability)