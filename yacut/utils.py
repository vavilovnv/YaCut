from . import db
from .models import URLMap

SHORT_ID_PATTERN = r'^[A-Za-z0-9]{1,16}$'
YACUT_TEMPLATE = 'yacut.html'


def save_data(obj: URLMap) -> None:
    db.session.add(obj)
    db.session.commit()
