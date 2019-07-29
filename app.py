from flask import Flask, render_template, request, redirect
import json
from util.encode_decode import *
from util.common import tolist
from model.operation import *

app = Flask(__name__)

app.config.from_pyfile('./config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        form_data = request.form
        original_url = form_data.get('url')
        if original_url:
            new_inserted_record_id = insert('urls', original_url)
            encode = toBase62(new_inserted_record_id)
            short_url = request.host+'/'+encode
            return render_template('index.html', short_url = short_url)
    return render_template('index.html')

@app.route('/<short_url>', methods=['GET'])
def get_short_url(short_url):
        decoded_str = toBase10(short_url)
        redirect_url = find_and_update('urls', decoded_str)
        if redirect_url != None:
            return redirect(redirect_url, code=302)
        return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        serch_str = json.loads(request.data.decode('utf-8'))
        res_obj = find('urls', serch_str)
        res_list = tolist(res_obj, request.host)
        return  json.dumps({"message":"success", "urls": res_list}), 200, {'ContentType':'application/json'}
    return  json.dumps({"message":"Please provide search string", "urls": []}), 200, {'ContentType':'application/json'}


if __name__ == '__main__':
    from model.schema import init_db
    init_db()
    db.init_app(app)
    app.run(debug = True)
