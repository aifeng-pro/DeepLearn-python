# !/usr/bin/python  
# encoding: utf-8
# author: zhangtong

'''
    把文件放置在对应位置
    运行此程序完成对训练集，测试集7/3分
    生成txt文件  train.txt val.txt 
    为目标检测使用的训练集测试集分类
'''

import os
import glob
import numpy as np

file_dir = 'C:/Users/Administrator/Desktop/car_position/category_aircraft/VOC2007/Annotations/'  # 图片路径
files_dir = 'C:/Users/Administrator/Desktop/car_position/category_aircraft/VOC2007/imageSets/Main/'  # txt生成路径
value = 0
with open(files_dir + 'aeroplane_val.txt', 'w') as f:
    pass
with open(files_dir+'aeroplane_train.txt', 'w') as f:
    pass
for root, dirs, files in os.walk(file_dir):
    for i in range(len(files)):
        if value >= len(files)*0.6:
            with open(files_dir+'aeroplane_train.txt', 'a') as f:
                f.write(files[i][:files[i].find('.')]+'\n')
        elif i % 2:
            with open(files_dir+'aeroplane_train.txt', 'a') as f:
                f.write(files[i][:files[i].find('.')]+'\n')
        else:
            print('value', value, 'i', i)
            with open(files_dir+'aeroplane_val.txt', 'a') as f:
                f.write(files[i][:files[i].find('.')]+'\n')
                value += 1

with open('aeroplane_train.txt', 'a')as train_f:
    with open('aeroplane_val.txt', 'a')as val_f:
        for file in glob.glob('./lirang/*/*.jpg'):
            print(os.path.basename(file))
            chance = np.random.randint(100)  # 真随机  8 1 1比例分配训练验证测试集
            print(chance)
            if chance < 20:
                val_f.write(os.path.splitext(os.path.basename(file))[0]+'\n')
            else:
                train_f.write(os.path.splitext(os.path.basename(file))[0]+'\n')
