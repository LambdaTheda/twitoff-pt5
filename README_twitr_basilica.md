<!-- README_twitr_basilica.md unit 3 mod 2-->

# Installation

```sh  

git clone ________
cd twitoff-pt-5
```

# Setup 

```sh
FLASK_APP=web_app flask db init
FLASK_APP=web_app flask db migrate
FLASK_APP=web_app flask db upgrade
```
# Usage

 ```sh
#FLASK_APP=hello.py flask run

FLASK_APP=web_app flask run # "Hey Flask, the app you should run is in our 
                            # web_app directory, and Flasks looks for/finds 
                            # the __init__ file, the ENTRY PT into that 
                            # directory, and run the script, so it'll run our # app
 ```

 