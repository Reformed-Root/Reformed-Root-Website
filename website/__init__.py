from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'UUu1NOwZCxqGHfKDqRbVBIodT9NxZ_rYZJMoetsbyk4'

    from .views import views
    app.register_blueprint(views)

    return app
