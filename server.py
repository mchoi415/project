"""Game logger Website project"""

from jinja2 import StrictUndefined

from flask import(Flask, render_template, redirect, request, flash, session)
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from model import User, Game, Review, connect_to_db, db

import seed

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
    if twitch_tag != "":
        user.twitch_tag=twitch_tag
    if discord_tag != "":
        user.discord_tag=discord_tag
    if xbox_tag != "":
        user.xbox_tag=xbox_tag
    if nintendo_tag != "":
        user.nintendo_tag=nintendo_tag
    if psn_tag != "":
        user.psn_tag=psn_tag
    if steam_tag != "":
        user.steam_tag=steam_tag
    db.session.commit()

    return redirect('/profile')


@app.route('/profile/update', methods=['GET'])
def profile_update():
    """Get update profile."""

    logged_user = session['current_user']
    user = User.query.filter_by(username=logged_user).first()

    return render_template('updateProfile.html', user=user)


@app.route('/game/<game_id>')
def show_game_info(game_id):
    """Show game information to user."""
    print(game_id)

    game = Game.query.filter_by(game_id=game_id).first()

    return render_template('gameInfo.html', game=game)


@app.route('/profile/list')
def game_list():
    """Show user's list"""
    
    logged_user = session['current_user']
    user = User.query.filter_by(username=logged_user).first()
    user_id = user.user_id
    game_reviews = Review.query.filter_by(user_id=user_id)
    game_reviews = game_reviews.join(Game)


    return render_template('gameList.html', game_reviews=game_reviews)


@app.route('/game/results', methods=['POST'])
def get_search_result():
    """Add search results into db."""

    current_id = request.form.get('title')
    print(current_id)

    if current_id == 'None':

        flash('Please search again')
        return redirect('/game/search')
    
    title = seed.get_game_by_id(current_id)
    print(title)


    current_game = Game.query.filter_by(game_id=current_id).first()

    if current_game is None:

        search_results = seed.get_game_by_id(current_id)[0]
        title = search_results['name']
        igdb_id = search_results['id']

        consoles = None
        game_available_dates = None
        genres = None
        url_image_id = None


        if 'platforms' in search_results.keys():
            console_ids = search_results['platforms']
            consoles = seed.get_console(console_ids)
          

        if 'release_dates' in search_results.keys():
            game_availabe_unixs = search_results['release_dates']
            game_available_dates = seed.get_released_date(game_availabe_unixs)

        if 'genres' in search_results.keys():
            genre_ids = search_results['genres']
            genres = seed.get_genre(genre_ids)
 
        if 'cover' in search_results.keys():
            cover_id = search_results['cover']
            url_image=seed.get_cover_url_by_id(igdb_id)


        # url_image = seed.get_image(url_image_id)


        new_game = Game(title=title,
                        igdb_id=igdb_id,
                        console=consoles,
                        #fix this
                        game_available_date=game_available_dates,
                        #fix this
                        genre=genres,
                        url_image=url_image)
        

        db.session.add(new_game)
        db.session.commit()

    session['title'] = title

    return redirect('/game/review')

@app.route('/game/results', methods=['GET'])
def show_search_result():
    """Show user search results and pick the right game."""

    title = session['title']

    search_results = seed.search_games(title)

    # for game in search_results:
    #     titles.append(game['name']) 

    # titles = [game['name'] for game in search_results[:5]]


    return render_template('searchResults.html',
                        titles=search_results)

    

@app.route('/game/search', methods=['POST'])
def add_game():
    """Check DB for game Add game into db if not there"""

    title = request.form.get('title')
    

    search_results = seed.search_games(title)
    #print game list on console
    print(search_results)

    # for search_result in search_results:
    # search_results = search_results[0]
    # title = search_results['name']
    session['title'] = title


    return redirect('/game/results')

@app.route('/game/search', methods=['GET'])
def get_game():
    """Load template for game checking"""

    return render_template('checkGame.html')

