class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        book = Book(title)
        self.books.append(book)
        print("Book added")

    def show_books(self):
        for book in self.books:
            status = "Available" if book.available else "Issued"
            print(book.title, "-", status)

    def lend_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print("Book issued")
                return
        print("Book not available")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print("Book returned")
                return


# Menu-driven program
lib = Library()

while True:
    print("\n1.Add Book 2.Show Books 3.Lend Book 4.Return Book 5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        title = input("Enter book name: ")
        lib.add_book(title)

    elif choice == 2:
        lib.show_books()

    elif choice == 3:
        title = input("Enter book to lend: ")
        lib.lend_book(title)

    elif choice == 4:
        title = input("Enter book to return: ")
        lib.return_book(title)

    elif choice == 5:
        break