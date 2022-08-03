 from flask import Flask, render_template, request
 from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'changeme'


@app.route("/")
def index():
    return render_template("index.html")        
    name = request.form['name'] 
    Date = request.form['date'] 
    fav_color = request.form['fav_color']   
    fav_subject = request.form['fav_subject']   
    hobby = request.form['hobby']   
    ig = request.form['ig'] 
    phone_number = request.form['phone_number']
    select = select.form['select']
    save_to_database(name, Date, fav_color, fav_subject,hobby, ig,phone_number, select)          
    return render_template('search.html')
        
@app.route('/profile')
def profile():
    return render_template("profile.html")
    
@app.route("/profile2")
def profile2():
    return render_template('profile2.html',n = name,
    D =Date,
    f = fav_color,
    fa = fav_subject,
    h = hobby,
    ig = ig,
    num = phone_number,
    s = select

@app.route("/search")
def search():
          return render_template("search.html")

@app.route("/login")
def login():
     if request.method == 'GET':    
         return render_template("login.html")   
     else:
         return render_template("profile.html")

    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    print("Hey Im Here -----------------")
    if request.method == 'GET':
        print("Hello?------------")
        return render_template('signup.html')
    else:
        print("Heyyy Im Here 2----------------")
        username = request.form['username']
        password = request.form['password']
        print(username + "--------------------")
        sign_up(username, password)
        return render_template('login.html')

           

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True) 
        
