import datetime

from flask import request, jsonify, Blueprint

from models import db

blueprint = Blueprint('api', __name__, url_prefix='/api')

DAWN_OF_TIME = datetime.datetime.min


@blueprint.route('/messages', methods=['GET'])
def get_messages():
    from models import Message
    since = request.args.get('since', DAWN_OF_TIME)
    # TODO: pagination
    msgs = db.session.query(Message).filter(Message.when_created >= since).all()
    return jsonify({'results': [format_msg(msg) for msg in msgs]})


def format_msg(msg):
    return {
        'content': msg.content,
        'username': msg.username,
        'when_created': msg.when_created,
    }
