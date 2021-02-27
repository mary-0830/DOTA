'''
Author: your name
Date: 2021-02-27 12:28:58
LastEditTime: 2021-02-27 12:29:21
LastEditors: your name
Description: In User Settings Edit
FilePath: \dota\modify_cls.py
'''
# -*- coding: UTF-8 -*-
# 修改类别
import json
# json文件转成txt文件
f = open(r"C:\Users\Desktop\val2017_bbox_results.json", 'r', encoding='utf-8')

arr = json.loads(f.read(), strict=False)
f.close()

file_ = open(r"C:\Users\Desktop\retinanet_pre.txt", 'w')

# 下面的代码时获取预测文件中，id,category, score, bbox
for i in arr:
    k = i['image_id']
    if i['category_id'] <= 16:
        file_.write(
        "%08d %d %f %f %f %f %f\n" % (
        i['image_id'], i['category_id'] - 1, i['score'],
        i['bbox'][0], i['bbox'][1], i['bbox'][2], i['bbox'][3]))
    else:
        print("error!")


    # file_.write(
    #     "%08d %d %f %f %f %f %f\n" % (
    #     i['image_id'], i['category_id'], i['score'],
    #     i['bbox'][0], i['bbox'][1], i['bbox'][2], i['bbox'][3]))

file_.close()

