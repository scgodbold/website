from flask import Blueprint, request
from resources.testbot import TestBot
from resources.rainyday import RainyDay


pancake = Blueprint('pancake', __name__, url_prefix='/pancake')


@pancake.route('/', methods=['POST'])
def home():
    """Groupme robit landing page"""
    json = request.get_json()
    bot = TestBot()
    bot.parse(json)
    return 'Hello World!'


@pancake.route('/rainyday', methods=['POST'])
def rainyday():
    """Rainyday robit landing page"""
    json = request.get_json()
    bot = RainyDay()
    bot.parse(json)
    return 'Hello World!'
