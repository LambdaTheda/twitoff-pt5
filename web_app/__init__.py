# web_app/__init__.py

from flask import Flask

from web_app.routes.home_routes import home_routes    # import our BLueprint obj from home_routes.py and register the Blueprint and 
                                                      # app.register_blueprint(homes_routes) tells our app (instance) about the routes                                                  # 2 step process allows us to move logically related routes into their own files to stay organized
from web_app.routes.book_routes import book_routes  

def create_app():
    app = Flask(__name__)                   # initialize new Flask app
    #app.register_blueprint(home_routes)    # tells our app (instance) about the routes
    app.register_blueprint(book_routes)     # REGISTER ONLY 1 ENDPT BC THEY WILL HAVE THE SAME APP ROUTES (jon)   
    return app
 
if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)    