@app.route('/game/review', methods=['POST'])
def add_review():
    """Add game/review to database."""

    rating = request.form.get('rating')
    comment = request.form.get('comment')
    if comment == '':
        comment = None

    start_date = request.form.get('start_date')

    end_date = request.form.get('end_date')
    if end_date =='':
        end_date = None

    title = session['title']

    logged_user = session['current_user']

    #Need user ID from DB
    user = User.query.filter_by(username=logged_user).first()
    game = Game.query.filter_by(title=title).first()


    # logged_id = user_info.user_id

    #Need game ID from DB

    #Add new review into DB
    new_review = Review(rating=rating,
                        comment=comment,
                        start_date=start_date,
                        finish_date=end_date,
                        game=game
                        )
                        
                        #Figure out how to get user id from logged in user!
                        #Figure out how to get game id from user input for title!
                     
                      # user_id=User.query.get('user')
    user.reviews.append(new_review)
        
    db.session.add(new_review)
    db.session.commit()

    return redirect('/profile/list')


@app.route('/game/review', methods=['GET'])
def get_review():
    """Get game info from user"""

    title = session['title']
    # get all games from db
    # give list of gmes to jinja
    # in jinja make a selext with options that have game info
    return render_template('addGame.html', title=title)

@app.route('/profile/<username>/list')
def show_other_collection(username):
    """Show other user game collection."""

    user = User.query.filter_by(username=username).first()

    return render_template('otherGameList.html',
                           game_reviews=user.reviews,
                           username=username)

@app.route('/profile/<username>/messages')
def show_other_messages(username):
    """Show other user messages."""

    return render_template('otherMessages.html')

@app.route('/profile/<username>')
def show_other_profile(username):
    """Show another user's profile."""

    user = User.query.filter_by(username=username).first()

    return render_template('otherProfile.html', user=user)

@app.route('/profile/messages', methods=['POST'])
def upload_message():

    message = request.form.get('message')
    author = User.query.filter_by(username=session['username']).first()
    author_id = user.user_id


    new_comment = Comment(comment= message,
                          author_id=author_id)

    

    
    return redirect('/profile/messages')

@app.route('/profile/messages', methods=['GET'])
def show_message():
    """Render user's message board"""

    return render_template('messageBoard.html')

@app.route('/profile')
def show_profile():
    """Show user's profile after login/register."""
    
    logged_user = session['current_user']
    user = User.query.filter_by(username=logged_user).first()
    other_users = User.query.all()

    message = request.form.get('message')
    print(message)

    return render_template('profile.html', user=user, other_users=other_users)

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

        user_username = User.query.filter_by(username=username).first()
        session['current_user'] = username
        flash(f'Logged in as {username}')       
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

@app.route('/search/<igdb_game_id>')
def show_search_game_info(igdb_game_id):
    """"Show searched game info."""

    game_info = seed.get_game_by_id(igdb_game_id)[0]
    print(game_info)
    
    game_cover = None
    game_genre = None
    game_consoles = None
    release_dates = None

    if 'cover' in game_info.keys():
        game_cover = seed.get_cover_url_by_id(igdb_game_id)
    
    if 'genres' in game_info.keys():
        game_genre = seed.get_genre(game_info['genres'])

    if 'platforms' in game_info.keys():
        game_consoles = seed.get_console(game_info['platforms'])

    if 'release_dates' in game_info.keys():
        release_dates = seed.get_released_date(game_info['release_dates'])


    return render_template('gameSearchInfo.html',
        game_info=game_info,
        cover=game_cover,
        genre=game_genre,
        consoles=game_consoles,
        release_dates=release_dates)

@app.route('/search/results')
def results_game():
    """Show results of the user's (db) search."""

    search_results = seed.search_games(session['search'])    


    return render_template('gameSearchResults.html',
        search_results=search_results)


@app.route('/search', methods=['POST'])
def search_game():
    """Save (db) search game to pass into results."""

    search = request.form.get('search')
    print('from first page', search)
    session['search'] = search

    return redirect('/search/results')


@app.route('/search')
def search():
    """search game through igdb database for user."""

    return render_template('searchGame.html')

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