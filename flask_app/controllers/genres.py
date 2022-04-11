from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.models.genre import Genre
from flask_app.models.user import User
from flask_app.models.allGenre import allGenre
from flask_app.models.SOS2 import SOS2
from flask_app.models.sosGenre import SOSGenre

@app.route('/genres/alternative-emo')
def alternative_emo():

    data = {
        'id': session['user_id']
    }

    return render_template('genre_altEmo.html',  userRatings = User.get_user_ratings(data), artists = Genre.get_alt_emo(), user = User.get_by_id(data))

@app.route('/genres/pop-punk')
def pop_punk():

    data = {
        'id': session['user_id']
    }

    return render_template('genre_popPunk.html', artists = Genre.get_pop_punk(),  userRatings = User.get_user_ratings(data), user = User.get_by_id(data))

@app.route('/genres/midwest-emo')
def midwest_emo(): 

    data = {
        'id': session['user_id']
    }

    return render_template('genre_midEmo.html', userRatings = User.get_user_ratings(data), artists = Genre.get_midwest_emo(), user = User.get_by_id(data))

@app.route('/genres/indie-rock')
def indie_rock():

    data = {
        'id': session['user_id']
    }

    return render_template('genre_indieRock.html', userRatings = User.get_user_ratings(data), artists = Genre.get_indie_rock(), user = User.get_by_id(data))

@app.route('/genres/glitchcore')
def glitchcore():

    data = {
        'id': session['user_id']
    }

    return render_template('genre_glitchcore.html', userRatings = User.get_user_ratings(data), artists = Genre.get_glitchcore(), user = User.get_by_id(data))

@app.route('/genres/math-rock')
def mathrock():

    data = {
        'id': session['user_id']
    }

    return render_template('genre_mathRock.html', userRatings = User.get_user_ratings(data), artists = Genre.get_mathrock(), user = User.get_by_id(data))

@app.route('/genres/plugg')
def plugg():

    data = {
        'id': session['user_id']
    }

    return render_template('genre_plugg.html', userRatings = User.get_user_ratings(data), artists = Genre.get_plugg(), user = User.get_by_id(data))

@app.route('/genres/vaporwave')
def vaporwave():

    data = {
        'id': session['user_id']
    }

    return render_template('genre_vaporwave.html', userRatings = User.get_user_ratings(data), artists = Genre.get_vaporwave(), user = User.get_by_id(data))

@app.route('/sos/synthpop')
def sos_synthpop():

    data = {
        'id': session['user_id']
    }

    return render_template('s_o_s_synthpop.html', userRatings = User.get_user_ratings(data), songs = SOS2.get_songs_from_synthpop(), user = User.get_by_id(data))

@app.route('/sos/<id>')
def solo_altemo(id):

    albumID = {
        'id': id
    } 

    data = {
        'id': session['user_id']
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_sos.html', userRatings = User.get_user_ratings(data), album = SOS2.get_sos_by_id(albumID), user = User.get_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/sos')
def sos():

    data = {
        'id': session['user_id']
    }

    return render_template('sos.html', userRatings = User.get_user_ratings(data), playlists = SOSGenre.get_all(), user = User.get_by_id(data))
    
@app.route('/sos/electro')
def sos_electro():

    data = {
        'id': session['user_id']
    }

    return render_template('s_o_s_electro.html', userRatings = User.get_user_ratings(data), songs = SOS2.get_songs_from_electro(), user = User.get_by_id(data))

@app.route('/sos/midwest-emo')
def sos_midwest(): 

    data = {
        'id': session['user_id']
    }

    return render_template('s_o_s_midwestemo.html', userRatings = User.get_user_ratings(data), songs = SOS2.get_all_midwest(), user = User.get_by_id(data))

# @app.route('/sos/italian-disco')
# def sos_italiandisco(): 

#     data = {
#         'id': session['user_id'] 
#     }

#     return render_template('s_o_s_italiandisco.html', userRatings = User.get_user_ratings(data), songs = SOS2.get_all_italiandisco(), user = User.get_by_id(data))

@app.route('/sos/pop-punk')
def sos_poppunk(): 

    data = {
        'id': session['user_id'] 
    }

    return render_template('s_o_s_poppunk.html', userRatings = User.get_user_ratings(data), songs = SOS2.get_all_poppunk(), user = User.get_by_id(data))

@app.route('/sos/instrumental-post-rock') 
def sos_instrumentalpostrock(): 

    data = {
        'id': session['user_id']
    }

    return render_template('s_o_s_instrumentalpostrock.html', userRatings = User.get_user_ratings(data), songs = SOS2.get_all_instrumentalpostrock(), user = User.get_by_id(data))

