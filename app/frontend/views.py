from flask import Blueprint, render_template

frontend = Blueprint('frontend', __name__)


@frontend.route('/', methods=['GET'])
def home():
    """Website Landing Page"""
    return render_template('index.html')
