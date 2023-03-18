from urllib.parse import urljoin

from flask import Response, flash, redirect, render_template, request

from . import app
from .utils import YACUT_TEMPLATE, save_data
from .forms import YaCutForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view() -> str:
    """Функция обрабатывает запросы к основной странице сервиса."""
    form = YaCutForm()
    if not form.validate_on_submit():
        return render_template(YACUT_TEMPLATE, form=form)
    short_url = form.custom_id.data
    if short_url and URLMap.query.filter_by(
            short=short_url
    ).first() is not None:
        form.custom_id.errors = [f'Имя {short_url} уже занято!']
        return render_template(YACUT_TEMPLATE, form=form)
    obj = URLMap()
    obj.shorten(form.original_link.data, short_url)
    save_data(obj)
    short_link = urljoin(request.base_url, obj.short)
    flash(f'Ваша новая ссылка готова: '
          f'<a href="{short_link}">{short_link}</a>')
    return render_template(YACUT_TEMPLATE, form=form)


@app.route('/<string:short>', methods=['GET'])
def short_url_view(short: str) -> Response:
    """Функция перенаправляет по данным короткой ссылки на оригинальную
    страницу."""
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original
    )
