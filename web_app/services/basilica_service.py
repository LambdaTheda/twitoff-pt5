# web-app/services/basilica_service.py scripts can be run totally seperate from:  1) our web app  2) the db

import os

import basilica
from dotenv import load_dotenv

load_dotenv() # parse the .env file for environment variables

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY")

#with basilica.Connection('8dbd4037-f1a2-40e3-01ab-1f877bfad9b5') as connection: # connection is a basilica connection obj; "with" signifies we're interfacing w/a context mngr - he's not sure y
connection = basilica.Connection('8dbd4037-f1a2-40e3-01ab-1f877bfad9b5')         # connection is a basilica connection obj; "with" signifies we're interfacing w/a context mngr - he's not sure y

#one approach for not having the conn obj "hanging out," whence it will be immediately invoked upon importing from this file, can nest it inside a fcn and then import and invoke that fcn later to get the connection
#def basilica_api_client():  
#   return basilica.Connection(BASILICA_API_KEY)

if __name__ == "__main__": # will let us import the connection to some other script w/o asking for this app_making req 
    print(type(connection))
                                                                        # "...there's no closing of this, it's not like a db conn...maybe has some performance impact?
    sentences = ["Hello world!", "How are you?"]

    #embeddings = list(c.embed_sentences(sentences)
    embeddings = connection.embed_sentences(sentences)

    print(list(embeddings))# [[0.8556405305862427, ...], ...]
    #print(embeddings)..if we print # of items, we'll have 2, 1 for ea sent
    #print(type(embeddings))
