class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def book_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")


class FictionBook(Book):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    def book_info(self):
        super().book_info()
        print(f"Genre: {self.genre}")


harry_potter = FictionBook("Harry Potter", "J.K Rowling", 1991, "Adventure")
harry_potter.book_info()
