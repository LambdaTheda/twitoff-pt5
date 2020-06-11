# twitoff-pt5

# Installation

```sh  

git clone ________
cd twitoff-pt-5
```

# Setup 

```sh
pipenv install # ACTUALLY USED: from https://stackoverflow.com/questions/31512422/pip-install-failing-with-oserror-errno-13-permission-denied-on-directory
               # virtualenv .env
               # source .venv/bin/activate 
               # pip install (SQLAlchemy & Flask-Migrate pkgs)
```
# Usage

 ```sh
#FLASK_APP=hello.py flask run

FLASK_APP=web_app flask run # "Hey Flask, the app you should run is in our 
                            # web_app directory, and Flasks looks for/finds 
                            # the __init__ file, the ENTRY PT into that 
                            # directory, and run the script, so it'll run our # app
 ```

 