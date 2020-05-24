from flask import Flask
from {{cookiecutter.app}} import config

def create_app():
    {{cookiecutter.app}} = Flask(__name__)
    {{cookiecutter.app}}.config.from_object(config.Config)
    
    from {{cookiecutter.app}}.home.routes import home
    {{cookiecutter.app}}.register_blueprint(home)

    return {{cookiecutter.app}}
