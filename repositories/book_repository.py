from db.run_sql import run_sql

from models.book import Book
from models.author import Author
from repositories import author_repository

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)

def save(book):
    sql = "INSERT INTO books (title, publisher, genre, author_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [book.title, book.publisher, book.genre, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id

def select_all():
    
    books =[]

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for book in results:
        author = author_repository.select(book['author_id'])
        book = Book(book['title'], book['genre'], book['publisher'], author, book['id'])
        books.append(book)
    return books

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values =[id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        author = author_repository.select(result['author_id'])
        book = Book(result['title'], result['genre'], result['publisher'], author, result['id'])
    return book

