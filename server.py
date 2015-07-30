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


@app.route("/submission", methods=["POST"])
#change route to login so it is clear what the route is doing
def submit_user_login():
    user_email = request.form.get("email")
    user_password = request.form.get("password")
    
    logged_in_user = User.query.filter(User.email== user_email).first()


    # query user from database using email
    #get user id
    #add user id to session session['user']= to what we get from 70
    print "HEEEEEEEEEEEEEEEEEELLLLLLLLLLLOOOOO", logged_in_user

#query database for user id and add id to session
    flash("You have successfully logged in!")

    return redirect('/')




if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()