@app.route('/electro/<id>')
def solo_electro(id):

    albumID = {
        'id': id
    }

    data = {
        'id': session['user_id']
    }

    return render_template('show_old_sos.html', userRatings = User.get_user_ratings(data), album = SOS2.get_electro_by_id(albumID), user = User.get_by_id(data))
    
@app.route('/sos/alternative-emo')
def sos_altemo():

    data = {
        'id': session['user_id']
    }

    return render_template('s_o_s_alternativeemo.html', userRatings = User.get_user_ratings(data), songs = SOS2.get_songs_from_altemo(), user = User.get_by_id(data))

@app.route('/sos/sophisti-pop')
def sos_sophisti():

    data = {
        'id': session['user_id']
    }

    return render_template('s_o_s_sophistipop.html', userRatings = User.get_user_ratings(data), songs = SOS2.get_songs_from_sophisti(), user = User.get_by_id(data))

@app.route('/sos/new-romantic')
def sos_newromantic():

    data = {
        'id': session['user_id']
    }

    return render_template('s_o_s_newromantic.html',  userRatings = User.get_user_ratings(data), songs = SOS2.get_all_new_romantic(), user = User.get_by_id(data))

@app.route('/sos/dance-rock')
def sos_dancerock():

    data = {
        'id': session['user_id']
    }

    return render_template('s_o_s_dancerock.html', userRatings = User.get_user_ratings(data), allSOS = SOS2.get_all(), songs = SOS2.get_all_dance_rock(), user = User.get_by_id(data))

@app.route('/sos/freestyle')
def sos_freestyle():

    data = {
        'id': session['user_id']
    }

    return render_template('s_o_s_freestyle.html', userRatings = User.get_user_ratings(data), songs = SOS2.get_all_freestyle(), user = User.get_by_id(data))

@app.route('/sos/math-rock')
def sos_mathrock():

    data = {
        'id': session['user_id'] 
    }

    return render_template('s_o_s_mathrock.html', userRatings = User.get_user_ratings(data), songs = SOS2.get_all_math_rock(), user = User.get_by_id(data))

@app.route('/replay/2018')
def replay2018():

    data = {
        'id': session['user_id']
    }

    return render_template('replay2018.html', userRatings = User.get_user_ratings(data), songs = SOS2.get_all_replay2018(), user = User.get_by_id(data))

@app.route('/replay/2017')
def replay2017():

    data = {
        'id': session['user_id']
    }

    return render_template('replay2017.html', userRatings = User.get_user_ratings(data), songs = SOS2.get_all_replay2017(), user = User.get_by_id(data))

@app.route('/playalot')
def playalot():

    data = {
        'id': session['user_id']
    }

    return render_template('playalot.html', userRatings = User.get_user_ratings(data), songs = SOS2.get_all_playalot(), user = User.get_by_id(data))

@app.route('/replay/2019')
def replay2019():

    data = {
        'id': session['user_id']
    }

    return render_template('replay2019.html', userRatings = User.get_user_ratings(data), songs = SOS2.get_all_replay2019(), user = User.get_by_id(data))

@app.route('/replay/2015')
def replay2015():

    data = {
        'id': session['user_id']
    }

    return render_template('replay2015.html', userRatings = User.get_user_ratings(data), songs = SOS2.get_all_replay2015(), user = User.get_by_id(data))

@app.route('/replay/2016')
def replay2016():

    data = {
        'id': session['user_id']
    }

    return render_template('replay2016.html', userRatings = User.get_user_ratings(data), songs = SOS2.get_all_replay2016(), user = User.get_by_id(data))

@app.route('/replay/2020')
def replay2020():

    data = {
        'id': session['user_id']
    }

    return render_template('replay2020.html', userRatings = User.get_user_ratings(data), songs = SOS2.get_all_replay2020(), user = User.get_by_id(data))

@app.route('/replay/2021')
def replay2021():

    data = {
        'id': session['user_id']
    }

    return render_template('replay2021.html', userRatings = User.get_user_ratings(data), songs = SOS2.get_all_replay2021(), user = User.get_by_id(data))

@app.route('/top-albums')
def topalbums():

    data = {
        'id': session['user_id']
    }

    return render_template('top_albums.html', userRatings = User.get_user_ratings(data), albums = SOS2.get_all_top_albums(), user = User.get_by_id(data))

@app.route('/top-albums/<id>')
def solo_topalbums(id):

    albumID = {
        'id': id
    }

    data = {
        'id': session['user_id']
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_topalbum.html', userRatings = User.get_user_ratings(data), album = SOS2.get_top_by_id(albumID), user = User.get_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))


@app.route('/discover')
def sounds_of_spotify():

    data = {
        'id': session['user_id']
    }

    return render_template('discovery.html', userRatings = User.get_user_ratings(data), user = User.get_by_id(data), genres = allGenre.get_all())