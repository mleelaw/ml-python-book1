library_catalog = [
    ("To Kill a Mockingbird", "Harper Lee", 1960),
    ("1984", "George Orwell", 1949),
    ("Pride and Prejudice", "Jane Austen", 1813),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925),
]


def display_books():
    print("Library Catalog:")
    for title, author, year in library_catalog:
        print(f"Title: {title}, Author: {author}, Year: {year}")


display_books()


def add_book(title, author, year):
    new_book = (title, author, year)
    library_catalog.append(new_book)
    print(f"Book '{title}' by {author} added to the catalog.")


add_book("The Catcher in the Rye", "J.D. Salinger", 1951)


def search_by_author(author):
    books_by_author = []
    for book in library_catalog:
        title, book_author, year = book
        if book_author.lower() == author.lower():
            books_by_author.append(book)
    return books_by_author


books_by_orwell = search_by_author("George Orwell")
print("Books by George Orwell:")
for title, author, year in books_by_orwell:
    print(f"Title: {title}, Year: {year}")
