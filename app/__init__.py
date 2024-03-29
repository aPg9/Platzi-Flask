from flask import Flask
from flask_bootstrap import Bootstrap as BT
from .config import Config
from .auth import auth
from flask_login import LoginManager
from app.models import UserModel

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(username):
    return UserModel.query(username)

def create_app():
    app = Flask(__name__)
    bootstrap = BT(app)

    app.config.from_object(Config)

    login_manager.init_app(app)
    
    app.register_blueprint(auth)

    return app