import os
from urllib import request
from flask import Flask, render_template, request, session
import base64
from model import SavedTotal

app = Flask(__name__)
default_key = b'\xd6\xc9G\xd0\xderS?\xdb\xdd\xf5\xb6\xfe\xc7P\xa5K\xe3!\xca\xee\x8d\xa9\x7f'
app.secert_key = os.environ.get('SECERT_KEY', default_key)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if 'total' not in session:
        session['total'] = 0

    if request.method == 'POST':
        number = int(request.form['number'])
        session['total'] += number
    return render_template('add.jinja2', session = session)

@app.route('/save', methods = ['POST'])
def save():
    total = session.get('total', 0)
    code = base64.b32encode(os.urandom(8)).decode().strip("=")

    saved_total = SavedTotal(value=total, code=code)
    saved_total.save()

    return render_template('saved.jinja2', code=code)

if __name__=="__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='127.0.0.1', port=port, debug=True)
