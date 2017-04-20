#-*- encoding:UTF-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__)
# 开头，行语法表达(line statements)
app.jinja_env.line_statement_prefix = '#'

@app.route('/index/')
@app.route('/')
def index():
    return 'hello'

@app.route('/profile/<int:uid>/', methods=['GET', 'POST'])
def profile(uid):
    # return 'profile:' + str(uid)
    colors = ('red', 'green')
    dicts = {'name': 'zhangsan', 'age': '12'}
    return render_template('profile.html', uid = uid, colors = colors, dicts = dicts)

@app.route('/request/')
def demo_request_response():
    res = ''
    for property in dir(request):
        res = res + str(property) + '#<br>' + str(eval('request.' + property)) + '<br>'
    return res

if __name__ == '__main__':
    app.run(debug=True)