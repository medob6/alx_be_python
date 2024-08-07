class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def __del__(self):
        print("Deleting (title of the book)")
    def __repr__(self) -> str:
        return f"Book('{self.title}', '{self.author}', {self.year})"
    def __str__(self) -> str:
        return f"{self.title} by {self.author}, published in {self.year}"