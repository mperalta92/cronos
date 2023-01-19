from flask_restx import Api, cors
from flask import current_app, url_for, render_template


api = Api(version='1.0', title='Cronos',
          description='Cronos api with swagger library')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    current_app.logger.exception(message)
    if not current_app.config['DEBUG']:
        return {'message': message}, 500

@api.documentation
@cors.crossdomain(origin='*')
def custom_ui():
    specs_path = url_for(api.endpoint('specs'))
    return render_template('custom-swagger-ui.html', title=api.title,
                           specs_url=specs_path)
