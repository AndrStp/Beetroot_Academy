# Library

# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []

# Library class
# Methods:

# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and 
# adds the book to the books list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year

# All 3 classes must have a readable __repr__ and __str__ methods.
# Also, the book class should have a class variable which holds the amount of all existing books


class Author:
    
    def __init__(self, name: str, country: str, birthday: str) -> None:
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self) -> str:
        return f'Author: {self.name}'
    
    def __str__(self) -> str:
        return f'{self.name} is the author of {self.books}. The author is from {self.country}'


class Book:
    
    book_amount = 0

    def __init__(self, name: str, year: int, author: object) -> None:
        self.name = name
        self.year = year
        self.author = author
        Book.book_amount += 1

    def __repr__(self) -> str:
        return f'Book: {self.name}'
    
    def __str__(self) -> str:
        return f'{self.name} was published in {self.year} and its author is {self.author}'


class Library:
    
    def __init__(self, name) -> None:
        self.name = name
        self.books = []
        self.authors = []
    
    def __repr__(self) -> str:
        return f'{self.name}'
    
    def __str__(self) -> str:
        return f'Library: {self.name} has {len(self.books)} books'

    def new_book(self, name: str, year: int, author: object) -> object:
        """Returns an instance of Book class and adds the book 
        to the books list for the current library."""
        book = Book(name, year, author)
        self.books.append(book)

        if author not in self.authors:
            self.authors.append(author)

        author.books.append(book.name)
        return book
    
    def group_by_author(self, author: Author) -> list:
        """Returns a list of all books grouped by the specified author"""
        return [book for book in self.books if book.author is author]

    def group_by_year(self, year: int) -> list:
        """Returns a list of all the books grouped by the specified year"""
        return [book for book in self.books if book.year == year]


author_1 = Author('Taras', 'Ukraine', '23 May')
author_2 = Author('Bill', 'UK', '14 October')

print(author_1) # -> Taras is the author of []. The author is from Ukraine
print(author_2) # -> Bill is the author of []. The author is from UK

library = Library('Great Library')

book_name = 'Kniga_'
for i in range(1, 3):
    library.new_book(f'{book_name + str(i)}', 2012 + i, author_1)

book_name = 'Book_'
for i in range(1, 5):
    library.new_book(f'{book_name + str(i)}', 2012 + i, author_2)

print(Book.book_amount) # -> 6
print(library) # -> Library: Great Library has 6 books
print(library.books) # -> [Book: Kniga_1, Book: Kniga_2, Book: Book_1, Book: Book_2, Book: Book_3, Book: Book_4]
print(library.authors) # -> [Author: Taras, Author: Bill]

print(author_1) # -> Taras is the author of ['Kniga_1', 'Kniga_2']. The author is from Ukraine
print(author_2) # -> Bill is the author of ['Book_1', 'Book_2', 'Book_3', 'Book_4']. The author is from UK

print(library.group_by_author(author_1)) # -> [[Book: Kniga_1, Book: Kniga_2]
print(library.group_by_author(author_2)) # -> [Book: Book_1, Book: Book_2, Book: Book_3, Book: Book_4]

print(library.group_by_year(2013)) # -> [Book: Kniga_1, Book: Book_1]