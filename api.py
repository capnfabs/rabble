import datetime

from flask import request, jsonify, Blueprint

from models import db, Message

blueprint = Blueprint('api', __name__, url_prefix='/api')

DAWN_OF_TIME = datetime.datetime.min


@blueprint.route('/messages', methods=['GET'])
def get_messages():
    since = request.args.get('since', DAWN_OF_TIME)
    # TODO: pagination
    msgs = db.session.query(Message).filter(Message.when_created >= since).all()
    return jsonify({'results': [format_msg(msg) for msg in msgs]})


@blueprint.route('/messages', methods=['POST'])
def post_message():
    obj = request.form
    msg = Message(
        content=obj['content'],
        username=obj['username'])
    db.session.add(msg)
    # This API is weird and I don't like it. I would want to wrap this in contextmanagers if I was
    # doing this for any longer.
    db.session.commit()
    # 204 == no content but the kids are alright
    return '', 204


def format_msg(msg):
    return {
        'content': msg.content,
        'username': msg.username,
        # It's not clear _why_ the default setup is returning "Sun, 20 Jan 2019 18:09:45 GMT", but
        # using ISO8601 is going to make it a lot simpler when interpreting timestamps in JS.
        # TODO: these don't have a timezone right now, which probably means that they'll do weird
        #    things. Fix this.
        'when_created': msg.when_created.isoformat(),
    }
