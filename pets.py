'''a class is a blueprint for an object describing what 
attributes it will have and what it will be able to do'''

# attributes of pets
# num of legs
# hungry
# needs_attention
# amt of hair
# indoor/outdoor
# hair pattern
# color
# species
# name
# DOB 
# size
# name they answer to
# sex


class Pet():
    def __init__(self, name, species, color):
        self.name = name
        self.species = species
        self.color = color


# build a specific instance of the class
# writing the name of the class followed by () invokes the __init__() 
# method for that class
stephens_dog = Pet("Breve", "Corgi", "sable")
orlandos_hedgehog = Pet("Ogbert", "hedgehog", ["black", "white", "brown"])
print(stephens_dog.__dict__)
print(orlandos_hedgehog.__dict__)
