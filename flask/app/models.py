from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from . import db


class Fenxi(db.Model):
    __tablename__ = 'pingjufenxi'
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer)
    competition = db.Column(db.String(40))
    round = db.Column(db.String(20))
    hometeam = db.Column(db.String(40))
    guestteam = db.Column(db.String(40))
    times = db.Column(db.Integer)
    htscore = db.Column(db.Integer)
    gtscore = db.Column(db.Integer)
    result = db.Column(db.Integer)

    def __repr__(self):
        return '<match of %r vs %r>' % (self.hometeam, self.guestteam)

