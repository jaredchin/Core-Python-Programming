from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class MatchForm(FlaskForm):
    competition = StringField('competition', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('查询')
