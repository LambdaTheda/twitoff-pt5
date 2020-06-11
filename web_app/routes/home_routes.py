# web_app/routes/home_routes.py

from flask import Blueprint #CSS or HTML styling class

home_routes = Blueprint("home_routes", __name__) # tell the Blueprint obj about this route, and then
                                                 # import the Blueprint obj, with __init__.py file.. (it goes there)

@home_routes.route("/")
def index():
    print("VISITING THE HOME PAGE") 
    x = 2 + 2
    return f"Hello World! {x}"

@home_routes.route("/about")
def about():
    #print("VISITING THE ABOUT PAGE")
    return "About me"  

'''
@app.route("/")
def index():
    #print("VISITING THE HOME PAGE")
    x = 2 + 2
    return f"Hello World! {x}"

@app.route("/about")
def about():
    print("VISITING THE ABOUT PAGE")
    return "About Me" 
'''