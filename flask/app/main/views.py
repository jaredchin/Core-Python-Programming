from flask import render_template, redirect, url_for, session
from . import main
from . forms import MatchForm
from .. import db
from ..models import Fenxi


@main.route('/', methods=['GET', 'POST'])
def index():
    form = MatchForm()
    match_list = None
    if form.validate_on_submit():
        match_list = Fenxi.query.filter_by(competition=form.competition.data).all()
        print(match_list)
    return render_template('index.html', form=form, match_list=match_list)
