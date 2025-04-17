planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
planet_list.append("Pluto")

rocky_planets = planet_list[0:4]
del planet_list[-1]

print(planet_list)

spacecraft = [
    ("Cassini", "Saturn", "Venus", "Jupiter"),
    ("Viking", "Mars"),
    ("Mariner 10", "Mercury", "Venus"),
    ("MESSENGER", "Mercury", "Venus"),
    ("Venera 1-16", "Venus"),
    ("Mariner 2", "Venus"),
    ("Mariner 5", "Venus"),
    ("Pioneer Venus 1 and 2", "Venus"),
    ("Vega 1 and 2", "Venus"),
    ("Galileo", "Venus", "Jupiter"),
    ("Magellan", "Venus"),
    ("Venus Express", "Venus"),
    ("Parker Solar Probe", "Venus"),
    ("Mariner 4", "Mars"),
    ("Mariner 6 and 7", "Mars"),
    ("Viking 1 and 2", "Mars"),
    ("Mars Pathfinder", "Mars"),
    ("Mars Odyssey", "Mars"),
    ("Spirit", "Mars"),
    ("Opportunity", "Mars"),
    ("Phoenix", "Mars"),
    ("Dawn", "Mars"),
    ("Curiosity", "Mars"),
    ("InSight", "Mars"),
    ("Perseverance", "Mars"),
    ("Pioneer 10 and 11", "Jupiter"),
    ("Voyager 1 and 2", "Jupiter", "Saturn"),
    ("Ulysses", "Jupiter"),
    ("New Horizons", "Jupiter", "Pluto"),
    ("Juno", "Jupiter"),
    ("Pioneer 11", "Saturn"),
    ("Voyager 2", "Uranus", "Neptune"),
]


def planet_space_craft_list(planet_list, spacecraft):
    for planet in planet_list:
        visitors = []
        for craft_tuple in spacecraft:

            craft, *visited_planets = craft_tuple
            if planet in visited_planets:
                visitors.append(craft)

        if visitors:
            print(f"{planet} has been visited by:")
            print("-" * 25)
            for visitor in visitors:
                print(visitor)
            print()


planet_space_craft_list(planet_list, spacecraft)
