import requests
from flask_cors import *
from flask import Flask, render_template, Response
from flask import request
from flask import jsonify


app = Flask(__name__)
CORS(app, supports_credentials=True) # 允许跨域

# 定义你的服务接口，接口名为api1（接口名你自己设定），请求方式为POST（POST方式不要改）
@app.route('/vgnet', methods=['POST'])
@cross_origin() # 这句话一定要加上，允许跨域
def vgnet():
	## 这里举一个例子，例如，我输入的是一段视频，输出是一个三维模型，那么，我会告诉你视频地址在哪，然后，你将三维模型存储在文件里，返回给我三维模型文件地址
    input_image_path = request.get_json()['input_image_path']
    output_folder = request.get_json()['output_folder']
    
    try:
    	# 这里开始写你的算法，例如
    	model_path = reconstruct(input_image_path,output_folder) # 重建并返回结果地址
    	
    	# 返回结果至前端，包括处理是否成功 success字段，以及你的结果字段 model_path
    	return jsonify({
    		"sucess": 1,
    		"model_path": model_path
    		})
    except Exception as e:
    	# 捕获异常，例如你的算法中间出错了，出错信息要提示

    	# 返回异常信息， 包括处理失败字段success 0，以及错误信息 error_info
    	return jsonify({
    		"sucess": 0,
    		"error_info": str(e)
    		})

import sys
sys.path.append("../Service/wuyj/URA")
from src.models import models
from src.losses import loss
from src.dataset import datasets
import soft_renderer.functional as srf
import yaml
import argparse,os
import numpy as np
from src.training import training
import torch.optim as optim
import torch
import urllib
from scipy import misc
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu") 

def reconstruct(input_image_path,output_folder):
#    filename = img_url.split('/')[-1]
#    try:
#        urllib.request.urlretrieve(img_url,filename)
#    except Exception as e:
#        print(e)
    
    f = open('../Service/wuyj/URA/configs/shapenet/shapenet_1c_02691156.yaml')
    cfg = yaml.load(f)
    f.close()
    # make model
    model_R = models.Reconstructor('../Model/wyj/URA/sphere_642.obj',cfg).to(device)
    checkpoint = torch.load('../Model/wyj/URA/02691156-R.pth.tar')
    model_R.load_state_dict(checkpoint['model_R'])
    model_R.eval()
    input_image_path = '..'+input_image_path
    output_folder = '..'+ output_folder
    temp_img = misc.imread(input_image_path)
    temp_img = misc.imresize(np.array(temp_img),size=(64,64)) 
    temp_img = temp_img.transpose(2,0,1)
    img = torch.FloatTensor(temp_img.astype('float32') / 255.).unsqueeze(0).to(device)
    vertices, faces,_ = model_R.reconstruct(img)
    srf.save_obj(os.path.join(output_folder,'model.obj'),vertices[0],faces[0])
    return 'model.obj'





if __name__ == '__main__':
	# 你自己定义端口，port=4001等，其余不要动
    app.run(host='0.0.0.0', port=4000 ,debug=True)
    