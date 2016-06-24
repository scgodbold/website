from flask import Flask
from flask_flatpages import FlatPages

app = Flask(__name__)
flat_pages = FlatPages(app)
app.config.from_object('config')

# The (bulk of) the views for the site`
from views import site
app.register_blueprint(site)


# Pancake Lincoln groupme bots
from app.pancake.views import pancake
app.register_blueprint(pancake)

# Errors are good to handle
import error
