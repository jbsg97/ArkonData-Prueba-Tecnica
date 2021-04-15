from flask import Flask
from src.config.db import db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'

@app.route("/")
def index():
    return "<h1>Bienvenidos a la api de ArkonData</h1>"

db.init_app(app)