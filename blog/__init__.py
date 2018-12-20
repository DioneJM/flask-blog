import os
from flask import Flask

def create_app(test_config=None):
    #Create a WSGI application
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'blog.sqlite'),
   )
   
    if test_config is None:
        #Load the instance_config to test_config
        app.config.from_pyfile('config.py', silent=True)
    else:
        #Load the test_config in
        app.config.from_mapping(test_config)

   #Check if instance folders exist
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #Creating basic page
    @app.route('/hello')
    def hello():
        return "Hello World!"

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app
