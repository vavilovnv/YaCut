from flask import flash, redirect, render_template, url_for

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
            flash('Такая короткая ссылка уже зарегистрирована.')
            return render_template('index.html', form=form)
        if not short_url:
            short_url = get_unique_short_id(form.original_link.data)
        obj = URLMap(
            original=form.original_link.data,
            short=short_url
        )
        db.session.add(obj)
        db.session.commit()
        return redirect(url_for('short_url_view', id=obj.id))
    return render_template('index.html', form=form)


@app.route('/<int:id>')
def short_url_view(id):
    form = YaCutForm()
    obj = URLMap.query.get_or_404(id)
    return render_template('index.html', form=form, obj=obj)
