"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from model import User, Rating, Movie, connect_to_db, db
from server import app


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





def load_movies():
    """Load movies from u.item into database."""
    
    pass

def load_ratings():
    """Load ratings from u.data into database."""

    pass

if __name__ == "__main__":
    connect_to_db(app)

    load_users()
    # load_movies()
    # load_ratings()
