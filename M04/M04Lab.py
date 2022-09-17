'''
Application Name: M04Lab.py
Author: Ryan Alvey
Date: 09/17/2022
Description:

This application is an API created with Flask in Python. This API will 
allow the user to access a database containing information on various books.

Class Attributes:
    id: INT - a unique number identifying each book entry.
    book_name: This is the title of the book
    author: The author of the book
    publisher: The publisher of the book. 

There API includes route/methods to Create, Read all books, Read book by ID and Delete items in the database. 
'''

# Import Flask, request, and SQLAlchemy
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# Name the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lab_data.db'
# Make the connection to the database using SQLAlchemy
db = SQLAlchemy(app)

# Create main class for the database model with all of the book attributes
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80), nullable=False)

    # Define a string representation for the returned object
    def __repr__(self) -> str:
        return f'{self.id} - {self.book_name} - {self.author} - {self.publisher}'


# First route is the index page
@app.route('/')
def index():
    return 'More stuff with books and APIs'

# route to view all of the books in the database
@app.route('/books')
def get_books():
    books = Book.query.all()

    # This will iterate through the database and create an 'output' list containing each entry.
    output = []
    for book in books:
        book_info = {'title': book.book_name, 'author': book.author, 'publisher':book.publisher}
        output.append(book_info)

    return {'book':output}

# Route to allow you to look up a book by the book id
@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return{"title":book.book_name, "author": book.author, "publisher":book.publisher}

# Route to allow a user to post a new entry into the database from the API
@app.route('/books', methods=['POST'])
def add_book():
    book = Book(book_name=request.json['title'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id} 

# Route to allow the user to delete an entry by the book id
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "The book has been deleted successfully."}