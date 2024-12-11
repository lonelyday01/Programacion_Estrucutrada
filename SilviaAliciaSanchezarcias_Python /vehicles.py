class Vehicle():
    def __init__(self, **kwargs):
        #Vehicle data
        self.__brand = None
        self.__model = None
        self.__year = None
        self.__license_plate = None
        #Rental information
        self.__daily_fee = 0
        self.__total_fee = 0
        self.__availability = True
        self.rental_days = kwargs.get("rental_days")

    #Setters and Getters for Vehicle data
    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, value):
        if isinstance(value, str) and value.strip():
            self.__brand = value
        else:
            raise ValueError("This brand is not valid")
        
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        if isinstance(value, str) and value.strip():
            self.__model = value
        else:
            raise ValueError("This model is not valid")
        
    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, value):
        if isinstance(value, int):
            self.__year = value
        else:
            raise ValueError("That year is invalid")
        
    @property
    def license_plate(self):
        return self.__license_plate
    
    @license_plate.setter
    def license_plate(self, value):
        if isinstance(value, str) and value.strip():
            self.__license_plate = value
        else:
            raise ValueError("That plate is invalid")
        
    #Setters and Getters for Rental information
    @property
    def daily_fee(self):
        return self.__daily_fee
    
    @daily_fee.setter
    def daily_fee(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self.__daily_fee = value
        else:
            raise ValueError("That fee is not valid")
        
    @property
    def total_fee(self):
        return self.__total_fee
    
    @total_fee.setter
    def total_fee(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self.__total_fee = value
        else:
            raise ValueError("That fee is not valid")
        
    @property
    def availability(self):
        return self.__availability
        
    def calculating_fee(self):
        pass

    #Rental methods
    def rent(self):
        if self.__availability:
            self.__availability = False
            print("The vehicle is on rent now.")
        else:
            print("This vehicle is being rented now.")

    def return_vehicle(self):
        if not self.__availability:
            self.__availability = True
            print("The vehicle has been returned successfully.")
        else:
            print("This vehicle has yet to be rented.")

class Car(Vehicle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__style = None

    @property
    def style(self):
        return self.__style
    
    @style.setter
    def style(self, value):
        if isinstance(value, str) and value.strip():
            self.__style = value
        else:
            raise ValueError("That style of car is invalid")

    def calculating_fee(self):
        match(self.__style):
            case("4X4"):
                self.total_fee = (self.daily_fee + 340) * self.rental_days
            case("Standard"):
                self.total_fee = (self.daily_fee + 275) * self.rental_days
            case("Delux"):
                self.total_fee = (self.daily_fee + 500) * self.rental_days
            case _:
                raise ValueError("That style of car is not valid")

        return self.total_fee

class Motorbike(Vehicle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculating_fee(self):
        self.total_fee = self.daily_fee * self.rental_days
        return self.total_fee
        

class Truck(Vehicle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__load_capacity = 0

    @property
    def load_capacity(self):
        return self.__load_capacity
    
    @load_capacity.setter
    def load_capacity(self, value):
        if isinstance(value, int) and  value > 0:
            self.__load_capacity = value
        else:
            raise ValueError("That load capacity is not valid")

    def calculating_fee(self):
        if self.__load_capacity <= 18:
            self.total_fee = (self.daily_fee + 320) * self.rental_days
        elif self.__load_capacity >= 19 and self.__load_capacity <= 27:
            self.total_fee = (self.daily_fee + 530) * self.rental_days
        elif self.__load_capacity >= 20:
            self.total_fee = (self.daily_fee + 845) * self.rental_days

        return self.total_fee