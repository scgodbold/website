from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from frontend.views import frontend
app.register_blueprint(frontend)

from ef.views import ef
app.register_blueprint(ef)

from pancake.views import pancake
app.register_blueprint(pancake)
