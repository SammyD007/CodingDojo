class Ninja:
    def __init__(self, firstName, lastName, treats, petFood, pet):
        self.firstName = firstName
        self.lastName = lastName
        self.treats = treats
        self.food = petFood
        self.pet = pet
    
    def walk(self):
        self.pet.play()
        return self
    
    def feed(self):
        self.pet.eat()
        return self
    
    def bathe(self):
        self.pet.noise()
        return self
