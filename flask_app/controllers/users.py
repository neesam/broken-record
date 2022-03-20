from flask_app import app
from flask import redirect, render_template, request, session, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
bcrypt = Bcrypt(app)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/register/user', methods=['POST'])
def register_user():

    if not User.validate_registration(request.form):
        return redirect('/registration')
    
    data = {
        'email': request.form['email'],
        'username': request.form['username'],
        'avatar': request.form['avatar'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }

    id = User.save(data)

    session['user_id'] = id

    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/login/user', methods=['POST'])
def login_user():

    user = User.get_by_username(request.form)

    if not user:
        flash('Invalid username/password')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Invalid username/password')
        return redirect('/')

    session['user_id'] = user.id

    return redirect('/dashboard') 