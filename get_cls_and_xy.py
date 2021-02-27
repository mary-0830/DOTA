
# coding:utf-8
# 读DOTA数据集的xml文件，得到每个对象的类别以及每个框的坐标，并存到tmp1.txt
# 以下介绍两种获取对象类别和坐标的方法，分别使用xml元素树和切分的方法，供大家使用。

# -*- coding: utf-8 -*-
# 方法一：用元素树的方法
# 读xml文件中的一个rect
import xml.etree.ElementTree as ET
import sys
import numpy as np
#import importlib
 
#importlib.reload(sys)
#sys.setdefaultencoding('utf-8')
xml_path="D:/datasets/DOTA_clip/val/labeltxt/P0003_0000_0000.xml"
root = ET.parse(xml_path).getroot() #获取元素树的根节点
rect={}
objects=[]
line=[]
for name in root.iter('name'):
    rect['name'] = name.text
for ob in root.iter('object'):
    for bndbox in ob.iter('bndbox'):
        for x0 in bndbox.iter('x0'):
            rect['x0'] = x0.text
        for y0 in bndbox.iter('y0'):
            rect['y0'] = y0.text
        for x1 in bndbox.iter('x1'):
            rect['x1'] = x1.text
        for y1 in bndbox.iter('y1'):
            rect['y1'] = y1.text
        for x2 in bndbox.iter('x2'):
            rect['x2'] = x2.text
        for y2 in bndbox.iter('y2'):
            rect['y2'] = y2.text
        for x3 in bndbox.iter('x3'):
            rect['x3'] = x3.text
        for y3 in bndbox.iter('y3'):
            rect['y3'] = y3.text
        line = rect['name'] + " "+ rect['x0']+ " "+rect['y0']+" "+rect['x1']+" "+rect['y1']+" "+rect['x2']+" "+rect['y2']+" "+rect['x3']+" "+rect['y3']
#        print(line)
        objects.append(line)
        print(objects)

# f1 = open('D:/datasets/output/tmp1.txt', 'w')
np.savetxt('D:/datasets/output/tmp1.txt', objects, fmt = '%s')


# --------------------------------------------------------------------------
# 方法二：split切分的方法
#import re
#
#xml_path="D:/datasets/DOTA_clip/val/labeltxt/P0003_0000_0000.xml"
#
#text = open(xml_path, 'r').read().split('\n')[20:-2]
#
#for i in range(0, len(text)-1, 16):
#	name = text[i+1].split('>')[1].split('<')[0]
#	x0 = text[i+6].split('>')[1].split('<')[0]
#	y0 = text[i+7].split('>')[1].split('<')[0]
#	x1 = text[i+8].split('>')[1].split('<')[0]
#	y1 = text[i+9].split('>')[1].split('<')[0]
#	x2 = text[i+10].split('>')[1].split('<')[0]
#	y2 = text[i+11].split('>')[1].split('<')[0]
#	x3 = text[i+12].split('>')[1].split('<')[0]
#	y3 = text[i+13].split('>')[1].split('<')[0]
#	output = f'{name} {x0} {y0} {x1} {y1} {x2} {y2} {x3} {y3}'
#	print(output)

