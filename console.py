import pdb
from models.book import Book
from models.author import Author
import  repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()



author1 = Author("JK", "Rowling")
author_repository.save(author1)

author2 = Author("Jesus", "Christ")
author_repository.save(author2)


book1 = Book("Philosopher Stone", "historical drama", "penguin", author1)
book_repository.save(book1)

book2 = Book("The Bible", "autobiography", "God", author2)
book_repository.save(book2)

