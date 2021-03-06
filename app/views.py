from flask import Blueprint, jsonify, request
from .utils import search_library

core = Blueprint('core', __name__, url_prefix="/")

@core.route('/search')
def search():
    # Calling method with query parameters
    data = search_library(request.args)
    return jsonify({'success': True, 'data': data})