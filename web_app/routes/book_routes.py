from flask import Blueprint, jsonify, request, render_template #

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/books.json")
def list_book():
    book = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ]
    return jsonify(books) # useful for updating a db (jon) to rtn obj

@book_routes.route("/books")
def list_books_for_humans():
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ]
    return render_template("books.html", message="Here's some book", books=books)  #render_template fcn looks for the templates folder and HTML file passed to it
  # https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/   ...FLASK method
