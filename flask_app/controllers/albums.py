from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.models.rating import Rating
from flask_app.models.album import Album
from flask_app.models.user import User
from flask_app.models.yearlyAlbums import yearlyAlbums
from flask_app.models.allTheYears import allTheYear 
from flask_app.models.seventy import Seventy
from flask_app.models.allAlbums import allAlbum

@app.route('/album/<id>')
def show_album(id):

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_rating.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Album.get_by_id(data),allUserRatings = User.get_user_ratings_for_one_album_page(both)) 

#SIXTIES


@app.route('/1960')
def sixty():

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = allTheYear.get_sixty())

@app.route('/1960/<id>')
def solo_sixty(id):

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = allTheYear.get_sixty_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/1961')
def sixtyone():

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = allTheYear.get_sixtyone())

@app.route('/1961/<id>')
def solo_sixtyone(id):

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = allTheYear.get_sixtyone_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/1962')
def sixtytwo():

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = allTheYear.get_sixtytwo())

@app.route('/1962/<id>')
def solo_sixtytwo(id):

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = allTheYear.get_sixtytwo_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))


@app.route('/1963')
def sixtythree():

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = allTheYear.get_sixtythree())

@app.route('/1963/<id>')
def solo_sixtythree(id):

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = allTheYear.get_sixtythree_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/1964')
def sixtyfour():

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = allTheYear.get_sixtyfour())

@app.route('/1964/<id>')
def solo_sixtyfour(id):

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = allTheYear.get_sixtyfour_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))


@app.route('/1965')
def sixtyfive():

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = allTheYear.get_sixtyfive())

@app.route('/1965/<id>')
def solo_sixtyfive(id):

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = allTheYear.get_sixtyfive_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))


@app.route('/1966')
def sixtysix():

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = allTheYear.get_sixtysix())

@app.route('/1966/<id>')
def solo_sixtysix(id):

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = allTheYear.get_sixtysix_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))


@app.route('/1967')
def sixtyseven():

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = allTheYear.get_sixtyseven())

@app.route('/1967/<id>')
def solo_sixtyseven(id):

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = allTheYear.get_sixtyseven_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))


@app.route('/1968')
def sixtyeight():

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = allTheYear.get_sixtyeight())

@app.route('/1968/<id>')
def solo_sixtyeight(id):

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = allTheYear.get_sixtyeight_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))


@app.route('/1969')
def sixtynine():

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = allTheYear.get_sixtynine())

@app.route('/1969/<id>')
def solo_sixtynine(id):

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = allTheYear.get_sixtynine_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/1970')
def seventy():

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_seventy())

@app.route('/1970/<id>')
def solo_seventy(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_seventy_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/1971')
def seventyone():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_seventyone())

@app.route('/1971/<id>')
def solo_seventyone(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_seventyone_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/1972')
def seventytwo():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_seventytwo())

@app.route('/1972/<id>')
def solo_seventytwo(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_seventytwo_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/1973')
def seventythree():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_seventythree())

@app.route('/1973/<id>')
def solo_seventythree(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_seventythree_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/1974')
def seventyfour():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_seventyfour())

@app.route('/1974/<id>')
def solo_seventyfour(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_seventyfour_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))


@app.route('/1975')
def seventyfive():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_seventyfive())

@app.route('/1975/<id>')
def solo_seventyfive(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_seventyfive_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))


@app.route('/1976')
def seventysix():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_seventysix())

@app.route('/1976/<id>')
def solo_seventysix(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_seventysix_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))


@app.route('/1977')
def seventyseven():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_seventyseven())

@app.route('/1977/<id>')
def solo_seventyseven(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_seventyfour_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))


@app.route('/1978')
def seventyeight():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_seventyeight())

@app.route('/1978/<id>')
def solo_seventyeight(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_seventyeight_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))


@app.route('/1979')
def seventynine():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_seventynine())

@app.route('/1979/<id>')
def solo_seventynine(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_seventynine_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/1980')
def eighty():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_eighty())

@app.route('/1980/<id>')
def solo_eighty(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_eighty_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/1981')
def eightyone():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_eighty())

@app.route('/1981/<id>')
def solo_eightyone(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_eightyone_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/1982')
def eightytwo():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_eightytwo())

@app.route('/1982/<id>')
def solo_eightytwo(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_eightytwo_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/1983')
def eightythree():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_eightythree())

@app.route('/1983/<id>')
def solo_eightythree(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_eightythree_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/1984')
def eightyfour():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_eightyfour())

@app.route('/1984/<id>')
def solo_eightyfour(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_eightyfour_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))


@app.route('/1985')
def eightyfive():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_eightyfive())

@app.route('/1985/<id>')
def solo_eightyfive(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_eightyfive_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))


@app.route('/1986')
def eightysix():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_eightysix())

@app.route('/1986/<id>')
def solo_eightysix(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_eightysix_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))


@app.route('/1987')
def eightyseven():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_eightyseven())

@app.route('/1987/<id>')
def solo_eightyseven(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_eightyseven_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))


@app.route('/1988')
def eightyeight():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_eightyeight())

@app.route('/1988/<id>')
def solo_eightyeight(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_eightyeight_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))


@app.route('/1989')
def eightynine():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_eightynine())

@app.route('/1989/<id>')
def solo_eightynine(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_eightynine_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/1990')
def ninety():

    if 'user_id' not in session:
        return redirect('/')
        
    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_ninety())

