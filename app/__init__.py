from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import os
import sqlalchemy as sa


db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_type=None):
    app = Flask(__name__)

    if config_type == None:
        config_type = os.getenv(
            'CONFIG_TYPE', default='config.DevelopmentConfig')

    app.config.from_object(config_type)

    initialize_extensions(app)
    register_blueprints(app)

    engine = sa.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

    return app


def initialize_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)

    from app.models.User import User
    from app.models.Book import Book
    from app.models.Category import Category

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter(User.id == int(user_id)).first()

    login_manager.login_view = "auth.login"



def register_blueprints(app):
    from .auth import auth
    from .books import books
    from .authors import authors
    from .categories import categories
    from .lists import lists

    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(books, url_prefix="/")
    app.register_blueprint(authors, url_prefix="/authors")
    app.register_blueprint(categories, url_prefix="/categories")
    app.register_blueprint(lists, url_prefix="/lists")