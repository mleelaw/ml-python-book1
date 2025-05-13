# class Car:
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage

#     def __str__(self):
#         return f"The {self.color} car has {self.mileage} miles."

# car1 = Car("blue", 20000)
# car2 = Car("red", 30000)

# print(car1)
# print(car2)


# ----------------------------


# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

#     def speak(self, sound):
#         return f"{self.name} barks: {sound}"


# # ...


# class JackRussellTerrier(Dog):
#     def speak(self, sound="Arf"):
#         return super().speak(sound)


# class Dachshund(Dog):
#     pass


# class Bulldog(Dog):
#     pass


# miles = JackRussellTerrier("Miles", 4)
# buddy = Dachshund("Buddy", 9)
# jack = Bulldog("Jack", 3)
# jim = Bulldog("Jim", 5)


# print(miles.speak())

# print(jim.speak("woof"))

# ------------------------------------------------------


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


miles = GoldenRetriever("Miles", 4)

print(miles.speak())
