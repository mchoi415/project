"""Game logger Website project"""

from jinja2 import StrictUndefined

from flask import(Flask, render_template, redirect, request, flash, session)
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from model import User, Game, Review, connect_to_db, db

app = Flask(__name__)

app.secret_key = 'secret'

app.jinja_env.undefined = StrictUndefined

@app.route('/profile/update', methods=['POST'])
def update_profile():
    """Update profile info in DB."""

    twitch_tag = request.form.get('twitch')
    discord_tag = request.form.get('discord')
    xbox_tag = request.form.get('xbox')
    nintendo_tag = request.form.get('nintendo')
    psn_tag = request.form.get('psn')
    steam_tag = request.form.get('steam')

    logged_user = session['current_user']
    user = User.query.filter_by(username=logged_user).first()

    #Figure out how to update new inputs from users!
    
    user.twitch_tag=twitch_tag
    user.discord_tag=discord_tag
    user.xbox_tag=xbox_tag
    user.nintendo_tag=nintendo_tag
    user.psn_tag=psn_tag
    user.steam_tag=steam_tag
    db.session.commit()

    return redirect('/profile')


@app.route('/profile/update', methods=['GET'])
def profile_update():
    """Get update profile."""

    logged_user = session['current_user']
    user = User.query.filter_by(username=logged_user).first()

    return render_template('updateProfile.html', user=user)

@app.route('/profile/list')
def game_list():
    """Show user's list"""

    return render_template('gameList.html')


@app.route('/game/review', methods=['POST'])
def add_game():
    """Add game/review to database."""

    title = request.form.get('title')
    rating = request.form.get('rating')
    comment = request.form.get('comment')
    start_date = request.form.get('stat_date')
    end_date = request.form.get('end_date')

    # FIXME: get actual pk of game (instead of defaulting) to 1
    game_id = request.form.get('game_id', 1)

    logged_user = session['current_user']

    #Need user ID from DB
    user = User.query.get(logged_user)
    game = Game.query.get(game_id)
    # logged_id = user_info.user_id

    #Need game ID from DB

    #Add new review into DB
    new_review = Review(rating=rating,
                        comment=comment,
                        start_date=start_date,
                        finish_date=end_date,
                        user=user,
                        game=game)
                        
                        #Figure out how to get user id from logged in user!
                        #Figure out how to get game id from user input for title!
                     
                      # user_id=User.query.get('user')
                      
        
    db.session.add(new_review)
    db.session.commit()

    return redirect('/profile/list')


@app.route('/game/review', methods=['GET'])
def get_game():
    """Get game info from user"""

    # get all games from db
    # give list of gmes to jinja
    # in jinja make a selext with options that have game info
    return render_template('addGame.html')


@app.route('/profile')
def show_profile():
    """Show user's profile after login/register."""
    
    logged_user = session['current_user']
    user = User.query.filter_by(username=logged_user).first()

    return render_template('profile.html', user=user)

@app.route('/register', methods=['POST'])
def register_user():
    """Register user into database."""

    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    twitch_tag = request.form.get('twitch')
    discord_tag = request.form.get('discord')
    xbox_tag = request.form.get('xbox')
    nintendo_tag = request.form.get('nintendo')
    psn_tag = request.form.get('psn')
    steam_tag = request.form.get('steam')

    try:
        new_user = User(username=username,
                        email=email,
                        password=password,
                        twitch_tag=twitch_tag,
                        discord_tag=discord_tag,
                        xbox_tag=xbox_tag,
                        nintendo_tag=nintendo_tag,
                        psn_tag=psn_tag,
                        steam_tag=steam_tag)
        
        db.session.add(new_user)
        db.session.commit()
        return redirect('/profile')

    except IntegrityError:
        flash('A user with that email or username already exists :(')
        return redirect('/register')


@app.route('/register', methods=['GET'])
def get_register():
    """Render template for register users."""

    return render_template('register.html')


@app.route('/logout')
def user_logout():
    """User logout and direct to homepage."""

    del session['current_user']
    
    flash('Logged Out.')
    return redirect('/')


@app.route('/login', methods=['GET'])
def get_login():
    """get login template"""

    return render_template('login.html')


@app.route('/login', methods=['POST'])
def user_login():
    """user login process."""

    username = request.form.get('username')
    password = request.form.get('password')

    user_username = User.query.filter_by(username=username).first()

    if user_username is None:
        flash('Incorrect username or password')
        return redirect('/login')

    else:
        if user_username.password == password:
            session['current_user'] = username
            flash(f'Logged in as {username}')
            
            return redirect('/profile')

        else:
            flash('Incorrect username or password')
            return redirect('/login')


@app.route('/')
def homepage():
    """Homepage"""

    return render_template('homepage.html')


if __name__=='__main__':

    app.debug= True

    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')