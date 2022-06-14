import pypyodbc
from flask import Flask, redirect, url_for, request, json
from flask import render_template
from flask import make_response, abort
from flask_dance.contrib.github import make_github_blueprint, github
import secrets
import os
import azurecred
import requests
from AzureDB import AzureDB

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
OAUTHLIB_INSECURE_TRANSPORT = 1
github_blueprint = make_github_blueprint(
    client_id = "504e0c51b40edbd3b",
    client_secret = "02e9f3afa14cd62115f02c545b1527c36ef2aa75"
)
app.register_blueprint(github_blueprint, url_prefix = '/github_login')

class AzureDB:


    dsn = 'DRIVER=' + azurecred.AZDBDRIVER + ';SERVER=tcp:' + azurecred.AZDBSERVER + ';PORT=1433;DATABASE = '+azurecred.AZDBNAME+';UID =w12'+';PWD =Haslo123'

def __init__(self):
     self.conn = pypyodbc.connect(self.dsn)
     self.cursor = self.conn.cursor()

def finalize(self):
     if self.conn:
            self.conn.close()

def __exit__(self, exc_type, exc_val, exc_tb):
     self.finalize()

def __enter__(self):
      return self

def azureGetData(self):
     try:
            self.cursor.execute("SELECT name,text from data")
            data = self.cursor.fetchall()
            return data
     except pypyodbc.DatabaseError as exception:
            print('Failed to execute query')
            print(exception)
            exit(1)

def azureGetData(self):
    try:
            self.cursor.execute("SELECT name, text from data")
            data = self.cursor.fetchall()
            return data
    except pypyodbc.DatabaseError as exception:
            print('Failed to execute query')
            print(exception)
            exit(1)

def azureAddData(self):
    self.cursor.execute("""INSERT INTO data (name, text) VALUES (?,?)""",
                            (request.form.get('cname'), request.form.get('comment')))
    self.conn.commit()



@app.route('/user/<username>', methods=['GET', 'POST'])
def show_user_profile(username):
    if request.method == 'POST':
        return 'HTTP POST for user %s with password %s' % (username, request.form['password'])
    else:
        return 'HTTP GET for user %s' % username

    @app.route('/error_denied')
    def error_denied():
        abort(401)

    @app.route('/error_internal')
    def error_internal():
        return render_template('template.html', name='ERROR 505'), 505

    @app.route('/error_not_found')
    def error_not_found():
        response = make_response(render_template('template.html', name='ERROR 404'), 404)

    response.headers['X-Something'] = 'A value'
    return response

@app.errorhandler(404)
def not_found_error(error):
        return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/ksiega_gosci')
def ksiega_gosci():
    return render_template('ksiega_gosci.html')

@app.route('/login')
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            account_info_json = account_info.json()
            return render_template('index.html')
    return '<h1>Request failed!</h1>'

def format_response(city):
    weather_key ='58c7d37c799707e478942f0e6d18697c'
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weather_key, "q": city, "units": "Metric"}
    response = requests.get(url, params = params)
    weather = response.json()
    name = weather['name']
    temp = weather['main']['temp']
    hum = weather['main']['humidity']
    pressure = weather['main']['pressure']
    wind = weather['wind']['speed']
    clouds = weather['clouds']['all']
    return "%s Temperature: %s°C Humidity: %s  Wind Speed: %s m/s  Pressure: %s hPa Cloudiness: %s"  %(name, temp, hum, wind, pressure, clouds)



@app.route('/', methods=['POST', 'GET'])
def home():
 if request.method == 'GET':
    return render_template('index.html')
 if request.method == 'POST':
    city = request.form['city']
 weather_data = format_response(city)
 return render_template('index.html', data=weather_data)
 return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)

