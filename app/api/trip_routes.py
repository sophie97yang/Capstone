from flask import Blueprint, jsonify
from flask_login import login_required
from ..models import Trip

trip_routes = Blueprint('trips', __name__)


@trip_routes.route('/')
def get_all_trips():
    pass
