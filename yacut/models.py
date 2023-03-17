from datetime import datetime

from flask import url_for
from shortuuid import ShortUUID

from . import db

SHORT_ID_LENGTH = 6


class URLMap(db.Model):
    """Модель соответствия оригинальной и короткой ссылок."""
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False, index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __init__(self, original: str = '', short: str = ''):
        self.original = original
        if not short:
            short = self.get_unique_short_id()
        self.short = short

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for(
                'short_url_view',
                short=self.short,
                _external=True)
        )

    @staticmethod
    def get_unique_short_id():
        """Функция создает short_id для короткой ссылки."""
        while True:
            short_id = ShortUUID().random(length=SHORT_ID_LENGTH)
            if not URLMap.query.filter_by(short=short_id).first():
                return short_id
