import requests
from flask_cors import *
from flask import Flask, render_template, Response
from flask import request
from flask import jsonify
from test_data import *

app = Flask(__name__, static_folder='./Data')
CORS(app, supports_credentials=True)
 # 允许跨域

@app.route('/getAllSensorData', methods=['POST'])
@cross_origin()
def getAllSensorData():
    return jsonify({"res": Sensor_Database})

@app.route('/getAllSMResData', methods=['POST'])
@cross_origin()
def getAllSMResData():
    return jsonify({"res": Single_Modal_AlgRes_Database})

@app.route('/detectionvideo', methods=['POST'])
@cross_origin()
def detectionvideo():
    return jsonify({"res": Single_Modal_AlgRes_Database[0]})

if __name__ == '__main__':
	# 你自己定义端口，port=4001等，其余不要动
    app.run(host='0.0.0.0', port=4100 ,debug=True)
    