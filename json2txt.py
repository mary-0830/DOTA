
# -*- coding: UTF-8 -*-
import json
# json文件转成txt文件
f = open(r"C:\Users\Desktop\results.json", 'r', encoding='utf-8')

# papers = []
# for line in f.readlines():
#     dic = json.loads(line)
#     papers.append(dic)

arr = json.loads(f.read(), strict=False)
# print(80*'=')
# print(arr)
# print(80*'=')
f.close()

file_ = open(r"C:\Users\Desktop\yolov4_test.txt", 'w')
# x1, y1, x2, y2
# for i in arr:
#     f.write(
#         "%08d %d %f %f %f %f %f\n" % (
#         i['image_id'], i['category_id'], i['score'],
#         i['bbox'][0], i['bbox'][1], i['bbox'][2] + i['bbox'][0], i['bbox'][3] + i['bbox'][1]))



# 下面的代码是获取gt中id,category,bbox
# for i in arr['annotations']:  
#     k = i['image_id']
#     file_.write(
#         "%08d %d %f %f %f %f\n" % (
#         i['image_id'],  i['category_id'],
#         i['bbox'][0], i['bbox'][1], i['bbox'][2], i['bbox'][3]))

# 下面的代码是获取预测文件中的id,category,bbox
# for i in arr:  
#     k = i['image_id']
#     file_.write(
#         "%08d %d %f %f %f %f\n" % (
#         i['image_id'],  i['category_id'],
#         i['bbox'][0], i['bbox'][1], i['bbox'][2], i['bbox'][3]))

# 下面的代码时获取预测文件中，id,category, score, bbox
for i in arr:
    k = i['image_id']
    file_.write(
        "%08d %d %f %f %f %f %f\n" % (
        i['image_id'], i['category_id'], i['score'],
        i['bbox'][0], i['bbox'][1], i['bbox'][2], i['bbox'][3]))

file_.close()


