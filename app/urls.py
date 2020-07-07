"""Routes for api call"""

from flask import Blueprint, render_template
from flask import current_app as app

from .data import c

home_page = Blueprint('home_page', __name__,
                      template_folder='templates', static_folder='static')


@home_page.route('/')
def index():
    """ loading D3.js data page""" 
    return render_template('index.html') 


@home_page.route('/home')
def main_page():
    """Loading the home page"""
    return render_template('home.html')
