from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.models.criterions import Criterion
from flask_app.models.user import User

@app.route('/criterion')
def criterion():

    if 'user_id' not in session:
        return redirect('/')

    data = {
        'id': session['user_id']
    }

    return render_template('criterion.html', films = Criterion.get_all(), user = User.get_by_id(data))