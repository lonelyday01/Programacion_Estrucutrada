from vehicles import Vehicle, Car, Motorbike, Truck

#Initialization of Car object
car1 = Car(rental_days = 0)

#Setting the car information
car1.brand = "Suzuki"
car1.model = "Jimny"
car1.year = 2024
car1.license_plate = "ED8789"
#Setting the car rent information
car1.daily_fee = 350.84
car1.style = "4X4"

#Initialization of Motorbike object
bike1 = Motorbike(rental_days = 0)

#Setting Motorbike information
bike1.brand = "Harley Davidson"
bike1.model = "Low Rider S"
bike1.year = 2024
bike1.license_plate = "JS9456"
#Setting the bike rent information
bike1.daily_fee = 277.89

#Initialization of Truck object
truck1 = Truck(rental_days = 0)

#Setting Truck information
truck1.brand = "Volvo"
truck1.model = "FH16 Aero"
truck1.year = 2020
truck1.license_plate = "FW5613"
truck1.load_capacity = 20
#Setting Truck rent information
truck1.daily_fee = 587.75
