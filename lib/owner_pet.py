


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        
    pass

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return Pet.all
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("Invalid pet type.")
        
    def get_sorted_pets(self):
        sorted_pets = sorted(Pet.all, key=lambda pet: pet.name)
        return sorted_pets
    pass