class Animal:
    def __init__(self, species_name: str):
        self.species_name = species_name


class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(species_name="Golden Retriver")
        self.name = name


my_dog = Dog("brown")

print(f"My dog's name is {my_dog.name} and he is a {my_dog.species_name}.")
