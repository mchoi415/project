"""Databass for project"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
    """Data model for user. """
    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                         primary_key=True,
                         autoincrement=True)

    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    twitch_tag = db.Column(db.String)
    discord_tag= db.Column(db.String)
    xbox_tag = db.Column(db.String)
    nintendo_tag = db.Column(db.String)
    psn_tag = db.Column(db.String)
    steam_tag = db.Column(db.String)

    games = db.relationship("Game", secondary="reviews", backref="users")

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<User user_id={self.user_id} email={self.email}>"

class Game(db.Model):
    """Data model for a Game."""

    __tablename__ = "games"

    game_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True
                        )

    title = db.Column(db.String, nullable=False)
    console = db.Column(db.String, nullable=False)
    game_available_date = db.Column(db.DateTime)
    genre = db.Column(db.String)
    url_image = db.Column(db.String)


class Review(db.Model):
    """Data model for ratings and reviews."""

    __tablename__ = "reviews"

    rating_id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    rating = db.Column(db.Integer)
    comment = db.Column(db.String)
    start_date = db.Column(db.DateTime)
    finish_date = db.Column(db.DateTime)

    user = db.relationship("User", backref="reviews")
    game = db.relationship("Game", backref="reviews")



########################
#Helper functions

def connect_to_db(app):
    """Connect to the database with Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///project'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print("Connected to DB.")
