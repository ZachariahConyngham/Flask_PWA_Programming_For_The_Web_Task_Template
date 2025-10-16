from flask import Flask
import sqlite3
from flask import render_template
from flask import request
from flask import g
from flask import redirect
from flask import Blueprint
from flask import flash
import sqlite3 as sql
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


main = Blueprint('main', __name__)


import database_manager as dbHandler

app = Flask(__name__)



def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect('userdata')
        db.row_factory = sqlite3.Row
    return db

#db = get_db




#class User(db.Model):
#    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#    username = db.Column(db.String(1000), unique=True)
#    email = db.Column(db.String(100), unique=True)
#    password = db.Column(db.String(100))
#    Gender = db.Column(db.String(100))





@app.route('/index', methods=['GET'])
@app.route('/', methods=['POST', 'GET'])
def story():
    storydata = dbHandler.listStory()
    return render_template('/index.html', content=storydata)


@app.route("/fiction")
def index2():
    fictionstorydata = dbHandler.listFictionStory()
    return render_template('/fiction.html', content=fictionstorydata)


@app.route("/non-fiction")
def index3():
    nonfictionstorydata = dbHandler.listNonFictionStory()
    return render_template('/non-fiction.html', content=nonfictionstorydata)



@app.route('/login', methods=['POST', 'GET'])
def add():
    userdata = dbHandler.listuserdata()
    row_countemail = dbHandler.emailcheckuserdata()
    row_countuserID = dbHandler.userIDcheckuserdata()


    if request.method == "POST":
        username = request.form["username"]
        email = request.form["ename"]
        password = request.form["pname"]
        Gender = request.form["Gname"]

        #if email in userdata:
        #    return render_template("/login.html", error="Email already registered")
            
        #else:
        #    if username in userdata: 
        #        return render_template("/login.html", error="Username taken")
        #    else:  
        dbHandler.insertuserdata(username, email, password, Gender)
        
  


        return redirect("/upload")
    else:
        return render_template("/login.html", content=userdata)
#    {% if is_done=True %} <--enable_your_stories=True--> {% else %} <--enable_your_stories=False--> {% endif %}
#    <form action="/login" method="POST" class="box">




@app.route("/upload", methods=['POST','GET'])
def index5():
    usersstorydata = dbHandler.listusersstorydata()

    if request.method == "POST":
        clas = request.form["fname"]
        name = request.form["Sname"]
        author = request.form["Aname"]
        story = request.form["Story"]
        dbHandler.insertuserdata(name, clas, author, story)
        return redirect("/upload")
    else:
        return render_template('/upload.html', content=usersstorydata)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
