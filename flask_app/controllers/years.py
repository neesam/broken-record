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

    return render_template('years2000.html', user = User.get_by_id(data))

@app.route('/years/1980')
def years_1980():

    if 'user_id' not in session:
        return redirect('/')

    data = {
        'id': session['user_id']
    }

    return render_template('years1980.html', user = User.get_by_id(data))