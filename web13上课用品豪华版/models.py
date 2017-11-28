from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 以下都是套路
app = Flask(__name__)
app.secret_key = 'secret key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 指定数据库的路径
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/pingjufenxi?charset=utf8'

db = SQLAlchemy(app)


# 定义一个 Model，继承自 db.Model
class Todo(db.Model):
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


if __name__ == '__main__':
    # 先 drop_all 删除所有数据库中的表
    # 再 create_all 创建所有的表
    db.drop_all()
    db.create_all()
    print('rebuild database')
