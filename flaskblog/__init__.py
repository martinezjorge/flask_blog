import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Log in to proceed!'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.blogs.routes import blogs
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    from flaskblog.comments.routes import comments
    from flaskblog.search.routes import search
    app.register_blueprint(users)
    app.register_blueprint(blogs)
    app.register_blueprint(comments)
    app.register_blueprint(main)
    app.register_blueprint(search)
    app.register_blueprint(errors)

    return app
