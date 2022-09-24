from flask import Flask
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask import flash

app = Flask(__name__)
app.secret_key = "alovio"

