# web_app/__init__.py

from flask import Flask

from web_app.models import db, migrate                # flask db migrate cmd creates our db for us; IMPORT HERE BC WE'RE USING THEM HERE
from web_app.routes.home_routes import home_routes    # import our BLueprint obj from home_routes.py and register the Blueprint and                                                     # app.register_blueprint(homes_routes) tells our app (instance) about the routes                                                  # 2 step process allows us to move logically related routes into their own files to stay organized
from web_app.routes.book_routes import book_routes  

# using relative filepath: sqlite is a Protocol in the conn str /// (may be for the Main Version of it), then the path->to-> data file
DATABASE_URI = "sqlite:///twitoff_development_pt5.db" # FOR MACs(or Windows): cr8s db in root dir of yr repo; WILL IGNORE DB FROM VERSION CONTROL WITH GIT_IGNORE FILE

#HARD-CODED FILEPATHS:
#DATABASE_URI = "sqlite:////Users/Username/Desktop/your-repo-name/web_app_99.db" # using absolute filepath on Mac (recommended)
#DATABASE_URI = "sqlite:///C:\\Users\\Username\\Desktop\\your-repo-name\\web_app_99.db" # using absolute filepath on Windows (recommended) h/t: https://stackoverflow.com/a/19262231/670433

def create_app():
    app = Flask(__name__)                   # initialize new Flask app
    
    #ASSOC OUR DB CONN W/ OUR FLASK APP:
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(home_routes)     # tells our app (instance) about the routes
    app.register_blueprint(book_routes)     # REGISTER ONLY 1 ENDPT BC THEY WILL HAVE THE SAME APP ROUTES (jon)   
    
    return app
 
if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)    