@app.route('/1990/<id>')
def solo_ninety(id):

    if 'user_id' not in session:
        return redirect('/')
        
    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_ninety_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/1991')
def ninetyone():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_ninetyone())

@app.route('/1991/<id>')
def solo_ninetyone(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_ninetyone_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/1992')
def ninetytwo():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_ninetytwo())

@app.route('/1992/<id>')
def solo_ninetytwo(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_ninetytwo_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/1993')
def ninetythree():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_ninetythree())

@app.route('/1993/<id>')
def solo_ninetythree(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_ninetythree_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/1994')
def ninetyfour():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_ninetyfour())

@app.route('/1994/<id>')
def solo_ninetyfour(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_ninetyfour_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))


@app.route('/1995')
def ninetyfive():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_ninetyfive())

@app.route('/1995/<id>')
def solo_ninetyfive(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_ninetyfive_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))


@app.route('/1996')
def ninetysix():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_ninetysix())

@app.route('/1996/<id>')
def solo_ninetysix(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_ninetysix_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))


@app.route('/1997')
def ninetyseven():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_ninetyseven())

@app.route('/1997/<id>')
def solo_ninetyseven(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_ninetyseven_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))


@app.route('/1998')
def ninetyeight():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_ninetyeight())

@app.route('/1998/<id>')
def solo_ninetyeight(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_ninetyeight_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))


@app.route('/1999')
def ninetynine():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_ninetynine())

@app.route('/1999/<id>')
def solo_ninetynine(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), allUserRatings = User.get_user_ratings_for_one_album_page(both), album = Seventy.get_ninetynine_by_id(data))




@app.route('/2000')
def twothousand():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_twothousand())

@app.route('/2000/<id>')
def twothousand_individual(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_twothousand_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both)) 

@app.route('/2001')
def twothousandone():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    return render_template('yearly_page.html', userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_twothousandone())

@app.route('/2001/<id>')
def twothousandone_individual(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_twothousandone_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/2002')
def twothousandtwo():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_twothousandtwo())

@app.route('/2002/<id>')
def twothousandtwo_individual(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_twothousandtwo_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/2003')
def twothousandthree():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_twothousandthree())

@app.route('/2003/<id>')
def twothousandthree_individual(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_twothousandthree_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/2004')
def twothousandfour():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_twothousandfour())

@app.route('/2004/<id>')
def twothousandfour_individual(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_twothousandfour_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/2005')
def twothousandfive():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_twothousandfive())

@app.route('/2005/<id>')
def twothousandfive_individual(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_twothousandfive_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/2006')
def twothousandsix():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_twothousandsix())

@app.route('/2006/<id>')
def twothousandsix_individual(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_twothousandsix_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/2007')
def twothousandseven():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_twothousandseven())

@app.route('/2007/<id>')
def twothousandseven_individual(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_twothousandseven_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/2008')
def twothousandeight():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_twothousandeight())

@app.route('/2008/<id>')
def twothousandeight_individual(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    data = {
        'id': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_twothousandeight_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/2009')
def twothousandnine():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_twothousandnine())

@app.route('/2009/<id>')
def twothousandnine_individual(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_twothousandnine_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/2010')
def twothousandten():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_twothousandten())

@app.route('/2010/<id>')
def twothousandten_individual(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_twothousandten_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/2011')
def twothousandeleven():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_twothousandeleven())

@app.route('/2011/<id>')
def twothousandeleven_individual(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_twothousandeleven_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/2012')
def twothousandtwelve():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_twothousandtwelve())

@app.route('/2012/<id>')
def twothousandtwelve_individual(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_twothousandtwelve_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/2013')
def twothousandthirteen():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_twothousandthirteen())

@app.route('/2013/<id>')
def twothousandthirteen_individual(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_twothousandthirteen_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/2014')
def twothousandfourteen():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_twothousandfourteen())

@app.route('/2014/<id>')
def twothousandfourteen_individual(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_twothousandfourteen_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/2015')
def twothousandfifteen():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_twothousandfifteen())

@app.route('/2015/<id>')
def twothousandfifteen_individual(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_twothousandfifteen_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/2016')
def twothousandsixteen():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_twothousandsixteen())

@app.route('/2016/<id>')
def twothousandsixteen_individual(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_twothousandsixteen_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/2017')
def twothousandseventeen():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_twothousandseventeen())

@app.route('/2017/<id>')
def twothousandseventeen_individual(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_twothousandseventeen_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/2018')
def twothousandeighteen():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_twothousandeighteen())

@app.route('/2018/<id>')
def twothousandeighteen_individual(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_twothousandeighteen_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/2019')
def twothousandnineteen():

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    return render_template('yearly_page.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), albums = Seventy.get_twothousandnineteen())

@app.route('/2019/<id>')
def twothousandnineteen_individual(id):

    if 'user_id' not in session:
        return redirect('/')
        
    userID = {
        'id': session['user_id']
    }
    

    data = {
        'id': id
    }

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = Seventy.get_twothousandnineteen_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

@app.route('/random')
def random_album():

    if 'user_id' not in session:
        return redirect('/')

    userID = {
        'id': session['user_id']
    }

    return render_template('random_album.html',  userRatings = User.get_user_ratings(userID), user = User.get_by_id(userID), album = allAlbum.get_random_from_all())
