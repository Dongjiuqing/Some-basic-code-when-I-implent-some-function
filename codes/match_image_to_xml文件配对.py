import os
from shutil import copy

image_path = '/Users/Dong/Desktop/test/dataset_org/train'
xml_path = '/Users/Dong/Desktop/test/dataset_org/train_xml'

img_list = []
xml_list = []
# 保存所有的图像名
for root, dirs, files in os.walk(image_path):
    for file in files:
        filename = file[:-4]
        img_list.append(filename)

# 保存所有的标签名
for root, dirs, files in os.walk(xml_path):
    for file in files:
        filename = file[:-4]
        xml_list.append(filename)

print(len(img_list))
print(len(xml_list))

# 因为我的情况是每个图像都有标签，而有些标签的图像没了。
# 因此我遍历所有的标签名，如果能和图像名对应不上，那么就删除这个标签。相反您也可以拿同样的方法去删除图像。
for i in xml_list:
    if i not in img_list:
        xml_path_abs = os.path.join(xml_path, i) + '.xml'
        os.remove(xml_path_abs)
