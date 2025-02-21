class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  
    def pets(self):
        """Returns a list of all pets owned."""
        return self._pets
    def add_pet(self, pet):
        """Adds a pet to the owner's list, ensuring it is an instance of Pet."""
        if not isinstance(pet, Pet):
            raise Exception("Only instances of Pet can be added.")
        
        pet.owner = self 
        self._pets.append(pet)    
    def get_sorted_pets(self):
        """Returns a sorted list of pets by their names."""
        return sorted(self._pets, key=lambda pet: pet.name)
class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Must be one of: {Pet.PET_TYPES}")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = None  
        if owner:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of the Owner class.")
            self.owner = owner
            owner.pets().append(self) 
        Pet.all.append(self)