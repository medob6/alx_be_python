class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        self.page_count = page_count
        super().__init__(title, author)


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def list_books(self):
        for book in self._books:
            if isinstance(book, EBook):
                print(
                    f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB"
                )
            elif isinstance(book, PrintBook):
                print(
                    f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}"
                )
            elif isinstance(book, Book):
                print(f"Book: {book.title} by {book.author}")
