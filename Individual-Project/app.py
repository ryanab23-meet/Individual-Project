from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

Config = {

"iKey":"AIzaSyC9p3c98SMicj7eGggCmgBlOISHfEelHLY",

"authDomain": "project-1-86a2e.firebaseapp.com",

"projectId": "project-1-86a2e",

"storageBucket": "project-1-86a2e.appspot.com",

"messagingSenderId": "495478794645",

"appId":project-1-495478794645-web-9efdaebf683dde422cae9c",

"measurementId": "G-99674BFEP4",

 "databaseURL": "https://project1-20262-default-rtdb.firebaseio.com"

}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()


@app.route("/")
def index():
       return render_template("index.html")
       email = request.form['email']
       password = request.form['password']


@app.route('/signup',methods=['GET', 'POST']):
def signup():
if request.method == 'POST':
email = request.form['email']
password =request.form['password']
print(email, password)
# try:
login_session['user'] = auth.create_user_with_email_and_password(email, password)
user = {"name": request.form['name'], "email" : email}


@app.route("/comedy.html")
def comedy():
    return render_template("comedy.html")



@aupp.route("/action.html")
def action():
    return render_template("action.html")  



@app.route("/romance.html")
def romance():
    return render_template("romance.html")  



           

if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080, debug=True) 

app.run(debug=True)        