from datetime import datetime

class Vehicle:
    def __init__(self, brand, model, year, km, licence_plate, price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.km = km
        self.licence_plate = licence_plate
        self.price_per_day = price_per_day
        self.available = True

    def mark_as_available(self):
        self.available = True

    def mark_as_unavailable(self):
        self.available = False

    def update_km(self, km):
        self.update_km += km

class Customer:
    def __init__(self, first_name, last_name, dni, age, licence_number, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.dni = dni
        self.age = age
        self.licence_number = licence_number
        self.phone_number = phone_number
        self.email = email
        self.rental_history = [] # Inicializa el historial como una lista vacia


    def add_rental(self,rental):
        self.rental_history.append(rental)


class Rental:
    def __init__(self, customer, vehicle, start_date, finish_date):
        self.customer = customer
        self.vehicle = vehicle
        self.start_date = start_date
        self.finish_date = finish_date
        self.total_cost = self.calculate_cost()

    def calculate_cost(self):
        days = (self.finish_date - self.start_date).days
        return days * self.vehicle.price_per_day

    def finalize_rental(self):
        self.vehicle.mark_as_available()
        self.customer.add_rental(self)


def input_customer_data():
    print("Ingrese los datos del cliente:")
    first_name = input("Nombre: ")
    last_name = input("Apellido: ")
    dni = input("Identificación Oficial: ")
    age = input("Edad: ")
    licence_number = input("Número de licencia: ")
    phone_number = input("Número de teléfono: ")
    email = input("Correo electrónico: ")
    return Customer(first_name, last_name, dni, age, licence_number, phone_number, email)


class Agency:
    def __init__(self, name,address):
        self.name = name
        self.address = address
        self.vehicles = []
        self.customers = []
        self.rentals = []

    def add_car(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, licence_plate):
        self.vehicles = [v for v in self.vehicles if v.licence_plate != licence_plate]

    def add_customer(self,customer):
        self.customers.append(customer)

    def remove_customer(self,dni):
        self.customers = [c for c in self.customers if c.dni !=dni]

    def create_rental(self, customer_dni, vehicle_licence_plate, start_date, finish_date):
        customer = next((c for c in self.customers if c.dni == customer_dni), None)
        if not customer:
            raise Exception(f"Customer with DNI {customer_dni} not found.")

        vehicle = next((v for v in self.vehicles if v.licence_plate == vehicle_licence_plate), None)
        if not vehicle:
            raise Exception(f"Vehicle with licence plate {vehicle_licence_plate} not found.")

        if not vehicle.available:
            raise Exception(f"Car {vehicle_licence_plate} is not available.")

        rental = Rental(customer, vehicle, start_date, finish_date)
        self.rentals.append(rental)
        vehicle.mark_as_unavailable()
        return rental

    def finalize_rental(self,rental):
        rental.finalize_rental()
        self.rentals.remove(rental)

    def list_available_vehicles(self):
        return [v for v in self.vehicles if v.available]



# Código base importado
# Aquí puedes incluir las clases Vehicle, Customer, Rental, Agency

# Función para mostrar el menú y manejar la interacción

def main_menu():
    agency = Agency("Agencia mas cercana", "Boulevar de los marcianos 123 ")

    while True:
        print("- Agencia mas cercana -")
        print("1. Añadir vehículo")
        print("2. Añadir cliente")
        print("3. Registrar alquiler")
        print("4. Finalizar alquiler")
        print("5. Listar vehículos disponibles")
        print("6. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            add_vehicle(agency)
        elif choice == "2":
            add_customer(agency)
        elif choice == "3":
            register_rental(agency)
        elif choice == "4":
            finalize_rental(agency)
        elif choice == "5":
            list_available_vehicles(agency)
        elif choice == "6":
            print("Saliendo del sistema. ¡Gracias!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def add_vehicle(agency):
    print("--- Añadir Vehículo ---")
    brand = input("Marca: ")
    model = input("Modelo: ")
    year = int(input("Año: "))
    km = int(input("Kilometraje: "))
    licence_plate = input("Placa: ")
    price_per_day = float(input("Precio por día: "))

    vehicle = Vehicle(brand, model, year, km, licence_plate, price_per_day)
    agency.add_car(vehicle)
    print(f"Vehículo {brand} {model} añadido exitosamente.")


def add_customer(agency):
    print("-Añadir Cliente")
    customer = input_customer_data()
    agency.add_customer(customer)
    print(f"Cliente {customer.first_name} {customer.last_name} añadido exitosamente.")

def register_rental(agency):
    print("-Registrar Alquiler-")
    customer_dni = input("Identificacion del cliente: ")
    vehicle_licence_plate = input("Placa del vehículo: ")

    try:
        start_date = datetime.strptime(input("Fecha de inicio (YYYY-MM-DD): "), "%Y-%m-%d")
        finish_date = datetime.strptime(input("Fecha de fin (YYYY-MM-DD): "), "%Y-%m-%d")
        rental = agency.create_rental(customer_dni, vehicle_licence_plate, start_date, finish_date)
        rental_index = len(agency.rentals) - 1
        print(f"Alquiler registrado con éxito. Número de alquiler: {rental_index}. Costo total: {rental.total_cost}")
    except Exception as e:
        print(f"Error al registrar el alquiler: {e}")


def finalize_rental(agency):
    print("--- Finalizar Alquiler ---")
    if not agency.rentals:
        print("No hay alquileres activos para finalizar.")
        return

    print("Alquileres activos:")
    for index, rental in enumerate(agency.rentals):
        print(f"[{index}] Cliente: {rental.customer.first_name} {rental.customer.last_name}, Vehículo: {rental.vehicle.brand} {rental.vehicle.model}, Placa: {rental.vehicle.licence_plate}")

    rental_index = int(input("Ingrese el número del alquiler a finalizar: "))

    if 0 <= rental_index < len(agency.rentals):
        rental = agency.rentals[rental_index]
        agency.finalize_rental(rental)
        print("Alquiler finalizado exitosamente.")
    else:
        print("Índice de alquiler inválido.")


def list_available_vehicles(agency):
    print("--- Vehículos Disponibles ---")
    available_cars = agency.list_available_vehicles()
    if available_cars:
        for car in available_cars:
            print(f"{car.brand} {car.model} ({car.year}) - Placa: {car.licence_plate} - Precio por día: {car.price_per_day}")
    else:
        print("No hay vehículos disponibles.")

if __name__ == "__main__":
    main_menu()
