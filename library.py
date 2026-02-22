class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book['title']}' added to the library.")

    def remove_book(self, book_title):
        self.books = [book for book in self.books if book['title'] != book_title]
        print(f"Book '{book_title}' removed from the library.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("Books in Library:")
        for book in self.books:
            print(f"- {book['title']} by {book['author']}")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Example usage:
if __name__ == '__main__':
    library = Library()
    # Adding books
    library.add_book({'title': '1984', 'author': 'George Orwell'})
    library.add_book({'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'})
    # Listing books
    library.list_books()