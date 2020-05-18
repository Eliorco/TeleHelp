# url api
# https://api.telegram.org/bot<token>/METHOD_NAME
from flask import Flask
from telehelp.configuration import FLASK_SECRET_KEY, db_connection_string
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = FLASK_SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_connection_string}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from telehelp import routes