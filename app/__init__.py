import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY']='dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://rohan:password@localhost:5432/gutendex"

    from . import dump
    dump.init_app(app)
    
    from . import db
    db.init_db(app)
    
    from .views import core
    app.register_blueprint(core)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app