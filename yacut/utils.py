from shortuuid import ShortUUID

from .models import URLMap


SHORT_ID_LENGTH = 6
SHORT_ID_PATTERN = r'^[A-Za-z0-9]{1,16}$'


def get_unique_short_id():
    """Функция создает short_id для короткой ссылки."""
    while True:
        short_id = ShortUUID().random(length=SHORT_ID_LENGTH)
        if not URLMap.query.filter_by(short=short_id).first():
            return short_id
