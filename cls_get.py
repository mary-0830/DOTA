# coding:utf-8
# 分割后的图片中，统计各个类别的图片数量及xml文件

# -*- coding: utf-8 -*-
import os
import os.path
import shutil

# 修改文件的xml和img图片的位置  
fileDir_ann = r'D:/datasets/DOTA_clip/val/labeltxt/'
fileDir_img = r'D:/datasets/DOTA_clip/val/images/'
 #存放包含需要的类的图片
saveDir_img = r'D:/datasets/DOTA_clip/helicopter/val/images'
        
if not os.path.exists(saveDir_img):
    os.mkdir(saveDir_img)
 
 
names = locals()
 
for files in os.walk(fileDir_ann):
    #遍历Annotations中的所有文件
    for file in files[2]:
        print (file + "-->start!")
 
        #存放包含需要的类的图片对应的xml文件
        saveDir_ann = r'D:/datasets/DOTA_clip/helicopter/val/annotations/'
 
        if not os.path.exists(saveDir_ann):
            os.mkdir(saveDir_ann)
        fp = open(fileDir_ann + file)       
        saveDir_ann = saveDir_ann + file
        fp_w = open(saveDir_ann, 'w')
        # 修改为自己数据集的类别
        classes = ['plane', 'baseball-diamond', 'bridge', 'ground-track-field', 
                   'small-vehicle', 'large-vehicle', 'ship', 
                   'tennis-court', 'basketball-court',  
                   'storage-tank', 'soccer-ball-field', 
                   'roundabout', 'harbor', 
                   'swimming-pool', 'helicopter']  
 
        lines = fp.readlines()
 
        #记录所有的\t<object>\n的位置
        ind_start = []
 
        #记录所有的\t</object>\n的位置
        ind_end = []
 
        lines_id_start = lines[:]
        lines_id_end = lines[:]
 
        # 根据xml文件中的格式进行修改
        while "<object>\n" in lines_id_start:
            a = lines_id_start.index("<object>\n")
            ind_start.append(a)
            lines_id_start[a] = "delete"
 
        while "</object>\n" in lines_id_end:
            b = lines_id_end.index("</object>\n")
            ind_end.append(b)
            lines_id_end[b] = "delete"
 
        for k in range(0,len(ind_start)):
            for j in range(0,len(classes)):
                if classes[j] in lines[ind_start[k]+1]:
                    a = ind_start[k]
                    names['block%d'%k] = lines[a:ind_end[k]+1]
                    break
        # 修改为自己所需要的类别，可以创建多个类别
        # 根据xml格式进行修改
        classes1 = '<name>large-vehicle</name>\n'
 
        string_start = lines[0:ind_start[0]]
        print(string_start)
        string_end = lines[ind_end[-1] + 1:]
 
        a = 0
        for k in range(0,len(ind_start)):
            if classes1 in names['block%d'%k]:
                a += 1
                string_start += names['block%d'%k]
 
        string_start += string_end
        for c in range(0,len(string_start)):
            fp_w.write(string_start[c])
        fp_w.close()
 
        if a == 0:
            os.remove(saveDir_ann)
        else:
            # 。png或者是.jpg文件，根据自己的格式进行修改
            name_img = fileDir_img + os.path.splitext(file)[0] + ".png"
            shutil.copy(name_img,saveDir_img)
        fp.close()


