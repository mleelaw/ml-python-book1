from datetime import date


class Goat:
    def __init__(self, name, species, shift, food):
        # establishing properties of each animal with a default value
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.date_added = date.today()
        self.walking = True

    def __str__(self):
        return f"{self.name} the {self.species} is available to pet uring the {self.shift} shift"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
