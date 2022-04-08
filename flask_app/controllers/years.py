from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.models.user import User
from flask_app.models.rating import Rating 
from flask_app.models.album import Album
from flask_app.models.favArtist import favArtist
from flask_app.models.brookfield import Brookfield

@app.route('/years/2000')
def years_2000():

    if 'user_id' not in session:
        return redirect('/')

    data = {
        'id': session['user_id']
    }

    return render_template('years2000.html', userRatings = User.get_user_ratings(data), user = User.get_by_id(data))

@app.route('/years/1980')
def years_1980():

    if 'user_id' not in session:
        return redirect('/')

    data = {
        'id': session['user_id']
    }

    return render_template('years1980.html', userRatings = User.get_user_ratings(data), user = User.get_by_id(data))

@app.route('/years/1960')
def years_1960():

    if 'user_id' not in session:
        return redirect('/')

    data = {
        'id': session['user_id']
    }

    return render_template('years1960.html', userRatings = User.get_user_ratings(data), user = User.get_by_id(data))

@app.route('/years/1970')
def years_1970():

    if 'user_id' not in session:
        return redirect('/')

    data = {
        'id': session['user_id']
    }

    return render_template('years1970.html', userRatings = User.get_user_ratings(data), user = User.get_by_id(data))

@app.route('/years/1990')
def years_1990():

    if 'user_id' not in session:
        return redirect('/')

    data = {
        'id': session['user_id']
    }

    return render_template('years1990.html', userRatings = User.get_user_ratings(data), user = User.get_by_id(data))
    
@app.route('/years/2010')
def years_2010():

    if 'user_id' not in session:
        return redirect('/')

    data = {
        'id': session['user_id']
    }

    return render_template('years2010.html', userRatings = User.get_user_ratings(data), user = User.get_by_id(data))




