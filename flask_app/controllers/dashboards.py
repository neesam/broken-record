from flask_app.models.favartistalbum import favArtistAlbum
from flask_app import app
from flask import redirect, render_template, request, session, flash, jsonify
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.rating import Rating 
from flask_app.models.album import Album
from flask_app.models.favArtist import favArtist
from flask_app.models.brookfield import Brookfield
from flask_app.models.yearlyAlbums import yearlyAlbums
bcrypt = Bcrypt(app)

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }

    return render_template('dashboard.html', user = User.get_by_id(data), users = User.get_all_users(), userRatings = User.get_user_ratings(data), ratings = User.get_user_who_posted(), albums = yearlyAlbums.get_side_albums()) 

@app.route('/listening/submit', methods=['POST'])
def listening_submit():

    if 'user_id' not in session:
        return redirect('/logout')

    if not User.validate_listening(request.form):
        return redirect('/dashboard')
    print(request.form)
    
    User.save_listening(request.form)

    return redirect('/dashboard')

@app.route('/albums')
def albums():

    if 'user_id' not in session:
        return redirect('/')

    data = {
        'id': session['user_id']
    }

    return render_template('all_albums.html',  userRatings = User.get_user_ratings(data), user = User.get_by_id(data), albums = Album.get_all())


@app.route('/brookfield')
def brookfield():

    if 'user_id' not in session:
        return redirect('/')

    data = {
        'id': session['user_id']
    }

    return render_template('all_my_albums.html',  userRatings = User.get_user_ratings(data), user = User.get_by_id(data), brookfield = Brookfield.get_my_albums())

@app.route('/brookfield/<int:id>')
def brookfield_individual(id):

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }
    

    idData = {
        'id': id
    }

    return render_template('show_brookfield.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Brookfield.get_brookfield_by_id(idData))

@app.route('/years')
def years():

    if 'user_id' not in session:
        return redirect('/')

    data = {
        'id': session['user_id']
    }

    return render_template('years.html',  userRatings = User.get_user_ratings(data), user = User.get_by_id(data))

@app.route('/favartists')
def favartists():

    if 'user_id' not in session:
        return redirect('/')

    data = {
        'id': session['user_id']
    }

    return render_template('fav_artists.html',  userRatings = User.get_user_ratings(data), user = User.get_by_id(data), artists = favArtist.get_all())

@app.route('/favartists/<id>')
def individual_artist(id):

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    idData = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_artist.html',  userRatings = User.get_user_ratings(userID), artist = favArtist.get_by_id(idData), user = User.get_by_id(userID), albums = favArtist.get_artist_with_albums(idData), tracks = favArtist.get_artist_tracks(idData), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/favartists/albums/<id>')
def favartists_album(id):

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    idData = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_album.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = favArtistAlbum.get_by_id(idData), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/sundial')
def sundial():

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    return render_template('sundial.html', user = User.get_by_id(userID),  userRatings = User.get_user_ratings(userID), sundial = Album.get_sundial_albums())

@app.route('/sundial/<int:id>')
def sundial_individual(id):

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_sundial.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Brookfield.get_sundial_by_id(data))