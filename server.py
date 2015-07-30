"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session

from flask_debugtoolbar import DebugToolbarExtension

from model import User, Rating, Movie, connect_to_db, db



app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    

    return render_template("homepage.html")


@app.route("/users")
def user_list():
    """Show list of users."""

    users = User.query.all()
    return render_template("user_list.html", users=users)

@app.route("/login")
def login_page():
    """ Page to login """



    return render_template("login_page.html")

@app.route("/logout")
def logout_page():
    """ Page to logout """


    if 'user_username' not in session:
        return redirect('/login')
    
    if 'user_password' not in session:
        return redirect('/login')
    
    session.pop('user_username', None)
    session.pop('user_password', None)
    return render_template("logout_page.html")


@app.route("/login", methods=["POST"])
#change route to login so it is clear what the route is doing DONE
def submit_user_login():
    user_email = request.form.get("email")
    user_password = request.form.get("password")
    

    logged_in_user = User.query.filter(User.email== user_email).first()

    session['logged_in_user'] = logged_in_user.user_id
    
    flash("You have successfully logged in!")

    return redirect('/user_page')

@app.route("/user_page")

# query the database for user's name, age, zipcode, and the score and film title of the films they rated.

# This should link to user__info_page

# Include a button that return user to the previous page




if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()