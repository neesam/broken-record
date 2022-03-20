from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.models.user import User
from flask_app.models.rating import Rating 
from flask_app.models.album import Album
from flask_app.models.favArtist import favArtist
from flask_app.models.brookfield import Brookfield
from flask_app.models.yearlyAlbums import yearlyAlbums
from flask_app.models.message import Message

@app.route('/messages')
def messages():

    data = {
        'id': session['user_id']
    }

    return render_template('messages.html', user = User.get_by_id(data), users = User.get_all_users(), messages = Message.get_user_messages(data))

@app.route('/post_message',methods=['POST'])
def post_message():
    if 'user_id' not in session:
        return redirect('/')

    data = {
        "sender_id":  request.form['sender_id'],
        "receiver_id" : request.form['receiver_id'],
        "content": request.form['content']
    }
    Message.save(data)

    return redirect('/messages')
@app.route('/destroy/message/<int:id>')
def destroy_message(id):
    data = {
        "id": id
    }
    Message.destroy(data)
    return redirect('/messages')