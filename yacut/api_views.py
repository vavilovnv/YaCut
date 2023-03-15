from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/', methods=['POST'])
def add_opinions():
    data = request.get_json()
    if 'original_url' not in data or 'short_url' not in data:
        raise InvalidAPIUsage('There are no mandatory fields in the request')
    if URLMap.query.filter_by(short_url=data['short_url']).first() is not None:
        raise InvalidAPIUsage('The opinion is already exists in database')
    obj = URLMap()
    obj.from_dict(data)
    db.session.add(obj)
    db.session.commit()
    return jsonify({'opinion': obj.to_dict()}), 201


@app.route('/api/id/<path:short_id>/', methods=['GET'])
def get_random_opinion(short_id):
    obj = URLMap.query.filter_by(short_url=short_id).first()
    if obj is None:
        raise InvalidAPIUsage('Short url is not found', 404)
    return jsonify({'opinion': obj.to_dict()}), 200
