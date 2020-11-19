from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    greeting = 'こんにちは'
    return render_template('hello.html', hello=greeting)


@app.route('/python')
def hello_python():
    return 'Hello Python!'


@app.route('/week')
def show_week():
    # week = ['月', '火', '水', '木', '金']
    duties = {'月': '佐藤', '火': '鈴木', '水': '清水', '木': '中村', '金': '高橋'}
    # return render_template('week.html', week=week)
    return render_template('week.html', duties=duties)


if __name__ == '__main__':
    app.run(debug=True)
