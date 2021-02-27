
# coding:utf-8
# 从预测结果图中找出某个类别的图片

# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# !/usr/bin/env python
import shutil
import os
import glob
from PIL import Image
import re

#指定找到文件后，另存为的文件夹绝对路径
outDir = os.path.abspath('D:/datasets/output') 

#指定第一个文件夹的位置
imageDir1 = os.path.abspath('D:/datasets/DOTA_clip/bridge/val/images')

#定义要处理的第一个文件夹变量
image1 = [] #image1指文件夹里的文件，包括文件后缀格式；
imgname1 = [] #imgname1指里面的文件名称，不包括文件后缀格式

#通过glob.glob来获取第一个文件夹下，所有'.png'文件
imageList1 = glob.glob(os.path.join(imageDir1, '*.png'))

#遍历所有文件，获取文件名称（包括后缀）
for item in imageList1:
    image1.append(os.path.basename(item))

#遍历文件名称，去除后缀，只保留名称
for item in image1:
    (temp1, temp2) = os.path.splitext(item)
    imgname1.append(temp1)

#对于第二个文件夹绝对路径，做同样的操作
imageDir2 = os.path.abspath('D:/datasets/R2CNN_20180922_DOTA_v28/R2CNN_20180922_DOTA_v28')
image2 = []
imgname2 = []
imageList2 = glob.glob(os.path.join(imageDir2, '*.jpg'))
    
        
for item in imageList2:
    image2.append(os.path.basename(item))

for item in image2:
    (temp1, temp2) = os.path.splitext(item)
    temp3 = temp1[0:15]  # 取前15位字符
    imgname2.append(temp3)

#通过遍历，获取第一个文件夹下，文件名称（不包括后缀）与第二个文件夹相同的文件，
#并另存在outDir文件夹下。文件名称与第一个文件夹里的文件相同，后缀格式亦保持不变。
List = []
for item1 in imgname1:
    for item2 in imgname2:
        if item1 == item2:
            temp = item1
            List.append(temp)
#            print(List)
#            print(temp)
# 如何在两个列表中，取出第二个列表对应的第一个列表的元素 .
#1，先根据数字在第二个列表的位置找第一个列表的数
#2，再根据第一个列表数字位置找第二个
        
print(List)
for i in List:
    # 字符串前加上f可以使得{}里的变量不被转换成字符串
    old_path0 = f'D:/datasets/R2CNN_20180922_DOTA_v28/R2CNN_20180922_DOTA_v28/{i}_r.jpg'
    old_path1 = f'D:/datasets/R2CNN_20180922_DOTA_v28/R2CNN_20180922_DOTA_v28/{i}_h.jpg'
    new_path0 = f'D:/datasets/output/bridge/{i}_r.jpg'
    new_path1 = f'D:/datasets/output/bridge/{i}_h.jpg'
    shutil.copy2(old_path0, new_path0); shutil.copy2(old_path1, new_path1)
                      
