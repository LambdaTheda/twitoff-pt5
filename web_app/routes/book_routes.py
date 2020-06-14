from flask import Blueprint, jsonify, request, render_template #

from web_app.models import db, Book, parse_records #web_app is folder; models file is ~cls? (jish)

book_routes = Blueprint("book_routes", __name__)

# RETURN JSON RESPONSES
@book_routes.route("/books.json")
def list_book():
    # Similar to a SQLite (app user) query: SELECT * FROM books; asking to rtn all the books exist in DB
    book_records = Book.query.all() # replaces our previous hard-coded books list; list had no functionality jish thinks, so when u go to books/json, we can see smthng..(Not a list we rtn'd anythg from); books=...
    print(book_records)
    
    books = parse_records(book_records)
    return jsonify(books) # useful for updating a db (jon) to rtn obj
    
    '''
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ]
    '''
   

# RETURN HTML RESPONSES
@book_routes.route("/books") 
def list_books_for_humans():
    #books = [
    #    {"id": 1, "title": "Book 1"},
    #    {"id": 2, "title": "Book 2"},
    #    {"id": 3, "title": "Book 3"},
    #]
    book_records = Book.query.all()
    print(book_records)

    books = parse_records(book_records) # convert to JSON
    return render_template("books.html", message="Here's some books", books=books)

    '''
    book_records = Book.query.all()
    print(book_records)  # this and book_records.. line above replaces books = .. below as in the query for all books, as in the JSON version of this method above

    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},  
        {"id": 3, "title": "Book 3"},
    ]
    '''

    return render_template("books.html", message="Here's some bookS", books=books)  #render_template fcn looks for the templates folder and HTML file passed to it
  # https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/   ...FLASK method

# CREATE A NEW ROUTE THAT WHEN WE VISIT (the endpt) /books/new, it will render a pg w/a form on it
@book_routes.route("/books/new")  # this pg will allow user to enter data th@ we'll pass to the server th@ will b sorting the db 
def new_book():  # /books/new is our USER INPUT pg, FWDs input data to /books/create PAGE (method starts below @book_route.. line 57ish)
    return render_template("new_book.html")

# CATCHING DATA WE SENT FRoM OUR NEW/BOOK FORM through the REQUEST obj line 34 atm, prov by Flask pkg. Invoke request.form inside our ROUTE ..it'll b a dict-like obj
@book_routes.route("/books/create", methods=["POST"])

def create_book():
    print("FORM DATA:", dict(request.form))
    
    new_book = Book(title=request.form["book_title"], author_id=request.form["author_name"])
    db.session.add(new_book)
    db.session.commit()
    
    return jsonify({
       "message": "BOOK CREATED OK",
       "book": dict(request.form)
    })
    # flash(f"Book '{new_book.title}' created successfully!", "success") # "danger" "warning"
    # return redirect(f"/books")


''' #  ------------WHY NOT WORK!?---------

@book_routes.route("/books/create", methods=["POST"]) # this route will resp to a POST req, but not a GET req (by default).. methods=["GET", "POST"] if want both; OPTIONAL param
def create_book():
    print("FORM DATA:", dict(request.form) # CATCHes DATA WE SENT FRoM OUR NEW/BOOK FORM; configs our route to handle POST req (from pg's form?) & do smthg w/it 
    
    new_book=Book(title=request.form["title"], author_id=request.form["author_name"]) # initialize a new Book obj
    db.session.add(new_book)
    db.session.commit()           # db from our model class 

    return jsonify({
        "message": "BOOK CREATED OK (TODO)",
        "book": dict(request.form) # MUST IMPORT request from flask- so when our rte handles a req, we can capture the data (from the form) incl'd in th@ req
    })
    #flash(f"Book '{new_book.title}' created successfully!", "success")
    #return redirect(f"/books")
'''