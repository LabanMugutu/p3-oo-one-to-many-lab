# lib/owner.py

class Pet:
    # Class variable containing all valid pet types
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    # Class variable that stores all Pet instances
    all = []

    def __init__(self, name, pet_type, owner=None):
        """
        Initialize a Pet instance with a name, pet type, and optional owner.
        Validate that the pet_type is one of the allowed types.
        """
        if pet_type not in Pet.PET_TYPES:
            raise Exception("pet_type must be one of the allowed types")

        self.name = name
        self.pet_type = pet_type

        # If an owner is provided, validate its type
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("owner must be an instance of Owner or None")

        self.owner = owner

        # Add this new pet instance to the class variable 'all'
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        """
        Initialize an Owner instance with a name.
        """
        self.name = name

    def pets(self):
        """
        Return a list of Pet instances that belong to this owner.
        """
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """
        Assign this owner to a Pet instance.
        Validate that pet is an instance of Pet.
        """
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet")

        pet.owner = self

    def get_sorted_pets(self):
        """
        Return a list of this owner's pets sorted by their names alphabetically.
        """
        return sorted(self.pets(), key=lambda pet: pet.name)
