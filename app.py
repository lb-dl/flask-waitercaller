from flask import Flask

from flask_login import LoginManager

# from mockdbhelper import MockDBHelper as DBHelper
from passwordhelper import PasswordHelper
from bitlyhelper import BitlyHelper
from user import User
from qrhelper import QRHelper

import config

if config.test:
    from sql.mockdbhelper import MockDBHelper as DBHelper
else:
    from sql.dbhelper import DBHelper

DB = DBHelper()
PH = PasswordHelper()
BH = BitlyHelper()
QR = QRHelper()


login_manager = LoginManager()
login_manager.login_view = 'main.login'


@login_manager.user_loader
def load_user(user_id):
    user_password = DB.get_user(user_id)
    if user_password:
        return User(user_id)


def create_app():
    app = Flask(__name__)

    app.config.update(
        SECRET_KEY='53PvPCt8G3D6roxjLE6Q9LZzdVRdcRVmyKlpYSHshEAPJGe4bsnLU7Lk7Z0YTFOKjIvKtFQLLApGQXLte0LZS34j2GNgPFiFHv',
    )
    login_manager.init_app(app)

    from views.main.routes import main
    from views.tables.routes import tables
    from views.users.routes import users

    app.register_blueprint(main)
    app.register_blueprint(tables)
    app.register_blueprint(users)

    return app
