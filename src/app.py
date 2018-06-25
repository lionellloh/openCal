from flask import Flask, render_template, request, session
from models.user import User
from common.database import Database

app = Flask(__name__)

# Define the secret key
app.secret_key = "lionell"

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route("/")
def hello_method():
    return render_template("home.html")

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route("/login")
def login_template():

    return render_template("login.html")

@app.route("/register")
def register_template():

    return render_template("register.html")

@app.route("/auth/login", methods = ["POST"])
def login_user():

    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)

    else:
        session["email"] = None
        return render_template("profile.html", email = session["email"])

@app.route('/auth/register', methods = ['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']

    User.register(email, password)


    return render_template("profile.html", email = session["email"])

@app.route('/blogs/<string:user_id>')
@app.route('/blogs')
def user_blogs(user_id = None):
    if user_id is not None:
        user = User.get_by_id(user_id)

    else:
        user = User.get_by_email(session["email"])
        
    blogs = user.get_blogs()

    return render_template("user_blogs.html", blogs = blogs)

if __name__ == "__main__":
    app.run(port = 5000, debug = True)
