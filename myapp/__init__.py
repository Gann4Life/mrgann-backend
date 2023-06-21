from flask import Flask
from .api.routes import api
from .site.routes import site

def create_app():
	app = Flask(__name__, static_folder=None)

	blueprints = [
		api, site
	]

	for blueprint in blueprints:
		app.register_blueprint(blueprint)

	return app