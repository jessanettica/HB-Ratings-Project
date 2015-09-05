"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the SQLite database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy() #db is an instance of SQLAlquemy


##############################################################################
# Model definitions

class User(db.Model): #User is a subclass of db.Model. 
    """User of rating website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    zipcode = db.Column(db.String(15), nullable=True)

    def similarity(self, other):
        """Return Pearson rating for user compared to other user,"""

        u_ratings = {}
        paired_ratings = []

        for r in self.ratings:
            u_r = u_ratings.get(r.movie_id)
            if u_r:
                paired ratings.append( (u_r.score, r.score) )

        if paired_ratings:
            return correlation.pearson(paired_ratings)

        else:
            return 0.0
    def predict_rating(self, movie):
        """Predict user's ratings of a movie"""

        other_ratings = movie.ratings


        print " ~~~~~~~ other ratings:", other_ratings

        similarities = [
            (self.similarity(r.user), r)
            for r in other_ratings
        ]
        similarities.sort(reverse=True)

        similarities = [(sim, r) for sim, r in similarities if sim > 0]

        if not similarities:
            return None

        numerator = sum([r.score * sim for sim, r in similarities])
        denominator = sum([sim for sim, r in similarities])

        return numerator/denominator

    @classmethod


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s email=%s>" % (self.user_id, self.email)


class Movie(db.Model):
    """ Movie database info """

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    title = db.Column(db.String(64), nullable = False)
    released_at = db.Column(db.DateTime)
    imdb_url = db.Column(db.String(64))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Movie movie_id=%s title=%s released_at=%s imdb_url=%s>" % (self.movie_id, self.title, self.released_at, self.imdb_url)


class Rating(db.Model):
    """Rating of a movie by a user."""


    __tablename__= "ratings"

    rating_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable = False)
    score = db.Column(db.Integer, nullable = False)

    #part2:define a relationship to user
    user = db.relationship("User", 
                            backref=db.backref("ratings", order_by=rating_id))


    #part2:Define relationship to movie
    movie= db.relationship("Movie",
                            backref=db.backref("ratings", order_by=rating_id))



    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Rating user_id=%s movie_id=%s score=%s>" % (self.user_id, self.movie_id, self.score)


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ratings.db'
    db.app = app
    db.init_app(app)
    # db.app.config["SQLALCHEMY_ECHO"] = True



if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."