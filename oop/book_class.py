class Book:
    def __init__(self, title, author, year):
        # Constructor to initialize the book's attributes
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        # Destructor that prints a message when the object is deleted
        print(f"Deleting {self.title}")

    def __str__(self):
        # String representation of the object, for user-friendly display
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Official representation of the object, suitable for recreation of the object
        return f"Book('{self.title}', '{self.author}', {self.year})"
