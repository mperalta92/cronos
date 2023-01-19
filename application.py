from flask import Flask, Blueprint
from flask_injector import FlaskInjector
import scheduler
from api.restx import api
from api.configuration import configure_api_routes, configure_api_bindings
import os


routing_modules = [
	configure_api_routes,
]

binding_modules = [
	configure_api_bindings,
]


def create_app(config: object = None, testing_modules_binding = [], configure_database=True, configure_scheduler=True):
	app = Flask(__name__)
	#if not config:
	#	config = f'environment_config.{get_environment_name()}Config'
	#app.config.from_object(config)  # TODO: implement function get_environment_name()
	# initializer = configure_database(app.config.get('DATABASE_URI'))  #TODO: implement configure_database function
	
	if os.environ.get("WERKZEUG_RUN_MAIN") != "true" and configure_scheduler:
		scheduler.scheduler_main.init_app(app)
		scheduler.scheduler_main.start()

	
	api_blueprint = Blueprint('cronos_api', __name__, url_prefix='/cronos-api')
	for routing in routing_modules:
		routing(api)
	api.init_app(api_blueprint)
	app.register_blueprint(api_blueprint)
	
	inject_modules = testing_modules_binding if testing_modules_binding else binding_modules
	injector = FlaskInjector(app=app, modules=inject_modules)
	
	return app

application = create_app()


if __name__ == '__main__':
	application.run(host='0.0.0.0', port=8000, threaded=True, debug=True)
