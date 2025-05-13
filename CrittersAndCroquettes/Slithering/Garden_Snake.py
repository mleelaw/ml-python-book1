from datetime import date


class Garden_Snake:
    def __init__(self, name, species, food):
        # establishing properties of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"
