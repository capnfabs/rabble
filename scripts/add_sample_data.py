#!/usr/bin/env python
from datetime import datetime

from models import Message, db


def main():
    import app
    with app.create_app().app_context():
        db.session.add(Message(content='Hello!', username='Fabian', when_created=datetime.now()))
        db.session.add(Message(content='Hello back!', username='Susan', when_created=datetime.now()))
        db.session.commit()

if __name__ == '__main__':
    main()
