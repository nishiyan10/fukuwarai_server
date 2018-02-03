import os
import io
from split import run_fukuwarai, run_roulette, ocv2b64
from flask import Flask, render_template, request, make_response, jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template("detail.html")


@app.route('/post', methods=['POST'])
def test_image():
    proc  = request.json['method']
    image = request.json['image']
    result = {
        "proc" : proc,
        "image": image
    }
    return make_response(jsonify(result))





@app.route('/image', methods=['POST'])
def upload_image():
    proc  = request.json['method']
    image = request.json['image']

    if request.method == 'POST':
        result = {
            "result": True,
            "data"  : {}
        }
        if   proc == 'fukuwarai':
            result['data'] = run_fukuwarai(image)
        elif proc == 'roulette':
            result['data'] = run_roulette(image)
        else:
            result['result'] = False
            result['data']   = { "error": "Unknown Process method." }

        if "error" not in result['data'] :
            img = {}
            for i, data in enumerate(result['data']):
                # img[data] = ocv2b64( result['data'][data][1] ) #ocv2b64( data )
                img[data] = {}
                img[data]['img'] = ocv2b64(result['data'][data]['img'][1])
                img[data]['w'] = str(result['data'][data]['w'])
                img[data]['h'] = str(result['data'][data]['h'])

            result['data'] = img
    else:
        result = {"error": "POST NotFound."}

    return make_response(jsonify(result))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
