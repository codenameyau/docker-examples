from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

boilerplate = Blueprint('boilerplate', __name__, template_folder='templates')

@boilerplate.route('/')
def home_page():
    try:
        return render_template('boilerplate/index.html')
    except TemplateNotFound:
        abort(404)
