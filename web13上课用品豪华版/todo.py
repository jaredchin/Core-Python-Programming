from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import Blueprint
from flask import abort

from models import Todo


# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字，第二个参数是套路
main = Blueprint('todo', __name__)


@main.route('/')
def index():
    # 查找所有的 todo 并返回
    todo_list = Todo.query.all()
    return render_template('todo_index.html', todos=todo_list)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    t = Todo(form)
    if t.valid():
        t.save()
    else:
        abort(400)
    # 蓝图中的 url_for 需要加上蓝图的名字，这里是 todo
    return redirect(url_for('todo.index'))

