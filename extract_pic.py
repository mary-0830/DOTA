# -*- coding:utf-8 -*-
# 配合 Extract_category.py 一起用，先Extract_category.py再进行下面的代码操作

import cv2
import numpy as py
import os


def get_pic(txt_path, pic_path, save_path):  
    with open(txt_path, 'r') as fp:
        while(1):
            line = fp.readline()
            if not line:
                print("txt is over!!!")
                break
            str = line.split(" ")
            img_id = str[0]                    
            x = round(float(str[3]))
            y = round(float(str[4]))
            w = round(float(str[5])) + x
            h = round(float(str[6])) + y
            ap = round(float(str[2]), 5)
            if ap >= 0.5:
                if os.path.exists(save_path + img_id + ".png"):  
                    img = cv2.imread(save_path + img_id + ".png") 
                    if str[1] == '1':
                            # cv2.rectangle(img,(x,y-22),(x+50,y),(0,255,0), thickness = -1)
                            cv2.putText(img, "plane", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                            cv2.rectangle(img,(x,y),(w,h),(0,0,255),2,4,0)
                            cv2.circle(img, (x, y), 3, (0, 0, 255), -1)  # 画heatmap
                        
                    elif str[1] == '2':
                        # cv2.rectangle(img,(x,y-22),(x+100,y),(0,0,255), thickness = -1)
                        cv2.putText(img, "ship", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(0,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

                    elif str[1] == '3':
                        # cv2.rectangle(img,(x,y-22),(x+40,y),(172,172,0), thickness = -1)             
                        cv2.putText(img, "stroage-tank", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(172,172,0),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
                    
                    elif str[1] == '4':
                        # cv2.rectangle(img,(x,y-22),(x+35,y),(172,0,172), thickness = -1)                  
                        cv2.putText(img, "baseball-diamond", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(172,0,172),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
                    
                    elif str[1] == '5':
                        # cv2.rectangle(img,(x,y-22),(x+90,y),(255,0,255), thickness = -1)               
                        cv2.putText(img, "tennis-court", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(255,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

                    elif str[1] == '6':
                        # cv2.rectangle(img,(x,y-22),(x+90,y),(255,0,255), thickness = -1)               
                        cv2.putText(img, "basketball-court", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(255,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

                    elif str[1] == '7':
                        # cv2.rectangle(img,(x,y-22),(x+90,y),(255,0,255), thickness = -1)               
                        cv2.putText(img, "ground-track-field", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(255,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
                    
                    elif str[1] == '8':
                        # cv2.rectangle(img,(x,y-22),(x+90,y),(255,0,255), thickness = -1)               
                        cv2.putText(img, "harbor", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(255,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

                    elif str[1] == '9':
                        # cv2.rectangle(img,(x,y-22),(x+90,y),(255,0,255), thickness = -1)               
                        cv2.putText(img, "bridge", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(255,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
                    
                    elif str[1] == '10':
                        # cv2.rectangle(img,(x,y-22),(x+90,y),(255,0,255), thickness = -1)               
                        cv2.putText(img, "small-vehicle", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(255,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

                    elif str[1] == '11':
                        # cv2.rectangle(img,(x,y-22),(x+90,y),(255,0,255), thickness = -1)               
                        cv2.putText(img, "large-vehicle", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(255,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

                    elif str[1] == '13':
                        # cv2.rectangle(img,(x,y-22),(x+90,y),(255,0,255), thickness = -1)               
                        cv2.putText(img, "helicopter", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(255,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

                    elif str[1] == '14':
                        # cv2.rectangle(img,(x,y-22),(x+90,y),(255,0,255), thickness = -1)               
                        cv2.putText(img, "roundabout", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(255,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

                    elif str[1] == '15':
                        # cv2.rectangle(img,(x,y-22),(x+90,y),(255,0,255), thickness = -1)               
                        cv2.putText(img, "soccer-ball-field", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(255,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
                    
                    elif str[1] == '16':
                        # cv2.rectangle(img,(x,y-22),(x+90,y),(255,0,255), thickness = -1)               
                        cv2.putText(img, "swimming-pool", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(255,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

                    cv2.imwrite(save_path + img_id +".png", img)
                    print(str[0]+".png is save....OK~~~")
                elif os.path.exists(pic_path + img_id + ".png") :
                    img = cv2.imread(pic_path + img_id + ".png")    
                    if str[1] == '1':
                            # cv2.rectangle(img,(x,y-22),(x+50,y),(0,255,0), thickness = -1)
                            cv2.putText(img, "plane", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                            cv2.rectangle(img,(x,y),(w,h),(0,0,255),2,4,0)
                            cv2.circle(img, (x, y), 3, (0, 0, 255), -1)  # 画heatmap
                        
                    elif str[1] == '2':
                        # cv2.rectangle(img,(x,y-22),(x+100,y),(0,0,255), thickness = -1)
                        cv2.putText(img, "ship", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(0,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

                    elif str[1] == '3':
                        # cv2.rectangle(img,(x,y-22),(x+40,y),(172,172,0), thickness = -1)             
                        cv2.putText(img, "stroage-tank", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(172,172,0),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
                    
                    elif str[1] == '4':
                        # cv2.rectangle(img,(x,y-22),(x+35,y),(172,0,172), thickness = -1)                  
                        cv2.putText(img, "baseball-diamond", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(172,0,172),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
                    
                    elif str[1] == '5':
                        # cv2.rectangle(img,(x,y-22),(x+90,y),(255,0,255), thickness = -1)               
                        cv2.putText(img, "tennis-court", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(255,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

                    elif str[1] == '6':
                        # cv2.rectangle(img,(x,y-22),(x+90,y),(255,0,255), thickness = -1)               
                        cv2.putText(img, "basketball-court", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(255,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

                    elif str[1] == '7':
                        # cv2.rectangle(img,(x,y-22),(x+90,y),(255,0,255), thickness = -1)               
                        cv2.putText(img, "ground-track-field", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(255,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
                    
                    elif str[1] == '8':
                        # cv2.rectangle(img,(x,y-22),(x+90,y),(255,0,255), thickness = -1)               
                        cv2.putText(img, "harbor", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(255,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

                    elif str[1] == '9':
                        # cv2.rectangle(img,(x,y-22),(x+90,y),(255,0,255), thickness = -1)               
                        cv2.putText(img, "bridge", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(255,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
                    
                    elif str[1] == '10':
                        # cv2.rectangle(img,(x,y-22),(x+90,y),(255,0,255), thickness = -1)               
                        cv2.putText(img, "small-vehicle", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(255,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

                    elif str[1] == '11':
                        # cv2.rectangle(img,(x,y-22),(x+90,y),(255,0,255), thickness = -1)               
                        cv2.putText(img, "large-vehicle", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(255,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

                    elif str[1] == '13':
                        # cv2.rectangle(img,(x,y-22),(x+90,y),(255,0,255), thickness = -1)               
                        cv2.putText(img, "helicopter", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(255,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

                    elif str[1] == '14':
                        # cv2.rectangle(img,(x,y-22),(x+90,y),(255,0,255), thickness = -1)               
                        cv2.putText(img, "roundabout", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(255,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

                    elif str[1] == '15':
                        # cv2.rectangle(img,(x,y-22),(x+90,y),(255,0,255), thickness = -1)               
                        cv2.putText(img, "soccer-ball-field", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(255,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
                    
                    elif str[1] == '16':
                        # cv2.rectangle(img,(x,y-22),(x+90,y),(255,0,255), thickness = -1)               
                        cv2.putText(img, "swimming-pool", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))
                        cv2.rectangle(img,(x,y),(w,h),(255,0,255),2,4,0)
                        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

                    cv2.imwrite(save_path + img_id +".png", img)
                    print(str[0]+".png is save....OK!!!")

if __name__ == '__main__':
    #样本图片路径
    pic_path = r"D:/code/check/test/"  
    # txt存放的路径
    txt_path="D:/code/check/detections_test2017__results.txt"
    # 画出来的图片保存的路径
    save_path="D:/code/check/out/"
    get_pic(txt_path, pic_path, save_path)

