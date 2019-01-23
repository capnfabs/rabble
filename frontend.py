from flask import Blueprint, render_template, request

from models import db, Message

blueprint = Blueprint('frontend', __name__)


@blueprint.route('/', methods=['GET'])
def get_index():
    # TODO: pagination
    msgs = db.session.query(Message).all()
    return render_template('index.html', messages=msgs)
