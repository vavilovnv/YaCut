from http import HTTPStatus
from re import match

from flask import Response, jsonify, request

from . import app
from .utils import SHORT_ID_PATTERN, save_data
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/', methods=['POST'])
def create_short_url_api() -> tuple[Response, HTTPStatus]:
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if not data.get('custom_id'):
        data['custom_id'] = URLMap.get_unique_short_id()
    elif URLMap.query.filter_by(short=data['custom_id']).first():
        raise InvalidAPIUsage('Имя "py" уже занято.')
    elif not match(SHORT_ID_PATTERN, data['custom_id']):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    obj = URLMap()
    obj.from_dict(data)
    save_data(obj)
    return jsonify(obj.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short>/', methods=['GET'])
def get_short_url_api(short: str) -> tuple[Response, HTTPStatus]:
    obj = URLMap.query.filter_by(short=short).first()
    if obj is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': obj.original}), HTTPStatus.OK
