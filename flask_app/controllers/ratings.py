from ..config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import redirect, render_template, request, session, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.rating import Rating
bcrypt = Bcrypt(app)

@app.route('/add-rating')
def add_rating():
    if 'user_id' not in session:
        return redirect('/login')
    
    data = {
        'id': session['user_id']
    }

    return render_template('create_rating.html', user = User.get_by_id(data))

@app.route('/create-rating', methods=['POST'])
def create_rating():

    if 'user_id' not in session:
        return redirect('/')

    data = {
        'stars': int(request.form['rating']),
        'artist': request.form['name'],
        'album': request.form['title'],
        'cover': request.form['cover'],
        'year': request.form['year'],
        'artist_link': request.form['artist_link'],
        'album_link': request.form['album_link'],
        'release_date': request.form['release_date'],
        'tracks': request.form['tracks'],
        'album_id': request.form['album_id'],
        'user_id': session['user_id'],
        'bunk': request.form['bunk'],
        'artist_id': request.form['artist_id']
    }

    Rating.save(data)
    
    return redirect('/dashboard')

@app.route('/destroy/<id>')
def delete_rating(id):

    if 'user_id' not in session:
        return redirect('/')

    data = {
        'id': id
    }

    userID = {
        'id': session['user_id']
    }

    Rating.destroy(data) 
    return redirect(f"/ratings/{session['user_id']}")

@app.route('/edit-rating', methods=['POST'])
def create_rating_yearly():

    if 'user_id' not in session:
        return redirect('/')

    data = {
        'stars': int(request.form['rating']),
        'rating_id': request.form['rating_id']
    }

    Rating.update_rating(data)
    
    return redirect('/dashboard')
    
@app.route('/ratings/<int:id>')
def user_ratings(id):

    if 'user_id' not in session:
        return redirect('/')

    data = {
        'id': id
    }

    sessionID = {
        'id': session['user_id']
    }

    return render_template('user_ratings.html', userRatings = User.get_user_ratings(data), user = User.get_by_id(sessionID), ratingProfile = User.get_by_id(data), users = User.get_all_users(), ratings = User.get_user_who_posted())