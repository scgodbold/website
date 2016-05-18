from flask import Blueprint, render_template


site = Blueprint('site', __name__)


@site.route('/', methods=['GET'])
def home():
    return render_template('home.html')
