class Book:
    """
    Stores data about a book.
    Example: Title, Author, Year
    """

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def book_info(self):
        """
        Displays Title, Author, Year.
        """
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")


class FictionBook(Book):
    """
        Child class of Book. Stores information about
        Fictional book.
    Args:
        Book (_Book Object_): _Inherits from Book class_
    """

    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    def book_info(self):
        """
        Displays information about a fictional book
        """
        super().book_info()
        print(f"Genre: {self.genre}")


class NonFictionBook(Book):
    """
        Child class of Book. Stores information about
        non fictional book.
    Args:
        Book (_Book Object_): _Inherits from Book class_
    """

    def __init__(self, title, author, year, topic):
        super().__init__(title, author, year)
        self.topic = topic

    def book_info(self):
        """
        Displays information about non fictional book.
        """
        super().book_info()
        print(f"Topic: {self.topic}")


class Library:
    """
    Stores information about a library.
    """

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a book to library list.

        Args:
            book (_Object_): _Book Object_
        """
        self.books.append(book)

    def display_books(self):
        """
        Displays books in library.
        """
        for book in self.books:
            book.book_info()
            print()

    def search_authors(self, author):
        """_searches library for matching author \
            and stores author's books in list. \
                displays all books by author._

        Args:
            author (_string_): _string that matches author in book_
        """
        author_list = []
        for book in self.books:
            if author.lower() in book.author.lower():  # Check matching author
                author_list.append(book)  # Append matching author to search result list

        # Iterate over search results and call book_info method for each book
        if author_list:  # Check to ensure search results list is not empty
            for item in author_list:
                print(f"Books by authors that match '{author}':")
                print("----------------------------------------------------")
                print()
                item.book_info()
                print()
        else:  # No matching
            print("No authors matching '{author}'")


if __name__ == "__main__":
    # Create sample book objects
    harry_potter = FictionBook("Harry Potter", "J.K Rowling", 1991, "Adventure")
    simple = NonFictionBook("Why Simple Wins", "Lisa Bodell", 2016, "Productivity")

    # Create list of books
    all_books = [harry_potter, simple]

    # Create library object
    my_library = Library()

    # Loop over books and add to library
    for book in all_books:
        my_library.add_book(book)

    # Search library for author and return all books by matching author
    my_library.search_authors("Bodell")
