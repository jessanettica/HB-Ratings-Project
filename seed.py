"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from model import User, Rating, Movie, connect_to_db, db
from server import app
from datetime import datetime


def load_users():
    """Load users from u.user into database."""

    open_user_file = open('seed_data/u.user')

    for row in open_user_file:
        user_info_cell = row.rstrip().split("|")
        new_user_id = user_info_cell[0]
        user_age = user_info_cell[1]
        user_zipcode = user_info_cell[4]

        new_user = User(user_id=new_user_id, age=user_age, zipcode=user_zipcode)
    #new_user is the object. new_user is also an instance of the User class. 
        db.session.add(new_user)
    db.session.commit()
    print "Done loading users!"


def load_movies():
    """Load movies from u.item into database."""

    open_movie_file = open('seed_data/u.item')

    for row in open_movie_file:
        new_movie_cell = row.rstrip().split("|")
        if new_movie_cell[1] =='unknown':
            continue
        else:
            new_movie_id = new_movie_cell[0]
            new_title= new_movie_cell[1][:-7]
            #Not sure if every title actually has a year, if the title doesn't have a year are we cutting off the last 6 characters of the film's title?
            new_release_date = new_movie_cell[2]
            d=datetime.strptime(new_release_date, "%d-%b-%Y")
            new_url = new_movie_cell[4]
            new_movie = Movie(movie_id=new_movie_id, title=new_title, released_at=d, imdb_url=new_url)
            db.session.add(new_movie)
    db.session.commit()  
    print "Done loading movies! yay!"


def load_ratings():
    """Load ratings from u.data into database."""

    open_rating_file = open('seed_data/u.data')
    for row in open_rating_file:
        movie_info_cell = row.rstrip().split("\t")
        new_movie_id = movie_info_cell[1]
        new_user_id = movie_info_cell[0]
        new_score = movie_info_cell[2]

        new_rating = Rating(movie_id = new_movie_id, user_id=new_user_id, score=new_score)


        db.session.add(new_rating)
    db.session.commit()
    print "Done loading ratings! go go go!"

if __name__ == "__main__":
    connect_to_db(app) 

    load_users()
    load_movies()
    load_ratings()
