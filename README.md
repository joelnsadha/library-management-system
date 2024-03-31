# Library Management System

This Python program implements a basic library management system. It allows users to create, store, and search for books within a library.

## Book Class

The `Book` class represents a basic book with attributes such as title, author, and publication year. It includes a method `book_info()` to display the details of the book.

## FictionBook Class

The `FictionBook` class is a subclass of `Book` and extends it to include additional information specific to fictional books, such as genre. It also overrides the `book_info()` method to display genre along with other book details.

## NonFictionBook Class

Similar to `FictionBook`, the `NonFictionBook` class is a subclass of `Book` and adds attributes relevant to non-fictional books, such as topic. It also overrides the `book_info()` method to include topic information in the book details.

## Library Class

The `Library` class represents a collection of books. It allows users to add books to the library and display all books stored. Additionally, it provides a method to search for books by author and display all books by authors matching the search query.

## How to Use

To use the library management system, create instances of `Book`, `FictionBook`, or `NonFictionBook` with relevant details. Then, create a `Library` object and add books to it using the `add_book()` method. Finally, search for books by author using the `search_authors()` method.

## Example

```python
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
```

## Technologies Used

- Python
- Object-Oriented Programming (OOP) principles

## Roadmap

In the future, additional features could be implemented such as:

- User authentication for accessing and modifying the library
- Ability to search for books by title or genre
- Integration with external databases for scalability

## Let's Connect

Feel free to reach out if you have any questions, suggestions, or would like to collaborate on enhancing this library management system!
