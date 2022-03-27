from flask_app import app
from flask_app.controllers import users, dashboards, ratings, albums, years, genres, messages, criterion
if __name__ == '__main__':
    app.run(debug=True)
