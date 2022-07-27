from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.book_repository as book_repository

def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)

def save(author):
    sql = "INSERT INTO authors (first_name, last_name) VALUES (%s, %s) RETURNING id"
    values = [author.first_name, author.last_name]
    results =run_sql(sql, values)
    id = results[0]['id']
    author.id = id

def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        author = Author(result['first_name'], result['last_name'], result['id'])
    return author