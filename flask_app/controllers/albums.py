from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.models.rating import Rating
from flask_app.models.album import Album
from flask_app.models.twothousand import twoThousand
from flask_app.models.user import User
from flask_app.models.yearlyAlbums import yearlyAlbums

@app.route('/album/<id>')
def show_album(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_rating.html', user = User.get_by_id(userID), album = Album.get_by_id(data)) 

@app.route('/2000')
def twothousand():

    userID = {
        'id': session['user_id']
    }

    return render_template('twothousand.html', user = User.get_by_id(userID), albums = twoThousand.get_twothousand())

@app.route('/2000/<id>')
def twothousand_individual(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_twothousand.html', user = User.get_by_id(userID), album = twoThousand.get_twothousand_by_id(data)) 

@app.route('/2001')
def twothousandone():

    userID = {
        'id': session['user_id']
    }

    return render_template('twothousandone.html', user = User.get_by_id(userID), albums = yearlyAlbums.get_twothousandone())

@app.route('/2001/<id>')
def twothousandone_individual(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = yearlyAlbums.get_twothousandone_by_id(data))

@app.route('/2002')
def twothousandtwo():

    userID = {
        'id': session['user_id']
    }

    return render_template('twothousandtwo.html', user = User.get_by_id(userID), albums = yearlyAlbums.get_twothousandtwo())

@app.route('/2002/<id>')
def twothousandtwo_individual(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = yearlyAlbums.get_twothousandtwo_by_id(data))

@app.route('/2003')
def twothousandthree():

    userID = {
        'id': session['user_id']
    }

    return render_template('twothousandthree.html', user = User.get_by_id(userID), albums = yearlyAlbums.get_twothousandthree())

@app.route('/2003/<id>')
def twothousandthree_individual(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = yearlyAlbums.get_twothousandthree_by_id(data))

@app.route('/2004')
def twothousandfour():

    userID = {
        'id': session['user_id']
    }

    return render_template('twothousandfour.html', user = User.get_by_id(userID), albums = yearlyAlbums.get_twothousandfour())

@app.route('/2004/<id>')
def twothousandfour_individual(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = yearlyAlbums.get_twothousandfour_by_id(data))

@app.route('/2005')
def twothousandfive():

    userID = {
        'id': session['user_id']
    }

    return render_template('twothousandfive.html', user = User.get_by_id(userID), albums = yearlyAlbums.get_twothousandfive())

@app.route('/2005/<id>')
def twothousandfive_individual(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = yearlyAlbums.get_twothousandfive_by_id(data))

@app.route('/2006')
def twothousandsix():

    userID = {
        'id': session['user_id']
    }

    return render_template('twothousandsix.html', user = User.get_by_id(userID), albums = yearlyAlbums.get_twothousandsix())

@app.route('/2006/<id>')
def twothousandsix_individual(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = yearlyAlbums.get_twothousandsix_by_id(data))

@app.route('/2007')
def twothousandseven():

    userID = {
        'id': session['user_id']
    }

    return render_template('twothousandseven.html', user = User.get_by_id(userID), albums = yearlyAlbums.get_twothousandseven())

@app.route('/2007/<id>')
def twothousandseven_individual(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = yearlyAlbums.get_twothousandseven_by_id(data))