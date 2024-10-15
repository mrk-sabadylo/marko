class Dog:
    def __init__(self, name, age, isHappy):
        self._name = name
        self._age = age
        self._isHappy = isHappy

    def set_data(self, dog_name, age, isHappy):
        self._name = dog_name
        self._age = age
        self._isHappy = isHappy

    def get_info(self):
        happiness = "happy" if self._isHappy else "sad"
        return f"{self._name}, {self._age} years old, {happiness}"

class DogOwner(Dog):
    def __init__(self, name, age, isHappy, owner_name):
        super().__init__(name, age, isHappy)
        self.owner_name = owner_name

    def get_owner_info(self):
        return f"Owner: {self.owner_name}, Dog: {self.get_info()}"

class Veterinarian:
    def __init__(self, vet_name, experience_years):
        self.vet_name = vet_name
        self.experience_years = experience_years

    def treat_dog(self, dog):
        dog.set_data(dog._name, dog._age, True)
        print(f"{self.vet_name} treated {dog._name}, now the dog is happy!")

class VetOwner(DogOwner, Veterinarian):
    def __init__(self, name, age, isHappy, owner_name, vet_name, experience_years):
        DogOwner.__init__(self, name, age, isHappy, owner_name)
        Veterinarian.__init__(self, vet_name, experience_years)

    def get_full_info(self):
        return f"Owner: {self.owner_name}, Vet: {self.vet_name}, Experience: {self.experience_years} years"

def demo():
    dog1 = Dog("Rex", 5, False)
    owner1 = DogOwner("Rex", 3, True, "Ivan")
    vet1 = Veterinarian("Kateryna", 10)
    vet_owner = VetOwner("Buddy", 6, False, "Olga", "Petro", 12)

    print(dog1.get_info())
    print(owner1.get_owner_info())
    vet1.treat_dog(dog1)
    print(vet_owner.get_full_info())
demo()
