from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.models.genre import Genre
from flask_app.models.user import User

@app.route('/genres/alternative-emo')
def alternative_emo():

    data = {
        'id': session['user_id']
    }

    return render_template('genre_altEmo.html', artists = Genre.get_alt_emo(), user = User.get_by_id(data))

@app.route('/genres/pop-punk')
def pop_punk():

    data = {
        'id': session['user_id']
    }

    return render_template('genre_popPunk.html', artists = Genre.get_pop_punk(), user = User.get_by_id(data))

@app.route('/genres/midwest-emo')
def midwest_emo(): 

    data = {
        'id': session['user_id']
    }

    return render_template('genre_midEmo.html', artists = Genre.get_midwest_emo(), user = User.get_by_id(data))