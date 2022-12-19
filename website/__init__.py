from flask import Flask
from flaskext.mysql import MySQL


mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "helloworld"
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = ''
    app.config['MYSQL_DATABASE_DB'] = 'books-rating'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    
    mysql.init_app(app)
    
    from .auth import auth


    app.register_blueprint(auth, url_prefix="/")
    
    
    return app