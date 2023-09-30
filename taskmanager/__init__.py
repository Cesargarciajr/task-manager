import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("envy.py"):
    import env # nqoa

app = Flask(__name__)
app.config["SECRET_KEY"]
app.config["SQLACHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from taskmanager import routes # nqoa
