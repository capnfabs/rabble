from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local.db'
    # Suppress a deprecation warning that I don't understand. This is the new
    # default value.
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    import models
    models.db.init_app(app)

    import api
    app.register_blueprint(api.blueprint)

    import frontend
    app.register_blueprint(frontend.blueprint)

    return app
