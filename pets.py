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
        # self refers to the specific instance of the class
        self.name = name
        self.species = species
        self.color = color

    def __str__(self):
        return f'{self.name} the {self.species}'

    def call(self):
        print(f'{self}, come here!')

    def fetch(self):
        return 'toy'

    def play(self, other):
        self.fetch()
        other.fetch()
        print(f'{self} is playing with {other}')


# build a specific instance of the class
# writing the name of the class followed by () invokes the __init__() 
# callping print() on an instance of a class invokes its __str__() method
# method for that class
stephens_dog = Pet("Breve", "Corgi", "sable")
orlandos_hedgehog = Pet("Ogbert", "hedgehog", ["black", "white", "brown"])
orlandos_hedgehog.call()
orlandos_hedgehog.play(stephens_dog)
