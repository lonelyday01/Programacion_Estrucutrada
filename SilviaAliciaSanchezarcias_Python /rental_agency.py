from objects import car1, bike1, truck1
#main running code
#Here goes the logic focused on the customer rental expierience
print("Welcome to the Vehicle Rental Agency")
print("What do you want to do? ")
action = int(input("1- Quote a vehicle rental \n2- Rent a vehicle \n3- Return a vehicle \n4- Nothing \n"))

match(action):
    case(1):
        print("What kind of vehicle do you want to get a rental quote for?")
        vehicle = int(input("1- Car \n2- Motorbike \n3-Truck \n"))
        match(vehicle):
            case(1):
                print("Right now we just have this car for rent: ")
                print(car1.brand, car1.model, car1.year)
                car1.rental_days = int(input("For how many days are you interested to rent this car? "))
                car1.calculating_fee()
                print(car1.total_fee)
            case(2):
                print("Right now we just have this bike for rent: ")
                print(bike1.brand, bike1.model, bike1.year)
                bike1.rental_days = int(input("For how many days are you interested to rent this bike? "))
                bike1.calculating_fee()
                print(bike1.total_fee)
            case(3):
                print("Right now we just have this truck for rent: ")
                print(truck1.brand, truck1.model, truck1.year)
                truck1.rental_days = int(input("For how many days are you interested to rent this truck? " ))
                truck1.calculating_fee()
                print(truck1.total_fee)
            case(_):
                raise ValueError("We don't rent horses, you nasty!!")
    case(2):
        print("What kind of vehicle do you want to rent?")
        vehicle = int(input("1- Car \n2- Motorbike \n3-Truck \n"))
        match(vehicle):
            case(1):
                print("Right now we just have this car for rent: ")
                print(car1.brand, car1.model, car1.year)
                rent = input("Do you want to rent this car? Yes/No \n")
                if rent == "Yes":
                    car1.rent()
                elif rent == "No":
                    print("Ok, bye!!")
                else:
                    print("Yes or No?!")
            case(2):
                print("Right now we just have this bike for rent: ")
                print(bike1.brand, bike1.model, bike1.year)
                rent = input("Do you want to rent this car? Yes/No \n")
                if rent == "Yes":
                    bike1.rent()
                elif rent == "No":
                    print("Ok, bye!!")
                else:
                    print("Yes or No?!")
            case(3):
                print("Right now we just have this truck for rent: ")
                print(truck1.brand, truck1.model, truck1.year)
                rent = input("Do you want to rent this truck? Yes/No ")
                if rent == "Yes":
                    truck1.rent()
                elif rent == "No":
                    print("Ok, bye!!")
                else:
                    raise ValueError("Yes or No?!")
            case(_):
                raise ValueError("What do you want a turtle for?!")
    case(3):
        print("What kind of vehicle do you want to return?")
        vehicle = int(input("1- Car \n2- Motorbike \n3-Truck \n"))
        match(vehicle):
            case(1):
                car1.return_vehicle()
            case(2):
                bike1.return_vehicle()
            case(3):
                truck1.return_vehicle()
            case(_):
                raise ValueError("We are not a shark shelter!! Return it to the sea!!")
    case(4):
        print("Bye!!")
    case(_):
        raise ValueError("What are you trying to do?!! Choose a number from 1 to 4!! It's not that hard!!!")