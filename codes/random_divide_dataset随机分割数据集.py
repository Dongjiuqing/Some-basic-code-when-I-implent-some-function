import os  # os是用来切换路径和创建文件夹的。
import random
from shutil import copy  # shutil 是用来复制黏贴文件的

# "blossom_end_rot", "graymold", "powdery_mildew", "spider_mite", "spotting_disease"

img_path = "/Users/Dong/Desktop/dataPath/data"
labels_path = "/Users/Dong/Desktop/dataPath/labels"

filelist_img_name = []
filelist_label_name = []

for root, dir, filenames in os.walk(img_path):
    for filename in filenames:
        if '.jpg' in filename:
            file_path = os.path.join(root, filename)
            print(file_path)
            filelist_img_name.append(file_path)
        else:
            pass
            # print("it is not a jpg file.", filename)

# .jpg.mat是我的标注文件的后缀名，您修改为自己的xml或者json或者其他类型即可。
for root, dir, filenames in os.walk(labels_path):
    for filename in filenames:
        if '.jpg.mat' in filename:
            filelist_label_name.append(filename.split('.jpg.mat')[0])
        else:
            pass
            # print("it is not a label file.", filename)

print(len(filelist_img_name))
print(len(filelist_label_name))
# 我一共含有580张图片，因此 348 ，464，464-580这几个数字是我自己计算的。我的比例是60% 20% 20%
# 如果您有10000张图片和10000张标注，那么您可以设置为6000，8000，8000:，以此类推
# 我没有写自动创建文件夹的那部分代码，因此你要自己首先把相关文件夹创建好。
random.shuffle(filelist_img_name)
filelist_img_name = filelist_img_name
for tr in filelist_img_name[0:348]:
    copy(tr, '/Users/Dong/Desktop/dataPath_new/data/train/')
    tr = tr.replace('data/', 'labels/')
    tr = tr.replace('.jpg', '.jpg.mat')
    copy(tr, '/Users/Dong/Desktop/dataPath_new/labels/train/')

for val in filelist_img_name[348:464]:
    copy(val, '/Users/Dong/Desktop/dataPath_new/data/val/')
    val = val.replace('data/', 'labels/')
    val = val.replace('.jpg', '.jpg.mat')
    copy(val, '/Users/Dong/Desktop/dataPath_new/labels/val/')

for test in filelist_img_name[464:]:
    copy(test, '/Users/Dong/Desktop/dataPath_new/data/test/')
    test = test.replace('data/', 'labels/')
    test = test.replace('.jpg', '.jpg.mat')
    copy(test, '/Users/Dong/Desktop/dataPath_new/labels/test/')

'''
# matching the images to labels

for k in filelist_img_name:
    if k not in filelist_json_name:
    #print("there is no label of image {}".format(k))
        pass
    else:
        print("ok")

'''
