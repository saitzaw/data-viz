"""Routes for api call"""

from flask import Blueprint, render_template
from flask import current_app as app

dashboard = Blueprint('dashboard', __name__,
                      template_folder='templates', static_folder='static')


@dashboard.route('/home')
def home_page():
    """Loading the home page"""
    return render_template('home.html')

@dashboard.route('/dashboard')
def data_visualize(): 
    """ Loading the dashboard """ 
    from . import views 
    views.dashborad