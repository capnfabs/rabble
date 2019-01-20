from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db():
    import app
    with app.create_app().app_context():
        db.create_all()


class Message(db.Model):
    msg_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    # TODO: I want to key this off of a session sometime, because I've seen anonymous chat apps be
    # super prone to users trying to impersonate each other and that seems terrible. Keying this to
    # a server-allocated session ID gives us a mechanism to differentiate, which we can eventually
    # pass to the UI.
    username = db.Column(db.Text, nullable=False)
    # TODO: I have no idea if this plays nicely with timezones or not, I have a vague recollection
    # of python's datetime having tz-aware as the default.
    when_created = db.Column(db.DateTime, nullable=False, index=True)
