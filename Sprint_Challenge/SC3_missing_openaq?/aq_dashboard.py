
from flask_sqlalchemy import SQLAlchemy
import ast, openaq.py, urllib, codecs, json
from collections import ChainMap
import urllib.parse

'''
We are pulling 100 observations of measurements of fine particulate matter (PM
2.5) in the Los Angeles area (in Chile, not the US). Note that this is
equivalent to making a request to this URL (you can even see the data in your
browser!):
https://api.openaq.org/v1/measurements?city=Los%20Angeles&parameter=pm25
'''

# Import (above) and set up the API object in your `aq_dashboard.py` file
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['ENV'] = 'production'

#DB is an instance of SQLAlchemy obj and we're passing it our app instance(?)
DB = SQLAlchemy(app)

def _finditem(obj, key):
    result = []
    if key in obj: return obj[key]
    for k, val  in obj.items():
        if isinstance(val, dict):
            item = _finditem(val, key)
            if item is not None:
                result.append(item)
                return result[0]

# Create a `Record` model 
class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return '<Time {}> --- <Value {}>'.format(self.datetime, self.value)
'''
# Create a `Record` model 
class CountryRecord(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return '<Time {}> --- <Value {}>'.format(self.datetime, self.value)
'''

@app.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    api = openaq.OpenAQ()
    status, body = api.measurements(city='Los Angeles', parameter='pm25')
    results = body['results']
    datetime_stuff = []

    for dictionary in results:
        print(type(dictionary))
        for key, value in dictionary.items():
         
            print(key, value)
            datetime_stuff_utc = _finditem(dictionary, "utc")
            datetime_stuff_value = _finditem(dictionary, "value")
            if not tuple([datetime_stuff_utc, datetime_stuff_value]) in datetime_stuff:
                datetime_stuff.append(tuple([datetime_stuff_utc, datetime_stuff_value]))
            continue
    for x, y in datetime_stuff:
        print(j,k)
        r = Record(datetime=x, value=y)
        DB.session.add(r)
    DB.session.commit()
    return 'Data refreshed!'

@app.route('/cities')
def retrive_cities():
    """Pull fresh data from Open AQ and replace existing data."""

    api = openaq.OpenAQ()
    status, body = api.cities()
    results = body['results']
    cities = []

    for dictionary in results:
        print(type(dictionary))
        for key, value in dictionary.items():
            print(key, value)
            city = _finditem(dictionary, "city")
            city = (city.encode('ascii', 'ignore')).decode("utf-8")
            if city not in cities and city != "unused":
                encoded = urllib.parse.quote_plus(city)
                cities.append({"city" : city, "urlencoded" : encoded})
            continue
 
    cities = [dict(t) for t in {tuple(d.items()) for d in cities}]

    return render_template('countries.html', title='Countries', data=cities)

@app.route('/')
def hello_world():

    data = Record.query.filter(Record.value > 10).all()
    print(data)
    display = []
    for d in data:
        print(d)
        print(d.value)
        display.append(tuple([d.datetime, d.value]))
    return render_template('base.html', title='Home', data=data)

    