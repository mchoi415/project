"""Game logger Website project"""

from jinja2 import StrictUndefined

from flask import(Flask, render_template, redirect, request, flash, session)
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Game, Review, connect_to_db, db

app = Flask(__name__)

app.secret_key = "secret"

app.jinja_env.undefined = StrictUndefined

@app.route('/update+profile', methods=['POST'])
def update_profile():
    """User update profile info."""

    twitch_tag = request.form.get('twitch')
    discord_tag = request.form.get('discord')
    xbox_tag = request.form.get('xbox')
    nintendo_tag = request.form.get('nintendo')
    psn_tag = request.form.get('psn')
    steam_tag = request.form.get('steam')

    #Figure out how to update new inputs from users!


    return redirect('/profile')

@app.route('/update+profile', methods=['GET'])
def profile_update():
    """Get update profile."""

    return render_template('updateProfile.html')


@app.route("/user+game+list")
def game_list():
    """Show User game list"""

    return render_template('gameList.html')


@app.route('/add+game', methods=['POST'])
def add_game():
    """Add game to database."""

    title = request.form.get('title')
    rating = request.form.get('rating')
    comment = request.form.get('comment')
    start_date = rquest.form.get('stat_date')
    end_date = request.form.get('end_date')


    new_review=Review(title=title,
                      rating=rating,
                      comment=comment,
                      start_date=start_date,
                      end_date=end_date)
                        
                        #Figure out how to get user id from logged in user!
                        #Figure out how to get game id from user input for title!
                     
                      # user_id=User.query.get('user')
                      
        
    db.session.add(new_review)
    db.session.commit()

    return redirect('/user+game+list')


@app.route("/add+game", methods=['GET'])
def get_game():
    """Get game info from user"""

    return render_template("addGame.html")

@app.route("/profile")
def show_profile():
    """show user's profile after login/register."""

    users = User.query.all()

    return render_template('profile.html', users=users)

@app.route("/register", methods=['POST'])
def register_user():
    """Register user into database."""

    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    twitch_tag = request.form.get('twitch')
    discord_tag = request.form.get('discord')
    xbox_tag = request.form.get('xbox')
    nintendo_tag = request.form.get('nintendo')
    psn_tag = request.form.get('psn')
    steam_tag = request.form.get('steam')



    user_email = User.query.filter_by(email=email).first()
    user_username = User.query.filter_by(username=username).first()

    if user_email == None:
        new_user=User(username=username,
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

        return redirect("/profile")


@app.route("/register", methods=['GET'])
def get_register():
    """Render template for register users."""

    return render_template("register.html")

@app.route("/login", methods=['GET'])
def get_login():
    """get login template"""

    return render_template("login.html")

@app.route("/login", methods=['POST'])
def user_login():
    """user login process."""

    username = request.form.get('username')
    password = request.form.get('password')

    user_username = User.query.filter_by(username=username).first()

    if user_username is None:
        flash('Incorrect username or password')
        return redirct('/login')

    else:
        if user_username.password == password:
            session['current_user'] = username
            flash(f'Logged in as {username}')
            
            return redirect("/profile")

        else:
            flash('Incorrect username or password')
            return redirect('/login')

@app.route("/")
def homepage():
    """Homepage"""

    return render_template("homepage.html")

if __name__=="__main__":

    app.debug= True

    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')