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

    @staticmethod
    def get_unique_short_id() -> str:
        """Функция создает short_id для короткой ссылки."""
        while True:
            short_id = ShortUUID().random(length=SHORT_ID_LENGTH)
            if not URLMap.query.filter_by(short=short_id).first():
                return short_id

    def to_dict(self) -> dict[str, str]:
        return dict(
            url=self.original,
            short_link=url_for(
                'short_url_view',
                short=self.short,
                _external=True)
        )

    def from_dict(self, data: dict[str, str]) -> None:
        self.original = data['url']
        self.short = data['custom_id']

    def shorten(self, original_link: str, short_id: str) -> None:
        self.original = original_link
        if not short_id:
            short_id = self.get_unique_short_id()
        self.short = short_id
