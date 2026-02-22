from flask import Flask, render_template, request, jsonify
from library import Library, Book
import json

app = Flask(__name__)
library = Library()
sample_books = [
    {'title': '1984', 'author': 'George Orwell', 'checked_out': False},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'checked_out': False},
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'checked_out': False}
]

for book in sample_books:
    library.add_book(book)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(library.books)

@app.route('/api/add-book', methods=['POST'])
def add_book():
    data = request.json
    book = {'title': data.get('title'), 'author': data.get('author'), 'checked_out': False}
    library.add_book(book)
    return jsonify({'status': 'success', 'message': 'Book added successfully'}), 201

@app.route('/api/checkout/<int:book_id>', methods=['POST'])
def checkout_book(book_id):
    if 0 <= book_id < len(library.books):
        library.books[book_id]['checked_out'] = True
        return jsonify({'status': 'success', 'message': 'Book checked out'})
    return jsonify({'status': 'error', 'message': 'Book not found'}), 404

@app.route('/api/return/<int:book_id>', methods=['POST'])
def return_book(book_id):
    if 0 <= book_id < len(library.books):
        library.books[book_id]['checked_out'] = False
        return jsonify({'status': 'success', 'message': 'Book returned'})
    return jsonify({'status': 'error', 'message': 'Book not found'}), 404

@app.route('/api/stats', methods=['GET'])
def get_stats():
    total = len(library.books)
    checked_out = sum(1 for book in library.books if book['checked_out'])
    available = total - checked_out
    return jsonify({'total_books': total, 'checked_out': checked_out, 'available': available})

if __name__ == '__main__':
    app.run(debug=True, port=5000)