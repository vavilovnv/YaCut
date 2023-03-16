from flask import flash, redirect, render_template, request

from . import app, db
from .forms import YaCutForm
from .models import URLMap
from .utils import YACUT_TEMPLATE, get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    """Функция обрабатывает запросы к основной странице сервиса."""
    form = YaCutForm()
    if form.validate_on_submit():
        short_url = form.custom_id.data
        if short_url and URLMap.query.filter_by(
                short=short_url
        ).first() is not None:
            form.custom_id.errors = [f'Имя {short_url} уже занято!']
            return render_template(YACUT_TEMPLATE, form=form)
        if not short_url:
            short_url = get_unique_short_id()
        obj = URLMap(
            original=form.original_link.data,
            short=short_url
        )
        db.session.add(obj)
        db.session.commit()
        short_link = request.base_url + short_url
        flash(f'Ваша новая ссылка готова: '
              f'<a href="{short_link}">{short_link}</a>')
    return render_template(YACUT_TEMPLATE, form=form)


@app.route('/<string:short>', methods=['GET'])
def short_url_view(short):
    """Функция перенаправляет по данным короткой ссылки на оригинальную
    страницу."""
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original
    )
