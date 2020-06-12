from flask import Blueprint, jsonify, request, render_template #

book_routes = Blueprint("book_routes", __name__)

# RETURN JSON RESPONSES
@book_routes.route("/books.json")
def list_book():
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ]
    return jsonify(books) # useful for updating a db (jon) to rtn obj

# RETURN HTML RESPONSES
@book_routes.route("/books")
def list_books_for_humans():
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ]
    return render_template("books.html", message="Here's some bookS", books=books)  #render_template fcn looks for the templates folder and HTML file passed to it
  # https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/   ...FLASK method

# CREATE A NEW ROUTE THAT WHEN WE VISIT (the endpt) /books/new, it will render a pg w/a form on it
@book_routes.route("/books/new")  # this pg will allow user to enter data th@ we'll pass to the server th@ will b sorting the db 
def new_book():
    return render_template("new_book.html")

# CATCHING DATA WE SENT FRoM OUR NEW/BOOK FORM through the REQUEST obj line 34 atm, prov by Flask pkg. Invoke request.form inside our ROUTE ..it'll b a dict-like obj
@book_routes.route("/books/create", methods=["POST"]) # this route will resp to a POST req, but not a GET req (by default).. methods=["GET", "POST"] if want both; OPTIONAL param
def create_book():
    print("FORM DATA:", dict(request.form)) # CATCHes DATA WE SENT FRoM OUR NEW/BOOK FORM; configs our rote to handle POST req f(rom pg's form?) & do smthg w/it 
    # todo: store in database
    return jsonify({
        "message": "BOOK CREATED OK (TODO)",
        "book": dict(request.form) # MUST IMPORT request from flask- so when our rte handles a req, we can capture the data (from the form) incl'd in th@ req
    })
    #flash(f"Book '{new_book.title}' created successfully!", "success")
    #return redirect(f"/books")
