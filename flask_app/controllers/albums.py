from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.models.rating import Rating
from flask_app.models.album import Album
from flask_app.models.user import User
from flask_app.models.yearlyAlbums import yearlyAlbums
from flask_app.models.allTheYears import allTheYear 
from flask_app.models.seventy import Seventy

@app.route('/album/<id>')
def show_album(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_rating.html', user = User.get_by_id(userID), album = Album.get_by_id(data)) 

# FIFTIES


@app.route('/1960')
def sixty():

    userID = {
        'id': session['user_id']
    }

    return render_template('nineteensixty.html', user = User.get_by_id(userID), albums = allTheYear.get_sixty())

@app.route('/1960/<id>')
def solo_sixty(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = allTheYear.get_sixty_by_id(data))

@app.route('/1961')
def sixtyone():

    userID = {
        'id': session['user_id']
    }

    return render_template('nineteensixtyone.html', user = User.get_by_id(userID), albums = allTheYear.get_sixtyone())

@app.route('/1961/<id>')
def solo_sixtyone(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = allTheYear.get_sixtyone_by_id(data))

@app.route('/1963')
def sixtythree():

    userID = {
        'id': session['user_id']
    }

    return render_template('nineteensixtythree.html', user = User.get_by_id(userID), albums = allTheYear.get_sixtythree())

@app.route('/1963/<id>')
def solo_sixtythree(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = allTheYear.get_sixtythree_by_id(data))

@app.route('/1964')
def sixtyfour():

    userID = {
        'id': session['user_id']
    }

    return render_template('nineteensixtyfour.html', user = User.get_by_id(userID), albums = allTheYear.get_sixtyfour())

@app.route('/1964/<id>')
def solo_sixtyfour(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = allTheYear.get_sixtyfour_by_id(data))


@app.route('/1965')
def sixtyfive():

    userID = {
        'id': session['user_id']
    }

    return render_template('nineteensixtyfive.html', user = User.get_by_id(userID), albums = allTheYear.get_sixtyfive())

@app.route('/1965/<id>')
def solo_sixtyfive(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = allTheYear.get_sixtyfive_by_id(data))


@app.route('/1966')
def sixtysix():

    userID = {
        'id': session['user_id']
    }

    return render_template('nineteensixtysix.html', user = User.get_by_id(userID), albums = allTheYear.get_sixtysix())

@app.route('/1966/<id>')
def solo_sixtysix(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = allTheYear.get_sixtysix_by_id(data))


@app.route('/1967')
def sixtyseven():

    userID = {
        'id': session['user_id']
    }

    return render_template('nineteensixtyseven.html', user = User.get_by_id(userID), albums = allTheYear.get_sixtyseven())

@app.route('/1967/<id>')
def solo_sixtyseven(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = allTheYear.get_sixtyfour_by_id(data))


@app.route('/1968')
def sixtyeight():

    userID = {
        'id': session['user_id']
    }

    return render_template('nineteensixtyeight.html', user = User.get_by_id(userID), albums = allTheYear.get_sixtyeight())

@app.route('/1968/<id>')
def solo_sixtyeight(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = allTheYear.get_sixtyeight_by_id(data))


@app.route('/1969')
def sixtynine():

    userID = {
        'id': session['user_id']
    }

    return render_template('nineteensixtynine.html', user = User.get_by_id(userID), albums = allTheYear.get_sixtynine())

@app.route('/1969/<id>')
def solo_sixtynine(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = allTheYear.get_sixtynine_by_id(data))

@app.route('/1971')
def seventyone():

    userID = {
        'id': session['user_id']
    }

    return render_template('nineteenseventyone.html', user = User.get_by_id(userID), albums = Seventy.get_seventyone())

@app.route('/1971/<id>')
def solo_seventyone(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = Seventy.get_seventyone_by_id(data))

@app.route('/1973')
def seventythree():

    userID = {
        'id': session['user_id']
    }

    return render_template('nineteenseventythree.html', user = User.get_by_id(userID), albums = Seventy.get_seventythree())

@app.route('/1973/<id>')
def solo_seventythree(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = Seventy.get_seventythree_by_id(data))

@app.route('/1974')
def seventyfour():

    userID = {
        'id': session['user_id']
    }

    return render_template('nineteenseventyfour.html', user = User.get_by_id(userID), albums = Seventy.get_seventyfour())

@app.route('/1974/<id>')
def solo_seventyfour(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = Seventy.get_seventyfour_by_id(data))


@app.route('/1975')
def seventyfive():

    userID = {
        'id': session['user_id']
    }

    return render_template('nineteenseventyfive.html', user = User.get_by_id(userID), albums = Seventy.get_seventyfive())

@app.route('/1975/<id>')
def solo_seventyfive(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = Seventy.get_seventyfive_by_id(data))


@app.route('/1976')
def seventysix():

    userID = {
        'id': session['user_id']
    }

    return render_template('nineteenseventysix.html', user = User.get_by_id(userID), albums = Seventy.get_seventysix())

@app.route('/1976/<id>')
def solo_seventysix(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = Seventy.get_seventysix_by_id(data))


@app.route('/1977')
def seventyseven():

    userID = {
        'id': session['user_id']
    }

    return render_template('nineteenseventyseven.html', user = User.get_by_id(userID), albums = Seventy.get_seventyseven())

@app.route('/1977/<id>')
def solo_seventyseven(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = Seventy.get_seventyfour_by_id(data))


@app.route('/1978')
def seventyeight():

    userID = {
        'id': session['user_id']
    }

    return render_template('nineteenseventyeight.html', user = User.get_by_id(userID), albums = Seventy.get_seventyeight())

@app.route('/1978/<id>')
def solo_seventyeight(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = Seventy.get_seventyeight_by_id(data))


@app.route('/1979')
def seventynine():

    userID = {
        'id': session['user_id']
    }

    return render_template('nineteenseventynine.html', user = User.get_by_id(userID), albums = Seventy.get_seventynine())

@app.route('/1979/<id>')
def solo_seventynine(id):

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = Seventy.get_seventynine_by_id(data))



@app.route('/2000')
def twothousand():

    userID = {
        'id': session['user_id']
    }

    data = {
        'id': id
    }

    return render_template('twothousand.html', user = User.get_by_id(userID), albums = yearlyAlbums.get_twothousand())

@app.route('/2000/<id>')
def twothousand_individual(id):

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

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = yearlyAlbums.get_twothousand_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both)) 

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

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = yearlyAlbums.get_twothousandone_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

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

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = yearlyAlbums.get_twothousandtwo_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

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

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = yearlyAlbums.get_twothousandthree_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

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

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = yearlyAlbums.get_twothousandfour_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

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

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = yearlyAlbums.get_twothousandfive_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

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

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = yearlyAlbums.get_twothousandsix_by_id(data), allUserRatings = User.get_user_ratings_for_one_album_page(both))

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

    both = {
        'id': session['user_id'],
        'id2': id
    }

    return render_template('show_yearly.html', user = User.get_by_id(userID), album = yearlyAlbums.get_twothousandseven_by_id(data))