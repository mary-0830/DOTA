# -*- coding:utf-8 -*-
import numpy as np
import json

f = open(r"D:\code\check\detections_test2017__results.json", 'r', encoding='utf-8')
arr = json.loads(f.read())
f.close()

file_ = open(r"D:\code\check\detections_test2017__results.txt", 'w')
for i in arr:
    if i['category_id'] == 5:
        file_.write(
            "%08d %d %f %f %f %f %f\n" % (
            i['image_id'], i['category_id'], i['score'],
            i['bbox'][0], i['bbox'][1], i['bbox'][2], i['bbox'][3]))


