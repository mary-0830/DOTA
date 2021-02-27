# -*- coding: utf-8 -*-
# 读取检测生成的pkl文件    
import pickle, pprint


pkl_file = open(r'D:/datasets/R2CNN_20180922_DOTA_v28/R2CNN_20180922_DOTA_v28_detections_r.pkl', 'rb')

data = pickle.load(pkl_file, encoding='bytes')
pprint.pprint(data)

pkl_file.close()
