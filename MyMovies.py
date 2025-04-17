favorite_movies = []


def add_movie(movie):
    favorite_movies.append(movie)
    print(f"Movie '{movie}' added ")


def remove_movie(movie):
    if movie in favorite_movies:
        favorite_movies.remove(movie)
        print(f"Movie '{movie}' removed")
    else:
        print(f"Movie '{movie}' not found")


def display_movies():
    print("My Awesome Movie List")
    for movie in favorite_movies:
        print(f" {movie}")


def count_movies():
    for movie in favorite_movies:
        count = favorite_movies.count(movie)
        print(f"{count}")


def find_movie(movie):
    if movie in favorite_movies:
        print(f"{movie} found! ")
    else:
        print(f"{movie} not in movie list!")


def clear_movies():
    favorite_movies.clear()
    print(f"Movie List Cleared")


add_movie("Freaky Friday")

display_movies()

count_movies()

clear_movies()

display_movies()
