from flask import Flask, render_template, request
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'changeme'


@app.route("/")
def index():
    return render_template("index.html")
    email = request.form['email']
    
    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
        return render_template('signup.html')
    else:
        return render_template('login.html')


@app.route("/comedy.html")
def comedy():
    return render_template("comedy.html")



@app.route("/action.html")
def action():
    return render_template("action.html")  



@app.route("/romance.html")
def romance():
    return render_template("romance.html")  



           

if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080, debug=True) 

app.run(debug=True)        