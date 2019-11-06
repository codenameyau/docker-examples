from flask import Flask
from boilerplate.routes import boilerplate

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'

app.register_blueprint(boilerplate, url_prefix='/boilerplate')
