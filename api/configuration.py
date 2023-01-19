from flask import Flask, Blueprint
from api.restx import Api, api
from api.resources.task_resource import TaskResource
from flask_injector import FlaskInjector
import os


def configure_api_routes(api: Api):
    api.add_resource(TaskResource, '/task')

def configure_api_bindings(binder):
    pass


# def create_app(config: object = None, testing_modules_binding = [], configure_database=True, configure_scheduler=True):
# 	app = Flask(__name__)
# 	#if not config:
# 	#	config = f'environment_config.{get_environment_name()}Config'
# 	#app.config.from_object(config)  # TODO: implement function get_environment_name()
# 	# initializer = configure_database(app.config.get('DATABASE_URI'))  #TODO: implement configure_database function
	
# 	api_blueprint = Blueprint('cronos_api', __name__, url_prefix='/cronos-api')
# 	api.init_app(api_blueprint)
	
# 	configure_api_routes(api)
# 	app.register_blueprint(api_blueprint)
	
# 	injector = FlaskInjector(app=app, modules=testing_modules_binding) if testing_modules_binding else FlaskInjector(app=app, modules=binding_modules)
	
# 	return app