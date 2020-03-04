"""Databass for project"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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

    # reviews: a list of Review objects
    games = db.relationship("Game", secondary="reviews", backref="users")
    comments = db.relationship('Comment',
                               secondary='users_comments',
                               backref='users')

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
    igdb_id = db.Column(db.Integer)
    title = db.Column(db.String, nullable=False)
    console = db.Column(db.String)
    game_available_date = db.Column(db.String)
    genre = db.Column(db.String)
    url_image = db.Column(db.String)


class Review(db.Model):
    """Data model for ratings and reviews."""

    __tablename__ = "reviews"

    rating_id = db.Column(db.Integer,
                          primary_key=True,
                          autoincrement=True)
    
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    rating = db.Column(db.Integer)
    comment = db.Column(db.String)
    start_date = db.Column(db.DateTime)
    finish_date = db.Column(db.DateTime, nullable=True)

    user = db.relationship("User", backref="reviews")
    game = db.relationship("Game", backref="reviews")

class GroupFinder(db.Model)
    """Data model for LFG games."""

    __tablename__ = "groupfinders"

    lfg_id = db.Column(db.Integer,
                       primary_key=True,
                       autoincrement=True)

    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    comment = db.Column(db.String)
    lfg = db.Column(db.Boolean)
    
    user = db.relationship("User", backref='groupfinders')
    gmae = db.realtionship("Game", backref='groupfinders')


class Comment(db.Model):

    __tablename__ = "comments"

    comment_id = db.Column(db.Integer,
                           primary_key=True,
                           autoincrement=True)

    author_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)

    author = db.relationship('User', backref='comments_written')


class UserComment(db.Model):
    __tablename__ = 'users_comments'

    user_comment_id = db.Column(db.Integer,
                                primary_key=True,
                                autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.comment_id'))


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
