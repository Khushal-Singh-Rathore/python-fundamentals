class Garage:
# __init__: This is your constructor.
# self: This represents the specific instance of the object.
    def __init__(self, owner_name:str):
        self.owner = owner_name
        self.cars = []

    def add_car(self, car_name:str):
        self.cars.append(car_name)
        print(f"Added {car_name} to {self.owner}'s garage.")

my_garage = Garage("Khushal")

my_garage.add_car("Seltos")

print(my_garage.cars)

# Term,         In your code,        Dart/Flutter equivalent

# Class,        class Garage:,       class Garage { ... }
# Constructor,  def __init__,        Garage(...)
# Property,     self.owner,          String owner;
# Method,       def add_car,         void addCar() { ... }
# Object,       my_garage,           var myGarage = Garage();