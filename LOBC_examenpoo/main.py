from vehiculos import motocicletas, Camion, Autos

# Instancias de vehículos
moto = motocicletas("Pulsar", "ns125", 2021, 50)
camion = Camion("Volvo", "xxx", 2020, 200, 18)
auto = Autos("Mercedes", "eqs", 2023, 100, "normal")

# Calcular precios vehiculos
print(f"Motocicleta: {moto.marca} {moto.modelo}, Año: {moto.anio}")
print(f"Precio de la motocicleta por 7 días: ${moto.calcular_precio(7)}")

print(f"Camión: {camion.marca} {camion.modelo}, Año: {camion.anio}, Capacidad de carga: {camion.capacidad_carga} ton.")
print(f"Precio del camión por 5 días: ${camion.calcular_precio(5)}")

print(f"Auto: {auto.marca} {auto.modelo}, Año: {auto.anio}, Tipo: {auto.tipo}")
print(f"Precio del auto por 2 días: ${auto.calcular_precio(2)}")
