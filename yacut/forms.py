from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from .utils import SHORT_ID_PATTERN


class YaCutForm(FlaskForm):
    """Основные параметры формы главной страницы сервиса."""
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            URL(require_tld=True, message='Некорректная ссылка')
        ]
    )
    custom_id = URLField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16),
            Optional(),
            Regexp(SHORT_ID_PATTERN, message='Некорректная ссылка')]
    )
    submit = SubmitField('Создать')
