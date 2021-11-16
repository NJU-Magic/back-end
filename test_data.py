import socket
import fcntl
import struct
import os
def get_host_ip():

    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()

    return ip
#获取本机ip
ipaddr = get_host_ip()

Sensor_Database = [
	{
		"net_path": ipaddr,
		"port": 4100,
		"model_path": "/Data/lst_test/SenD/PC/0/normalized_model.obj",
		"mtl_path": "/Data/lst_test/SenD/PC/0/model.mtl",
		"mtl_png_path": "/Data/lst_test/SenD/PC/0/texture.png",
		"cover_path": "/Data/lst_test/SenD/PC/0/image.jpg",
		"description": "3DFuture Model 1",
		"upload_date": "2021-11-13",
		"data_type": "点云"
	},
	{
		"net_path": ipaddr,
		"port": 4100,
		"model_path": "/Data/lst_test/SenD/PC/1/normalized_model.obj",
		"mtl_path": "/Data/lst_test/SenD/PC/1/model.mtl",
		"mtl_png_path": "/Data/lst_test/SenD/PC/1/texture.png",
		"cover_path": "/Data/lst_test/SenD/PC/1/image.jpg",
		"description": "3DFuture Model 2",
		"upload_date": "2021-11-13",
		"data_type": "点云"
	},
	{
		"net_path": ipaddr,
		"port": 4100,
		"model_path": "/Data/lst_test/SenD/PC/2/normalized_model.obj",
		"mtl_path": "/Data/lst_test/SenD/PC/2/model.mtl",
		"mtl_png_path": "/Data/lst_test/SenD/PC/2/texture.png",
		"cover_path": "/Data/lst_test/SenD/PC/2/image.jpg",
		"description": "3DFuture Model 3",
		"upload_date": "2021-11-13",
		"data_type": "点云"
	},
	{
		"net_path": ipaddr,
		"port": 4100,
		"model_path": "/Data/lst_test/SenD/PC/3/model.ply",
		"mtl_path": None,
		"mtl_png_path": None,
		"cover_path": "/Data/lst_test/SenD/PC/3/cover.jpg",
		"description": "Scannet Model 1",
		"upload_date": "2021-11-13",
		"data_type": "点云"
	},
	{
		"net_path": ipaddr,
		"port": 4100,
		"model_path": "/Data/lst_test/SenD/PC/4/model.ply",
		"mtl_path": None,
		"mtl_png_path": None,
		"cover_path": "/Data/lst_test/SenD/PC/4/cover.jpg",
		"description": "Scannet Model 2",
		"upload_date": "2021-11-13",
		"data_type": "点云"
	},
	{
		"net_path": ipaddr,
		"port": 4100,
		"model_path": "/Data/lst_test/SenD/PC/5/model.ply",
		"mtl_path": None,
		"mtl_png_path": None,
		"cover_path": "/Data/lst_test/SenD/PC/5/cover.jpg",
		"description": "Scannet Model 3",
		"upload_date": "2021-11-13",
		"data_type": "点云"
	},
	{
		"net_path": ipaddr,
		"port": 4100,
		"data_path": "/Data/lst_test/SenD/RGB/0.mp4",
		"cover_path": None,
		"description": "Face Video 1",
		"upload_date": "2021-11-13",
		"data_type": "视频"
	},
	{
		"net_path": ipaddr,
		"port": 4100,
		"data_path": "/Data/lst_test/SenD/RGB/1.jpg",
		"cover_path": None,
		"description": "Kitti Dataset 1",
		"upload_date": "2021-11-13",
		"data_type": "图像"
	},
	{
		"net_path": ipaddr,
		"port": 4100,
		"data_path": "/Data/lst_test/SenD/RGB/2.jpg",
		"cover_path": None,
		"description": "3D Future Model",
		"upload_date": "2021-11-13",
		"data_type": "图像"
	},
]

Single_Modal_AlgRes_Database = [
	{
		"net_path": ipaddr,
		"port": 4100,
		"task_type": "检测",
		"input_type":"视频",
		"output_type":"视频",
		"algrithm_name": "rcfnet",
		"process_date": "2021-11-13",
		"input_video_url": "/Data/lst_test/SMRes/detection/0/input.mp4",
		"output_video_url": "/Data/lst_test/SMRes/detection/0/output.mp4",
		"output_detail":[
			{
				"image_gallery":[
					"/Data/lst_test/SMRes/detection/0/540/{}".format(x) for x in os.listdir("/home/magic/NJU-Magic/back-end/Data/lst_test/SMRes/detection/0/540")
				],
				"class": "people1",
				"time": "01:00-01:03"
			},
			{
				"image_gallery":[
					"/Data/lst_test/SMRes/detection/0/677/{}".format(x) for x in os.listdir("/home/magic/NJU-Magic/back-end/Data/lst_test/SMRes/detection/0/677")
				],
				"class": "people2",
				"time": "01:00-01:03"
			},
			{
				"image_gallery":[
					"/Data/lst_test/SMRes/detection/0/877/{}".format(x) for x in os.listdir("/home/magic/NJU-Magic/back-end/Data/lst_test/SMRes/detection/0/877")
				],
				"class": "people3",
				"time": "01:00-01:03"
			}
		]
	},
	{
		"net_path": ipaddr,
		"port": 4100,
		"task_type": "检测",
		"input_type":"点云",
		"output_type":"点云",
		"algrithm_name": "rcfnet",
		"process_date": "2021-11-13",
		"input_model_url": None,
		"output_model_url": None,
	},
	{
		"net_path": ipaddr,
		"port": 4100,
		"task_type": "分割",
		"input_type": "图像",
		"output_type":"图像",
		"algrithm_name": "rcfrgbnet",
		"process_date": "2021-11-13",
		"input_image_url":"/Data/lst_test/SMRes/segmentation/0/input.jpg",
		"output_image_url":"/Data/lst_test/SMRes/segmentation/0/output.png"
	},
	{
		"net_path": ipaddr,
		"port": 4100,
		"task_type": "分割",
		"input_type": "点云",
		"output_type":"点云",
		"algrithm_name": "rcfpcnet",
		"process_date": "2021-11-13",
		"input_model_url":"/Data/lst_test/SMRes/segmentation/1/input.ply",
		"output_model_url":"/Data/lst_test/SMRes/segmentation/1/output.ply"
	},
	{
		"net_path": ipaddr,
		"port": 4100,
		"task_type": "重建",
		"input_type": "点云",
		"output_type":"点云",
		"algrithm_name": "zyjpcnet",
		"process_date": "2021-11-13",
		"input_model_url":"/Data/lst_test/SMRes/reconstruction/0/input.obj",
		"output_model_url":"/Data/lst_test/SMRes/reconstruction/0/output.obj"
	},
	{
		"net_path": ipaddr,
		"port": 4100,
		"task_type": "重建",
		"input_type": "图像",
		"output_type":"点云",
		"algrithm_name": "zyjrgbnet",
		"process_date": "2021-11-13",
		"input_image_url":"/Data/lst_test/SMRes/reconstruction/1/input.jpg",
		"output_model_url":"/Data/lst_test/SMRes/reconstruction/1/output.obj"
	},
]

BIM_Database = [
	{
		"net_path": ipaddr,
		"port": 4100,

		"model_path": "/Data/lst_test/SenD/PC/0/normalized_model.obj",
		"mtl_path": "/Data/lst_test/SenD/PC/0/model.mtl",
		"mtl_png_path": "/Data/lst_test/SenD/PC/0/texture.png",

		"cover_path": "/Data/lst_test/SenD/PC/0/image.jpg",
		"description": "3DFuture Model 1",
	}
]