class Book:
    def __init__(self, title:str, author:str, isbn:str, year:int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}', {self.year})"

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

    def __eq__(self, other):
        return self.isbn==other.isbn

    def __lt__(self, other):
        return self.year<other.year

if __name__=="__main__":
    # Test it:
        book1 = Book("1984", "Orwell", "123", 1949)
        book2 = Book("1984", "Orwell", "123", 1949)
        print(book1)  # Should use __str__
        print(repr(book1))  # Should use __repr__
        print(book1 == book2)  # Should be True (same isbn)
        books = [book1, Book("Dune", "Herbert", "456", 1965)]
        print(sorted(books))  # Should sort by year