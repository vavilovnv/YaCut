from flask import flash, redirect, render_template, request, url_for

from . import app, db
from .models import URLMap
from .forms import YaCutForm
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = YaCutForm()
    if form.validate_on_submit():
        short_url = form.custom_id.data
        if short_url and URLMap.query.filter_by(short=short_url).first() is not None:
            form.custom_id.errors = ['Короткая ссылка уже зарегистрирована.']
            return render_template('yacut.html', form=form)
        if not short_url:
            short_url = get_unique_short_id()
        obj = URLMap(
            original=form.original_link.data,
            short=short_url
        )
        db.session.add(obj)
        db.session.commit()
        short_link = request.base_url + short_url
        flash(f'Ваша новая ссылка готова: <a href="{short_link}">{short_link}</a>')
    return render_template('yacut.html', form=form)


@app.route('/<string:short>', methods=['GET'])
def short_url_view(short):
    return redirect(URLMap.query.filter_by(short=short).first_or_404().original)
