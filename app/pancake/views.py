import requests

from flask import Blueprint, jsonify, request

from app import app
from app.pancake.process import rainy_day

pancake = Blueprint('pancake', __name__, url_prefix='/pancake')


@pancake.route('/health', methods=['GET'])
def health():
    payload = {'message': 'Good day sir, what can I help you with?'}
    return jsonify(payload)


@pancake.route('/', methods=['POST'])
def endpoint():
    json = request.get_json()
    if json['sender_type'] == 'user':
        # Well dont want our but to cause recursion, since its a user
        # Lets fire up the ole bot script
        response = rainy_day(json)
        if response is not None:
            response['bot_id'] = app.config['GROUPME_BOTS'][json['group_id']]
            requests.post(app.config['GROUPME_URL'], response)
    return None
