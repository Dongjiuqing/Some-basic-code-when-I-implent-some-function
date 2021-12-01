# -*- coding: UTF-8 -*-
import os
action_set = [1, 2, 3, 10, 11, 12, 16, 17, 28, 29, 30, 31, 32, 41, 44, 47]

# 获得文件夹下文件名列表
path = "/Volumes/FILES/2s-AGCN-master16/dataset/nturgb+d_skeletons/"

file_list = os.listdir(path)

# 选择要重命名的文件夹路径
os.chdir(path)

# 将文件名中的Lesson和空格用空字符串替代
for filename in file_list:
    action_class = int(filename[filename.find('A') + 1:filename.find('A') + 4])

    if action_class == 10:
        os.rename(filename, filename.replace("A010", "A004"))
    elif action_class == 11:
        os.rename(filename, filename.replace("A011", "A005"))
    elif action_class == 12:
        os.rename(filename, filename.replace("A012", "A006"))
    elif action_class == 16:
        os.rename(filename, filename.replace("A016", "A007"))
    elif action_class == 17:
        os.rename(filename, filename.replace("A017", "A008"))
    elif action_class == 28:
        os.rename(filename, filename.replace("A028", "A009"))
    elif action_class == 29:
        os.rename(filename, filename.replace("A029", "A010"))
    elif action_class == 30:
        os.rename(filename, filename.replace("A030", "A011"))
    elif action_class == 31:
        os.rename(filename, filename.replace("A031", "A012"))
    elif action_class == 32:
        os.rename(filename, filename.replace("A032", "A013"))
    elif action_class == 41:
        os.rename(filename, filename.replace("A041", "A014"))
    elif action_class == 44:
        os.rename(filename, filename.replace("A044", "A015"))
    elif action_class == 47:
        os.rename(filename, filename.replace("A047", "A016"))
    else:
        print("action_class is ",action_class)
