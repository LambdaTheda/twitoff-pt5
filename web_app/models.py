# web_app/models.py  FORMATS OUR TABLE, THIS PG IS USED BY OUR BOOK ROUTES, NEW BOOKS ROUTES, ..imports stuff in this pg to help our ROUTES PGS AND OUR FLASK WEB APP RUN
                    # WHOLE FILE PAGE IS A CLASS, IT'S THE CLASS DEF 

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#initialize instances of these classes we just imported 
db = SQLAlchemy()

migrate = Migrate()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True) # id will be auto-cr8d
    title = db.Column(db.String(128))
    author_id = db.Column(db.String(128))

    def __repr__(self): #determines how that inst should be displayed when u print or ask what datatype it is
        return f"<Book {self.id} {self.title}>"
    
def parse_records(database_records): #KEEPS APPENDING THE NEW BOOKS THAT WE ADD TO OUR INITIALLY EMPTY BOOKS LIST
    """
    A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON

    Param: database_records (a list of db.Model instances)

    Example: parse_records(User.query.all())

    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"},
        ]
    """
    parsed_records = [] # IS A list THAT IS INSIDE ALL DB RECS(ie ROWS)     In Python, what is difference between Array and List? | Edureka Community 
    for record in database_records:
        print(record)
        parsed_record = record.__dict__  # ?? https://www.tutorialspoint.com/What-does-built-in-class-attribute-dict-do-in-Python
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)   # APPENDs NEW books
    return parsed_records