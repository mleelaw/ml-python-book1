movie_collection = [
    ("The Proposal", "Anne Fletcher", 2009),
    ("How To Losere A Guy In 10 Days", "Donald Petrie", 2003),
    ("Crazy Stupid Love", "Glenn Ficarra and John Requa", 2011),
    ("Hocus Pocus 2", "Anne Fletcher", 2022),
]


def add_movie(title, director, year):
    movie = (title, director, year)
    movie_collection.append(movie)
    print(f"{title} added to movie collection")


add_movie("La La Land", "Damien Chazelle", 2016)


def display_movies():
    print("My Fav Movie Collection")
    print("~" * 25)
    for title, director, year in movie_collection:
        print(f"{title} , {director} , {year}")


def search_by_director(director):

    director_list = []
    for movie in movie_collection:
        title, director_movie, year = movie
        if director_movie.lower() == director.lower():
            director_list.append(movie)
    return director_list


movies_by_anne = search_by_director("Anne Fletcher")
print("Movies by Anne Fletcher:")
print("~" * 25)
for title, director, year in movies_by_anne:
    print(f"Title: {title}, Year: {year}")


def remove_movie(title):
    for movie in movie_collection:
        title_movie, director, year = movie
        if title_movie.lower() == title.lower():
            movie_collection.remove(movie)
            print("movie removed!")
        return movie_collection


def update_movie(title, new_director, new_year):
    for i in range(len(movie_collection)):
        current_movie = movie_collection[i]

        current_title = current_movie[0]
        current_director = current_movie[1]
        current_year = current_movie[2]

        if current_title == title:
            updated_movie = (title, new_director, new_year)

            movie_collection[i] = updated_movie

            print(
                f"{title} new director is {new_director} and the new year is {new_year}"
            )

            return

    print(f"Movie '{title}' not found in collection.")


def sort_movies_by_year():

    def sort_key(movie):
        return movie[2]

    movie_collection.sort(key=sort_key)

    print("Movies Sorted by Year:")
    print("~" * 25)
    for title, director, year in movie_collection:
        print(f"{title} ({year}) directed by {director}")


sort_movies_by_year()

display_movies()

remove_movie("The Proposal")
display_movies()

update_movie("Crazy Stupid Love", "Me", 2025)

display_movies()
