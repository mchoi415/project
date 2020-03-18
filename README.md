# Game Stack
____
One of the first questions I want to ask when I meet someone is, "What video games do you play?" Depending on their answer, my next question is often, "Will you play with me?" 

Game Stack gives players a way to get both answers with ease.
 _____
 # About Me
 I graduated from San Francisco State University with a Bachelor of Science in Chemistry with the intention of becoming a pharmacist. However, after learning more about coding online, I realized that I had a passion for building things and solving  problems. I took the leap and immersed myself full-time in coding by joining Hackbright.
 
 My management experience at a small Japanese restaurant chain in San Francisco, where I worked for over 10 years, prepared me to think flexibly in a fast-paced environment. My passion for video games, which started when my grandmother first introduced me to the SNES (Super Nintendo Entertainment System), grew into a drive for achievement, and also exercised my ability to communicate with a team and perform under pressure.
 ____
 # Technologies
 
  - Python
  - JavaScript
  - Flask
  - Jinja
  - PostgreSQL
  - SQLAlchemy
  - Jquery
  - HTML
  - CSS
  - Bootstrap
  - IGDB API
 
_____

# How to install

##### Game Stack requires
 * Python3
 * [IGDB API Key](https://www.igdb.com/api)
 
Clone this repo
```
$ git clone https://github.com/mchoi415/project.git
```

Create and activate a virtual environment within the project folder
```
$ virtualenv env
$ source env/bin/activate
```

Install dependencies
```
$ pip install -r requirements.txt
```
Sign up to [IGDB](https://www.igdb.com/api) to get their API key
Save your API Key to a file called secrets.sh in this format:
```
export IGDB_API_KEY="YOUR_KEY_HERE"
```
Source your key
```
$ source secrets.sh
```
Set up your database
```
$ createdb project
$ python3 -i model.py
$ db.create_all()
```
Run the app
```
$ python3 server.py
```

On your internet browser, you can now access the webapp at:
```
http://localhost:5000/
```
_________
# Features
#### Landing Page
<img src="/static/images/landing-page.jpg">

You can log in, register, or even search for a game that you might be interested in.

#### Register
<img src="/static/images/register.jpg">

When you register, you will need to input a username, password, and email address. You can optionally provide are your Xbox, PSN, Nintendo, Steam, Twitch, and Discord tags to share on your profile. 

#### Login

<img src="/static/images/login.jpg">

If you are already a registered member, you can log in with the username and password provided at registration to go to your profile page.

#### Profile Page

<img src="/static/images/user-profile.jpg">

On your profile, you can easily see and access your game collection, LFG (Looking for Group) posts, a message board, your gamer tags, and other users to the right of your profile.

#### Game Collection

<img src="/static/images/game-collection.jpg">

This is an example of what a game collection would look like. You can add reviews, ratings, and your start and end dates for each game.

#### LFG (Looking for Group)

<img src="/static/images/lfg-posts.jpg">
<img src="/static/images/lfg-options.jpg">

On your profile, you will have the option to add, remove, or even update a current LFG post. These LFG posts will be shown on your profile and will also show up a user searches for that game.

#### Search for a Game

<img src="/static/images/search-game.jpg">

The search function allows you to get information about different games.

<img src="/static/images/search-results.jpg">

In the results page, you will be able to see the cover photo, release date, platform(s), and genre for the game. All LFG posts made for that game with also be displayed at bottom, along with a link to the profiles of the users who made each post.
_____
# Future Updates

  - Add more customization options for the user. For example, the ability to add a profile picture and a blurb about themselves.
  - Add a feature that will recommend other video games based on ratings and reviews the user has made in their game collection.
  - Add an optional dark mode
 ______

### Other information

  - This was a project made during my last 4 weeks at Hackbright Academy as a Full-Time Student in 2020.
 
 
 
 


