import time

from flask import Flask, render_template
from api import param
from api.api import pictrue
import config

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    update_time = time.strftime('%Y年%m月%d日 %H:%M:%S')
    return render_template('index.html', **config.info, time=update_time)


@app.route('/api/')
def app_api():
    cid = param.value('cid')

    pic = pictrue()

    start = param.value('start')
    count = param.value('count')

    if cid is None:
        return pic.i360search()

    if cid == '360new':
        return pic.i360new(start, count)

    if cid == '360tags':
        return pic.i360tags()

    if cid == '360search':
        content = param.value('content')
        return pic.i360search(content, start, count)

    if cid == 'bing':
        return pic.bing(start, count)

    return pic.default(cid, start, count)


if __name__ == '__main__':
    app.run()
