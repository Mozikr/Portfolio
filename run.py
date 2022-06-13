from flask import Flask, render_template, request
from AzureDB import AzureDB
from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github
import secrets
import os

app = Flask(__name__)
app.secret_key = secrets.token_hex(16) #generujemy sekretny klucz aplikacji
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1' #zezwalamy na polaczenie w lokalnym
 #srodowisku bez https

github_blueprint = make_github_blueprint(
 client_id="fbac0505ba404c110c0b", #tu wklek swoj wygenerowany id z github
 client_secret="e6a2acf3d72b0da596194f0dcad2dc47ff8ad628",#tu wklej swoj
 #wygenerowany client secret z github
)
app.register_blueprint(github_blueprint, url_prefix='/login')

app = Flask(__name__)
@app.route('/')
def hello():
 with AzureDB() as a:
    data = a.azureGetData()
 return render_template("result.html", data = data)
if __name__ == '__main__':
 app.run(debug=True)

 @app.route('/login')
 def github_login():
     if not github.authorized:
         return redirect(url_for('github.login'))
     else:
         account_info = github.get('/user')
         if account_info.ok:
             account_info_json = account_info.json()
             return render_template('inde.html')
         return '<h1>Request failed!</h1>'
if __name__ == "__main__":
    app.run(debug=True)