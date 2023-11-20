class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy += 5
        self.health += 10

    def play(self):
        self.health += 5

    def noise(self):
        print(f"{self.name} makes a sound!")

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print(f"{self.first_name} is walking {self.pet.name}.")
        self.pet.play()

    def feed(self):
        print(f"{self.first_name} is feeding {self.pet.name}.")
        self.pet.eat()

    def bathe(self):
        print(f"{self.first_name} is bathing {self.pet.name}.")
        self.pet.noise()

# Example :
if __name__ == "__main__":
#Create a Pet instance
    my_pet = Pet(name="Fluffy", type="Dog", tricks=["Sit", "Roll over"])

    #Create a Ninja instance and assign the pet to the ninja
    my_ninja = Ninja(first_name="Hiro", last_name="Yamato", treats=5, pet_food=10, pet=my_pet)

    #Perform actions with the Ninja and their Pet
    my_ninja.walk()
    my_ninja.feed()
    my_ninja.bathe()
