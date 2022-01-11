class Book():
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.yearofrelease = year

class Paperbook(Book):
    def __init__(self, name, author, year,pages):
        self.pages = pages
        super().__init__(name, author, year)

    def showbook(self):
        return 'Name: {} Author: {} Year of release: {} Number of pages: {}'.format(self.name, self.author, self.yearofrelease ,self.pages)

class Ebook(Book):
    def __init__(self, name, author, year, file_size):
        self.size = file_size
        super().__init__(name, author, year)

    def showebook(self):
        return 'Name: {} Author: {} Year of release: {} File size: {}'.format(self.name, self.author, self.yearofrelease ,self.size)


ebook = Ebook('Harry Potter', 'JK Rowling', '2002', '250MB')

print(ebook.showebook())

book = Paperbook('Harry Potter', 'JK Rowling', '2002', '250')

print(book.showbook())
